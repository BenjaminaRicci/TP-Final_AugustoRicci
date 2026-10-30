# Taller 01: Uso de GPIO y tiempos de demoras

## Objetivo
Comprender qué es la Raspberry Pi Pico, instalar las herramientas, MicroPython y ejecutar el primer código.

## Tareas previas

### Paso 1
* Hacer un cuadro comparativo entre las capacidades de las Raspberry Pi Pico, Pico W, Pico 2 y Pico 2W.
* Diferencias fundamentales entre los distintos microprocesadores, velocidad, memoria e entradas y salidas GPIO.
* Registrar imágenes del Pin-Out en caso que se requiera las imágenes necesarias para tener como referencia cómo se relacionan los GPIO con el número de pin.

### Paso 2
* Preparación del entorno: Descarga e instalación de Thonny IDE en nuestra PC de trabajo, flasheo del firmware de MicroPython en la placa (modo BOOTSEL).
* Registrar los link y las versiones utilizadas, tanto para el IDE como para firmware.
* Operar con el entorno IDE y la placa para familiarizarse con los comandos y formas de almacenamiento de variables y archivos.

### Paso 3
* Para el manejo de los puertos GPIO y tiempos de demora, necesitaremos librerías específicas, MicroPython dispone de módulos específicos para tales efectos, como `machine` y `time`.
* Buscar documentación para su uso en: [MicroPython Library Docs](https://docs.micropython.org/en/latest/library/index.html)

Ejemplos de configuración:

```python
import machine
led = machine.Pin(2, machine.Pin.OUT) # Configura el pin 2 como salida
led.value(1) # Enciende el LED
```

```python
from machine import Pin
led = Pin("LED", Pin.OUT) # Configurar el pin del LED interno
led.value(1) # Enciende el LED
```

---

## Materiales necesarios

| Cant. | Componentes |
|---|---|
| 1 | Placa Raspberry Pi Pico |
| 2 min | LED (distintos colores) |
| 2 min | Resistores 330 a 470 $\Omega$ limitadora de corriente para los LED |
| 1 | Pulsadores |

---

## Importante
* La placa Raspberry Pi Pico si bien es alimentada con $5\text{ V}$, internamente trabaja con $3.3\text{ V}$. Es importante no exceder esta última tensión en sus GPIO.
* Es fundamental calcular el resistor en serie que debemos ponerle a cada LED para no exceder la corriente máxima que soporta cada GPIO.

---

## Mini Proyecto
Se debe desarrollar un circuito, especificando los puertos utilizados, con al menos dos LED y un pulsador que realice una función determinada (definida para cada proyecto).

Se podrán realizar prototipos simples, a modo prueba de concepto, debiendo documentar cada uno de ellos.

Los LED con su resistor en serie se podrán conectar a GND o a los $3.3\text{ V}$, esto implica consideraciones especiales en la programación; algo similar ocurre con los pulsadores (recordar que se puede utilizar la resistencia pull-up interna).

También el proyecto debe incluir el manejo de tiempos tanto en segundos como en milisegundos.