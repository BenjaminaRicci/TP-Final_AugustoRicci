# 01 Tipos de Datos

## Comentarios
Los comentarios no afectan al programa pero son de utilidad para recordar cómo pensamos el programa.

```python
# Esto es un comentario que no afecta a ningún comando

"""
Este tipo de comentarios puede ser de varias líneas
2024 V1.0
"""
```

---

## Variables y Constantes
Una variable puede contener una gran diversidad de tipos de datos, como booleanos, numéricos o cadenas de caracteres (*string*). Para identificarlas les asignamos un nombre compuesto de letras minúsculas o mayúsculas (siendo estas interpretadas como diferentes), y también pueden incluir un guion bajo o un número mientras este no ocupe el primer carácter.

> **Nota - REPL:**
> Tres símbolos de mayor seguidos (`>>>`) indican que estamos en la consola del lenguaje a la espera de interpretar un nuevo comando. Este entorno se denomina **Bucle de Lectura, Evaluación, Impresión** o **REPL** (*Read-Eval-Print-Loop*).

```python
>>> Peso = 87
>>> peso = 12
>>> Peso2 = 8
>>> _peso = 5
```

> **Nota - Constantes:**
> Python no diferencia estrictamente entre constantes y variables, pero es una buena práctica de programación escribir el nombre de las constantes en **MAYÚSCULAS**. Estas convenciones de escritura se referencian en la guía de estilo **PEP-8** (*Python Enhancement Proposals*).

```python
PI = 3.14159265  # Constante
radio = 5.6       # Variable
```

---

## Tipo de Datos
El tipo de variable es asignado dinámicamente según el valor y no debemos definirlo de antemano. La función `type()` permite conocer la clase o tipo de una variable.

```python
nombre = "Hola Mundo"
numero = 89
flotante = 3.14
complejo = 3 + 2j
binario = 0b010110
hexadecimal = 0xf32a
booleano = True

print(type(nombre))       # <class 'str'>
print(nombre)

print(type(numero))       # <class 'int'>
print(numero)

print(type(flotante))     # <class 'float'>
print(flotante)

print(type(complejo))     # <class 'complex'>
print(complejo)

print(type(binario))      # <class 'int'>
print(binario)

print(type(hexadecimal))  # <class 'int'>
print(hexadecimal)

print(type(booleano))     # <class 'bool'>
print(booleano)
```

Los datos de tipo **booleano** pueden tomar dos valores: `True` o `False` (verdadero o falso). Internamente los booleanos son evaluados como enteros con valores $1$ o $0$. Estas palabras clave corresponden al estado lógico y son reservadas.