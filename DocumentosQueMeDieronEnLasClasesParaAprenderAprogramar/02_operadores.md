# 02 Operadores

## Tipos de Datos Primitivos Simples
* **Números (*numbers*):** Secuencia de dígitos (pueden incluir el signo `-` para negativos y `.` para decimales). Ejemplo: `0`, `-1`, `3.1415`.
* **Cadenas (*strings*):** Secuencia de caracteres alfanuméricos que representan texto. Se escriben entre comillas simples o dobles. Ejemplo: `'Hola'`, `"Adiós"`.
* **Booleanos (*boolean*):** Contiene únicamente dos elementos, `True` y `False`, que representan los valores lógicos verdadero y falso.

## Tipos de Datos Primitivos Compuestos (Contenedores)
* **Listas (*lists*):** Colecciones ordenadas y mutables de objetos de distintos tipos. Se representan con corchetes y sus elementos se separan por comas. Ejemplo: `[1, "dos", [3, 4], True]`.
* **Tuplas (*tuples*):** Colecciones ordenadas de objetos de distintos tipos. A diferencia de las listas son **inmutables** (no cambian durante la ejecución). Se representan con paréntesis. Ejemplo: `(1, 'dos', 3)`.
* **Diccionarios (*dictionaries*):** Colecciones de objetos almacenados con una clave asociada. Se representan con llaves, los pares separados por comas y cada par estructurado como `clave: valor`. Ejemplo: `{'pi': 3.1416, 'e': 2.718}`.

---

## Operadores de Asignación
Permiten realizar una operación y almacenar el resultado directamente en la variable inicial.

| Operador | Ejemplo | Equivalente |
|---|---|---|
| `=` | $x = 7$ | $x = 7$ |
| `+=` | $x += 2$ | $x = x + 2$ |
| `-=` | $x -= 2$ | $x = x - 2$ |
| `*=` | $x *= 2$ | $x = x \cdot 2$ |
| `/=` | $x /= 2$ | $x = x / 2$ |
| `%=` | $x \%= 2$ | $x = x \% 2$ |
| `//=` | $x //= 2$ | $x = x // 2$ |
| `**=` | $x **= 2$ | $x = x^2$ |
| `&=` | $x \&= 2$ | $x = x \ \& \ 2$ |
| `|=` | $x |= 2$ | $x = x \ | \ 2$ |
| `^=` | $x \text{^}= 2$ | $x = x \oplus 2$ |
| `>>=` | $x >>= 2$ | $x = x >> 2$ |
| `<<=` | $x <<= 2$ | $x = x << 2$ |

---

## Operadores Aritméticos

```python
2 + 3   # Resultado: 5 (Adición)
5 - 3   # Resultado: 2 (Sustracción)
2 * 3   # Resultado: 6 (Producto)
6 / 3   # Resultado: 2.0 (Cociente)
7 % 3   # Resultado: 1 (Módulo / Resto)
2 ** 3  # Resultado: 8 (Potenciación)
7 // 3  # Resultado: 2 (Cociente entero)
```

> **Relación División:**
> Recordando la fórmula del algoritmo de la división $D = d \cdot c + r$ (Dividendo = divisor $\times$ cociente + resto), el cociente entero `//` y el resto `%` satisfacen esta relación (ej. para $10 // 3 = 3$ y $10 \% 3 = 1$, se cumple $3 \cdot 3 + 1 = 10$).

### Prioridad de Operadores Aritméticos (de mayor a menor)
1. `()` Paréntesis
2. `**` Exponente
3. `-x` Negación
4. `*`, `/`, `//`, `%` Multiplicación, División, Cociente entero, Módulo
5. `+`, `-` Suma, Resta

---

## Operaciones de Comparación

### Con Números

```python
>>> 5 > 6    # Mayor que -> False
>>> 8 >= 5   # Mayor o igual que -> True
>>> 5 < 6    # Menor que -> True
>>> 8 <= 5   # Menor o igual que -> False
>>> 56 == 56 # Igual a -> True
>>> 34 != 59 # Distinto de -> True
```

### Con Cadenas de Texto
Utilizan el orden lexicográfico definido por el código ASCII:

* `c1 == c2`: `True` si son exactamente iguales.
* `c1 > c2`: `True` si `c1` sucede alfabéticamente a `c2`.
* `c1 < c2`: `True` si `c1` antecede a `c2`.
* `c1 != c2`: `True` si son distintas.

```python
>>> 'Python' == 'python'
False
>>> 'Python' < 'python'
True
>>> 'a' > 'Z'
True
```

---

## Operaciones Lógicas
Los valores booleanos son `True` (equivalente a $1$) y `False` (equivalente a $0$).

* `not b`: Negación lógica.
* `b1 and b2`: Conjunción (devuelve `True` solo si ambos son `True`).
* `b1 or b2`: Disyunción (devuelve `True` si al menos uno es `True`).

### Tabla de Verdad

| $x$ | $y$ | `not x` | `x and y` | `x or y` |
|---|---|---|---|---|
| `False` | `False` | `True` | `False` | `False` |
| `False` | `True` | `True` | `False` | `True` |
| `True` | `False` | `False` | `False` | `True` |
| `True` | `True` | `False` | `True` | `True` |

---

## Operaciones con Cadenas

### Acceso a Elementos e Índices

| Cadena | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Índice positivo | 0 | 1 | 2 | 3 | 4 | 5 |
| Índice negativo | -6 | -5 | -4 | -3 | -2 | -1 |

```python
>>> 'Python'[0]
'P'
>>> 'Python'[-1]
'n'
```

### Subcadenas (Slicing): `c[i:j:k]`
Devuelve la subcadena desde el índice `i` hasta el índice previo a `j`, tomando elementos con un paso `k`.

```python
>>> 'Python'[1:4]
'yth'
>>> 'Python'[2:]
'thon'
>>> 'Python'[:-2]
'Pyth'
>>> 'Python'[0:6:2]
'Pto'
```

### Operadores de Cadenas
* `c1 + c2`: Concatenación.
* `c * n`: Repetición $n$ veces.
* `c1 in c2`: Pertenece (subcadena contenida).
* `c1 not in c2`: No pertenece.

```python
>>> 'Me gusta ' + 'Python'
'Me gusta Python'
>>> 'Python' * 3
'PythonPythonPython'
>>> 'tho' in 'Python'
True
```