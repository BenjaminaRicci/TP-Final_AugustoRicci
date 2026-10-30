# 05 Funciones Integradas (*Built-in Functions*)

Python y MicroPython incluyen más de 60 funciones integradas disponibles globalmente sin necesidad de importar módulos externos.

---

## Entrada, Salida y Archivos
* `print()`: Muestra texto o valores en la salida estándar (consola).
* `input()`: Lee una cadena de texto introducida por el usuario desde la consola.
* `open()`: Abre un archivo y devuelve un objeto de tipo archivo para lectura/escritura.

---

## Matemáticas y Números
* `abs()`: Devuelve el valor absoluto de un número.
* `divmod()`: Devuelve el cociente y el resto de una división entera como una tupla `(cociente, resto)`.
* `max() / min()`: Devuelven el elemento mayor o menor de un iterable o grupo de argumentos.
* `pow()`: Eleva un número a una potencia ($x^y$).
* `round()`: Redondea un número al número especificado de decimales.
* `sum()`: Suma todos los elementos de un iterable numérico.
* `bin(), hex(), oct()`: Convierten un entero a formato binario, hexadecimal u octal.
* `complex(), float(), int()`: Convierten valores a tipos numéricos complejos, flotantes o enteros.

---

## Manipulación de Secuencias y Colecciones
* `all()`: Devuelve `True` si todos los elementos de un iterable son verdaderos.
* `any()`: Devuelve `True` si al menos un elemento de un iterable es verdadero.
* `enumerate()`: Agrega un contador a un iterable y devuelve tuplas `(índice, valor)`.
* `filter()`: Filtra los elementos de un iterable evaluándolos con una función condicional.
* `len()`: Devuelve la cantidad de elementos de un objeto (longitud).
* `map()`: Aplica una función a cada elemento de un iterable.
* `range()`: Genera una secuencia inmutable de números dentro de un rango.
* `reversed()`: Devuelve un iterador que recorre una secuencia en orden inverso.
* `slice()`: Crea un objeto de recorte (*slice*) para indexación.
* `sorted()`: Devuelve una nueva lista ordenada a partir de un iterable.
* `zip()`: Empareja elementos de múltiples iterables por posición en tuplas.

---

## Creación y Conversión de Tipos
* `bool()`: Convierte un valor a booleano (`True` o `False`).
* `dict(), list(), set(), tuple()`: Crean o convierten estructuras a diccionario, lista, conjunto o tupla.
* `frozenset()`: Crea un conjunto inmutable.
* `str(), bytes(), bytearray(), memoryview()`: Manipulan texto, secuencias de bytes y acceso directo a memoria.
* `chr() / ord()`: Convierten entre caracteres Unicode y sus códigos enteros correspondientes.
* `format()`: Formatea un valor siguiendo una especificación de formato.
* `repr() / ascii()`: Devuelven representaciones en cadena imprimibles o evaluables de un objeto.

---

## Inspección, Objetos y Atributos
* `callable()`: Comprueba si un objeto se puede llamar (como una función o método).
* `dir()`: Lista todos los atributos y métodos válidos de un objeto.
* `getattr(), setattr(), hasattr(), delattr()`: Obtienen, asignan, verifican o eliminan atributos dinámicamente.
* `hash()`: Devuelve el valor *hash* de un objeto.
* `id()`: Devuelve el identificador único en memoria de un objeto.
* `isinstance() / issubclass()`: Validan si un objeto pertenece a una clase o hereda de ella.
* `type()`: Devuelve el tipo de dato de un objeto.
* `vars()`: Devuelve el diccionario interno de atributos (`__dict__`) de un objeto.

---

## Programación Orientada a Objetos
* `classmethod() / staticmethod()`: Decoradores para definir métodos de clase o métodos estáticos.
* `object()`: Instancia de la clase base de la cual heredan todos los objetos en Python.
* `property()`: Crea propiedades administradas mediante métodos de lectura, escritura y borrado.
* `super()`: Otorga acceso a los métodos y atributos de la superclase.

---

## Ejecución, Entorno e Iteración
* `breakpoint()`: Inicia el depurador interactivo de Python (PDB).
* `compile(), eval(), exec()`: Compilan, evalúan o ejecutan código Python dinámicamente.
* `globals() / locals()`: Devuelven diccionarios con las variables del ámbito global o local.
* `help()`: Despliega el sistema interactivo de documentación.
* `iter() / next()`: Obtienen un iterador de un objeto o devuelven su siguiente elemento.