# 04 Funciones

En MicroPython y Python, las funciones se definen utilizando la palabra clave `def`.

## Sintaxis Básica

```python
def nombre_de_la_funcion(parametro1, parametro2, ...):
    # Código que realiza la tarea
    return resultado
```

* **`def`:** Palabra clave que indica la definición de una función.
* **`nombre_de_la_funcion`:** Identificador descriptivo de la función.
* **`parametro1, parametro2, ...`:** Valores recibidos de entrada (opcionales).
* **`return`:** Especifica el valor devuelto. Es opcional si la función no retorna datos.

---

## Ejemplos de Aplicación

### 1. Función simple sin parámetros

```python
def saludar():
    print("¡Hola, mundo!")

# Llamada a la función
saludar()
```

**Salida:**
```text
>>> ¡Hola, mundo!
```

### 2. Función con parámetros

```python
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

# Llamadas a la función
saludar_persona("Juan")
saludar_persona("Ana")
```

**Salida:**
```text
>>> ¡Hola, Juan!
>>> ¡Hola, Ana!
```

### 3. Función con valor de retorno

```python
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamada a la función y almacenamiento del resultado
total = sumar(5, 3)
print(f"La suma es: {total}")
```

**Salida:**
```text
>>> La suma es: 8
```