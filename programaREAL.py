import math
import socket
import time

import network
import ntptime
from machine import Pin, PWM, SPI


# Copiar este archivo en las dos Pico 2 W y cambiar el rol en cada una.
ROL = "paciente"  # En la otra placa: "enfermera"
WIFI_NOMBRE = "TU_WIFI"
WIFI_CLAVE = "TU_CLAVE"
IP_ENFERMERA = "192.168.1.50"
PUERTO = 5000
MUESTRAS = 6
INTERVALO = 5
ARCHIVO = "registro.csv"
HORAS_24 = 24 * 60 * 60


def conectar_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        wifi.connect(WIFI_NOMBRE, WIFI_CLAVE)
        for intento in range(20):
            if wifi.isconnected():
                break
            time.sleep(1)
    if not wifi.isconnected():
        raise OSError("No se pudo conectar al Wi-Fi")
    print("IP:", wifi.ifconfig()[0])
    return wifi


def leer_temperatura():
    cs.value(0)
    spi.write(b"\x80\xc1")
    cs.value(1)
    time.sleep_ms(70)
    cs.value(0)
    spi.write(b"\x01")
    datos = spi.read(2)
    cs.value(1)
    if datos[1] & 1:
        return None
    resistencia = (((datos[0] << 8) | datos[1]) >> 1) * 430 / 32768
    if resistencia < 80 or resistencia > 125:
        return None
    a = 3.9083e-3
    b = -5.775e-7
    return (-a + math.sqrt(a * a - 4 * b * (1 - resistencia / 100))) / (2 * b)


def clasificar(temperatura):
    if temperatura is None or temperatura < 25 or temperatura > 45:
        return "error"
    if temperatura < 36:
        return "hipotermia"
    if temperatura > 37:
        return "fiebre"
    if temperatura >= 36.8:
        return "febricula"
    return "normal"


def guardar(ahora, mensaje):
    try:
        with open(ARCHIVO) as archivo:
            inicio = int(archivo.readline())
    except (OSError, ValueError):
        inicio = 0
    if not inicio or ahora - inicio >= HORAS_24 or ahora < inicio:
        with open(ARCHIVO, "w") as archivo:
            archivo.write("{}\n".format(ahora))
    with open(ARCHIVO, "a") as archivo:
        archivo.write(mensaje)


def enviar(mensaje):
    conexion = socket.socket()
    try:
        conexion.settimeout(3)
        conexion.connect((IP_ENFERMERA, PUERTO))
        conexion.write(mensaje.encode())
        if conexion.recv(16) != b"OK\n":
            raise OSError("Sin respuesta de enfermeria")
    finally:
        conexion.close()


def paciente():
    global spi, cs
    spi = SPI(0, baudrate=1000000, polarity=0, phase=1,
              sck=Pin(18), mosi=Pin(19), miso=Pin(16))
    cs = Pin(17, Pin.OUT, value=1)
    wifi = conectar_wifi()
    try:
        ntptime.settime()
    except OSError:
        if time.localtime()[0] < 2024:
            raise OSError("Se necesita hora de internet para guardar 24 horas")

    while True:
        temperaturas = []
        estados = []
        for numero in range(MUESTRAS):
            temperatura = leer_temperatura()
            temperaturas.append(temperatura)
            estados.append(clasificar(temperatura))
            print("Medicion", numero + 1, temperatura, estados[-1])
            time.sleep(INTERVALO)

        if "error" in estados:
            resultado = "error"
        elif estados.count("fiebre") == MUESTRAS:
            resultado = "fiebre"
        elif estados.count("hipotermia") == MUESTRAS:
            resultado = "hipotermia"
        elif estados.count("normal") == MUESTRAS:
            resultado = "normal"
        elif all(estado in ("normal", "febricula") for estado in estados):
            resultado = "febricula"
        else:
            resultado = "observacion"

        ahora = time.time()
        valores = ",".join("{:.2f}".format(t) if t is not None else "error"
                           for t in temperaturas)
        mensaje = "{},{},{}\n".format(ahora, valores, resultado)
        guardar(ahora, mensaje)
        print("Bloque:", resultado)
        try:
            if not wifi.isconnected():
                wifi = conectar_wifi()
            enviar(mensaje)
        except OSError as error:
            print("No se pudo enviar:", error)


def enfermera():
    rojo = Pin(2, Pin.OUT)
    verde = Pin(15, Pin.OUT)
    azul = Pin(4, Pin.OUT)
    buzzer = PWM(Pin(5), freq=2000, duty_u16=0)
    conectar_wifi()
    servidor = socket.socket()
    servidor.bind(("0.0.0.0", PUERTO))
    servidor.listen(1)
    print("Esperando datos del paciente...")
    while True:
        conexion, origen = servidor.accept()
        try:
            conexion.settimeout(3)
            mensaje = b""
            while not mensaje.endswith(b"\n") and len(mensaje) < 128:
                parte = conexion.recv(128 - len(mensaje))
                if not parte:
                    break
                mensaje += parte
            campos = mensaje.decode().strip().split(",")
            if len(campos) != 8 or campos[-1] not in (
                    "fiebre", "hipotermia", "normal", "febricula", "observacion", "error"):
                raise ValueError("Datos incompletos")
            print("Recibido:", campos)
            rojo.value(campos[-1] == "fiebre")
            verde.value(campos[-1] == "normal")
            azul.value(campos[-1] == "hipotermia")
            conexion.write(b"OK\n")
            if campos[-1] in ("fiebre", "hipotermia"):
                buzzer.duty_u16(32768)
                time.sleep(1)
                buzzer.duty_u16(0)
        except (OSError, ValueError) as error:
            print("Error al recibir:", error)
        finally:
            conexion.close()


if ROL == "paciente":
    paciente()
elif ROL == "enfermera":
    enfermera()
else:
    raise ValueError("ROL debe ser paciente o enfermera")