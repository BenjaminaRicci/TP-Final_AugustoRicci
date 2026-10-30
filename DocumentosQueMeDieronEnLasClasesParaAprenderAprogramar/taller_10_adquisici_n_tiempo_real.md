# Taller 10: Adquisición de Datos en Tiempo Real con Raspberry Pi Pico

> **Pregunta Motivadora:**
> ¿Cómo conseguir que una señal analógica sea muestreada a intervalos de tiempo lo más uniformes posible para que luego pueda ser procesada y reconstruida correctamente?

---

## 1. Información General
* **Tema:** Polling, interrupciones y multitarea en MicroPython aplicados a la adquisición de señales analógicas.
* **Plataforma:** Raspberry Pi Pico / Pico W, MicroPython, ADC del RP2040, PC para visualización y procesamiento.
* **Duración sugerida:** 3 a 4 horas.

---

## 2. Objetivos de la Clase
1. Comprender las diferencias entre polling, interrupciones y multitarea/hilos.
2. Implementar las tres estrategias en MicroPython.
3. Utilizar el ADC del RP2040 para adquirir una señal analógica.
4. Comprender la diferencia entre frecuencia de adquisición programada y frecuencia de muestreo efectiva.
5. Medir experimentalmente la separación temporal entre muestras.
6. Identificar el jitter temporal producido por el software.
7. Comprender por qué un muestreo no uniforme puede afectar el procesamiento digital posterior.
8. Relacionar el muestreo temporal con: frecuencia de Nyquist, aliasing, reconstrucción y procesamiento digital de señales.
9. Comparar experimentalmente polling, interrupciones y multitarea.

---

## 3. Concepto Central: Jitter Temporal
Para $f_s = 100\text{ Hz}$, se espera $T_s = \frac{1}{f_s} = 10\text{ ms}$.

* **Muestreo Ideal:** $t_0, t_0+10\text{ms}, t_0+20\text{ms}, t_0+30\text{ms}, \dots$
* **Muestreo Real:** $t_0, t_0+10.3\text{ms}, t_0+19.7\text{ms}, t_0+30.8\text{ms}, \dots$

La diferencia constituye un error temporal denominado **jitter**:
$$t_n = nT_s + \epsilon_n$$

---

## 4. Códigos de Ejemplo

### Lectura Simple con Polling
```python
from machine import ADC
import time

adc = ADC(26)

while True:
    valor = adc.read_u16()
    print(valor)
    time.sleep_ms(100)
```

### Medición de Marca Temporal ($t_n$)
```python
from machine import ADC
import time

adc = ADC(26)

while True:
    t = time.ticks_us()
    x = adc.read_u16()
    print(t, x)
    time.sleep_ms(100)
```

### TP 1: Polling con Temporización Precisa
```python
from machine import ADC
import time

adc = ADC(26)
Ts_us = 100_000
t_proxima = time.ticks_us()

while True:
    t_proxima = time.ticks_add(t_proxima, Ts_us)
    x = adc.read_u16()
    t = time.ticks_us()
    print(t, x)
    while time.ticks_diff(t_proxima, time.ticks_us()) > 0:
        pass
```

### TP 2: Interrupción por Timer
```python
from machine import ADC, Timer
import time

adc = ADC(26)
flag = False

def timer_callback(timer):
    global flag
    flag = True

timer = Timer()
timer.init(period=100, mode=Timer.PERIODIC, callback=timer_callback)

while True:
    if flag:
        flag = False
        t = time.ticks_us()
        x = adc.read_u16()
        print(t, x)
```

### TP 3: Multitarea (`_thread`)
```python
import _thread
import time

def tarea_1():
    while True:
        print("Adquisición")
        time.sleep_ms(100)

_thread.start_new_thread(tarea_1, ())

while True:
    print("Proceso principal")
    time.sleep_ms(250)
```

---

## 5. Tabla Comparativa de Estrategias

| Característica | Polling | Interrupciones | Multitarea |
|---|---|---|---|
| Complejidad | Baja | Media | Alta |
| Facilidad de programación | Alta | Media | Baja |
| Respuesta a eventos | Media | Alta | Alta |
| Control temporal | Limitado | Bueno | Depende de la implementación |
| Recursos compartidos | Simple | Moderado | Complejo |
| Jitter | Elevado | Menor | Variable |
| Depuración | Fácil | Media | Difícil |
| Riesgo de condiciones de carrera | Bajo | Bajo/medio | Alto |

---

## 6. Conclusión
En un sistema de adquisición:
$$x[n] = x(t_n) \quad \text{donde} \quad t_n = t_0 + nT_s + \epsilon_n$$
El objetivo de la arquitectura de software es mantener el jitter ($\epsilon_n$) en niveles mínimos para asegurar la validez del procesamiento posterior.