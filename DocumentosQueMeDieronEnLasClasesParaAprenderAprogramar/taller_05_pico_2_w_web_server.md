# Taller 05: Adquisición y Control Bidireccional de Datos con Raspberry Pi Pico 2 W

* **Asignatura:** Procesamiento, Adquisición y Análisis de Señales (PAAS)
* **Carrera:** TEM - UNSAM ECyT
* **Placa Objetivo:** Raspberry Pi Pico 2 W (RP2350)
* **Entorno / Lenguaje:** Thonny IDE / MicroPython
* **Autores:** G. La Mura; E. Gulla

---

## 1. Objetivos del Laboratorio
1. Configurar la pila Wi-Fi en la Pico 2 W mediante MicroPython usando la librería `network`.
2. Implementar un servidor web HTTP liviano con sockets TCP en el puerto 80.
3. Adquirir y procesar entradas analógicas (ADC GP26) y digitales (GP14).
4. Controlar actuadores desde la interfaz web (GP15).
5. Comparar el Modo Estación (`STA_IF`) y el Modo Punto de Acceso (`AP_IF`).

---

## 2. Marco Teórico Comparativo

| Parámetro | Modo Estación (`STA_IF`) | Modo Punto de Acceso (`AP_IF`) |
|---|---|---|
| **Rol en la Red** | Cliente Wi-Fi asociado a un router existente. | Servidor / AP emisor autónomo. |
| **Asignación IP** | Dinámica por DHCP (`192.168.1.X`). | Estática por defecto (`192.168.4.1`). |
| **Infraestructura** | Requiere router / hotspot externo. | Autónoma (no requiere router). |
| **Acceso a Internet** | Posible (si el router dispone WAN). | Sin salida a WAN. |

---

## 3. Circuito de Conexión
* **Entrada Analógica (ADC0 - GP26):** Potenciómetro de $10\text{ k}\Omega$ conectado a $3.3\text{ V}$ y $\text{GND}$.
* **Entrada Digital (GP14):** Pulsador con resistencia *pull-down* interna.
* **Salida Digital (GP15):** LED con resistencia de limitación de $330\ \Omega$.

---

## 4. Práctica 1: Servidor Web en Modo Estación (`main_sta.py`)

```python
import network
import socket
import time
from machine import ADC, Pin

# Hardware
adc = ADC(Pin(26))
btn_input = Pin(14, Pin.IN, Pin.PULL_DOWN)
led_output = Pin(15, Pin.OUT)

# Wi-Fi Config
WIFI_SSID = "RED_LABORATORIO"
WIFI_KEY = "CLAVE_LABORATORIO"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_KEY)

print("Conectando a Wi-Fi...")
timeout = 10
while not wlan.isconnected() and timeout > 0:
    time.sleep(1)
    timeout -= 1

if not wlan.isconnected():
    raise RuntimeError("Error de conexión Wi-Fi.")

ip_info = wlan.ifconfig()
print("IP Asignada:", ip_info[0])

def render_html(raw_adc, voltaje, estado_btn, estado_led):
    str_btn = "ALTO (1)" if estado_btn else "BAJO (0)"
    str_led = "ENCENDIDO" if estado_led else "APAGADO"
    return f"""<html><body>
    <h2>Pico 2 W STA</h2>
    <p>ADC GP26: {raw_adc} ({voltaje:.2f} V)</p>
    <p>GP14: {str_btn}</p>
    <p>LED GP15: {str_led}</p>
    <a href="/led=on">Encender LED</a> | <a href="/led=off">Apagar LED</a>
    </body></html>"""

addr = socket.getaddrinfo("0.0.0.0", 80)[-1]
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(1)

while True:
    try:
        conn, client = server.accept()
        request = conn.recv(1024).decode("utf-8")
        if "/led=on" in request:
            led_output.value(1)
        elif "/led=off" in request:
            led_output.value(0)
            
        val_adc = adc.read_u16()
        volt = (val_adc * 3.3) / 65535
        resp = render_html(val_adc, volt, btn_input.value(), led_output.value())
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        conn.send(resp)
        conn.close()
    except Exception as e:
        print("Error:", e)
```

---

## 5. Práctica 2: Servidor Web en Modo Punto de Acceso (`main_ap.py`)

```python
import network
import socket
import time
from machine import ADC, Pin

adc = ADC(Pin(26))
btn_input = Pin(14, Pin.IN, Pin.PULL_DOWN)
led_output = Pin(15, Pin.OUT)

AP_SSID = "Pico2W_Lab_GrupoX"
AP_KEY = "Pico2W_Acceso2026"

ap = network.WLAN(network.AP_IF)
ap.config(essid=AP_SSID, password=AP_KEY)
ap.active(True)

while not ap.active():
    time.sleep(0.1)

ip_info = ap.ifconfig()
print("AP Activo:", AP_SSID, "IP:", ip_info[0])

def render_html_ap(raw_adc, voltaje, estado_btn, estado_led):
    str_btn = "ALTO (1)" if estado_btn else "BAJO (0)"
    str_led = "ENCENDIDO" if estado_led else "APAGADO"
    return f"""<html><body>
    <h2>Pico 2 W AP</h2>
    <p>SSID: {AP_SSID}</p>
    <p>ADC GP26: {raw_adc} ({voltaje:.2f} V)</p>
    <p>Entrada GP14: {str_btn}</p>
    <p>Salida GP15: {str_led}</p>
    <a href="/led=on">Activar Salida</a> | <a href="/led=off">Desactivar Salida</a>
    </body></html>"""

addr = socket.getaddrinfo("0.0.0.0", 80)[-1]
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(1)

while True:
    try:
        conn, client = server.accept()
        request = conn.recv(1024).decode("utf-8")
        if "/led=on" in request:
            led_output.value(1)
        elif "/led=off" in request:
            led_output.value(0)
            
        val_adc = adc.read_u16()
        volt = (val_adc * 3.3) / 65535
        resp = render_html_ap(val_adc, volt, btn_input.value(), led_output.value())
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        conn.send(resp)
        conn.close()
    except Exception as e:
        print("Error AP:", e)
```

---

## 6. Cuestionario de Evaluación
1. **Q1:** ¿Cuáles son las diferencias fundamentales entre una socket `s.listen(1)` bloqueante y un modelo asincrónico basado en `uasyncio` para gestionar múltiples clientes HTTP?
2. **Q2:** Analice la diferencia entre la resolución de 12 bits real del ADC del RP2350 y el entero de 16 bits entregado por `read_u16()`. ¿Cómo influye esto en la cuantización de la medición?
3. **Q3:** En un entorno industrial o de campo, ¿qué ventajas ofrece desplegar un modo AP con IP estática frente al modo STA con DHCP?
4. **Q4:** ¿Qué ocurre con las conexiones socket si el cliente cierra la pestaña del navegador abruptamente antes de recibir la respuesta HTTP completa?