# Taller 04: Experiencia 01 - Salida Serie y Serial Plotter

## Descripción
Conectar el cursor de un potenciómetro a la entrada analógica de la Raspberry Pi Pico y los extremos de este potenciómetro a $3.3\text{ V}$ y $\text{GND}$ respectivamente.

## Código MicroPython

```python
from machine import ADC
import time

pot = ADC(28)

while True:
    valor = pot.read_u16()
    tension = valor * 3.3 / 65535
    print(f"Tension: {tension:.2f} V")
    time.sleep(0.1)
```

## Visualización con Thonny
1. Antes de ejecutar el programa, verificar que en Thonny esté seleccionada la vista **Plóter** en el menú de visualización.
2. Al ejecutar, en la parte inferior se observará tanto la consola REPL como la gráfica de la tensión en el plóter:

```
Consola:
Tension: 3.08 V
Tension: 3.09 V
Tension: 3.09 V
Tension: 3.11 V
Tension: 3.08 V
...
```

---

## Uso de Serial Plotter Web
Otra alternativa es utilizar un monitor de salida serie externo en la web:

1. Abrir el navegador e ingresar a [serialplotter.io](https://serialplotter.io/).
2. Seleccionar la velocidad estándar de la Pico: **115200 bps**.
3. Hacer clic en **Connect Device** y seleccionar el puerto COM asignado a la Pico.
4. *Nota:* Asegurarse de cerrar la conexión o el programa Thonny antes de conectarse en la web, ya que no se pueden mantener dos conexiones abiertas al mismo puerto serie simultáneamente.