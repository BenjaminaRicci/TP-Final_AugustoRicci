import math
import time
from machine import Pin, PWM, SPI


MUESTRAS = 6
INTERVALO = 5

# La PT100 necesita un modulo MAX31865 para conectarse a la Pico 2 W.
spi = SPI(0, baudrate=1000000, polarity=0, phase=1,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT, value=1)

led_rojo = Pin(2, Pin.OUT)
led_verde = Pin(15, Pin.OUT)
led_azul = Pin(4, Pin.OUT)
buzzer = PWM(Pin(5), freq=2000, duty_u16=0)


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


print("Prueba de luces y buzzer")
for led in (led_rojo, led_verde, led_azul):
    led.value(1)
    time.sleep_ms(300)
    led.value(0)
buzzer.duty_u16(32768)
time.sleep_ms(300)
buzzer.duty_u16(0)

while True:
    resultados = []
    for numero in range(MUESTRAS):
        temperatura = leer_temperatura()
        if temperatura is None or temperatura < 25 or temperatura > 45:
            resultado = "error"
        elif temperatura < 36:
            resultado = "hipotermia"
        elif temperatura > 37:
            resultado = "fiebre"
        elif temperatura >= 36.8:
            resultado = "febricula"
        else:
            resultado = "normal"
        resultados.append(resultado)
        print("Medicion", numero + 1, temperatura, resultado)
        time.sleep(INTERVALO)

    fiebre = resultados.count("fiebre") == MUESTRAS
    hipotermia = resultados.count("hipotermia") == MUESTRAS
    normal = resultados.count("normal") == MUESTRAS

    led_rojo.value(fiebre)
    led_azul.value(hipotermia)
    led_verde.value(normal)

    if "error" in resultados:
        print("Error de lectura: revisar PT100 y MAX31865")
    elif fiebre or hipotermia:
        print("Alerta:", "fiebre" if fiebre else "hipotermia")
        buzzer.duty_u16(32768)
        time.sleep(1)
        buzzer.duty_u16(0)
    else:
        print("Sin alerta. Resultados:", resultados)