# 03 Estructuras de Control

Las estructuras de control permiten modificar el flujo lineal de ejecución de un programa, ejecutando ciertos bloques de código solo cuando se cumplen condiciones específicas.

---

## Condicional `if`

Se utiliza para tomar decisiones. Por ejemplo, antes de realizar una división debemos verificar que el denominador $b$ sea distinto de cero ($b \neq 0$):

```python
a = 8
b = 2

if b != 0:
    print(a / b)
```

### Reglas clave:
* La condición va seguida de dos puntos (`:`).
* El bloque de código condicionado **debe estar indentado**.

```python
if b != 0:
    c = a / b
    d = c + 1
    print(d)
```

---

## Uso de `else` y `elif`

* **`else`:** Se ejecuta de forma excluyente cuando la condición del `if` resulta falsa.
* **`elif`:** Permite evaluar múltiples condiciones consecutivas.

```python
x = 5

if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")
```

> **Nota:** En Python puede existir un único `if` y un único `else` por estructura, pero múltiples bloques `elif`. Python no posee una sentencia `switch/case` tradicional en sus versiones clásicas.

---

## Bucle `for`

Se utiliza para iterar sobre una secuencia de elementos (listas, tuplas, rangos, etc.).

```python
for variable in secuencia:
    # Bloque de código a ejecutar en cada iteración
```

Ejemplo utilizando `range()`:

```python
for i in range(5):
    print("Iteración:", i)
```

**Salida:**
```text
>>> Iteración: 0
>>> Iteración: 1
>>> Iteración: 2
>>> Iteración: 3
>>> Iteración: 4
```

---

## Bucle `while`

Repite un bloque de código mientras la condición evaluada sea verdadera (`True`).

```python
contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1
```

**Salida:**
```text
>>> Contador: 0
>>> Contador: 1
>>> Contador: 2
>>> Contador: 3
>>> Contador: 4
```

---

## Control de Bucles: `break` y `continue`

* **`break`:** Termina la ejecución del bucle inmediatamente.
* **`continue`:** Salta el resto del código de la iteración actual y pasa a la siguiente.

### Ejemplo de `break`
```python
for i in range(10):
    if i == 5:
        break
    print("Iteración:", i)
```

### Ejemplo de `continue`
```python
for i in range(5):
    if i == 2:
        continue
    print("Iteración:", i)
```

**Salida con `continue`:**
```text
>>> Iteración: 0
>>> Iteración: 1
>>> Iteración: 3
>>> Iteración: 4
```