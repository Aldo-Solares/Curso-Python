# -*- coding: utf-8 -*-
"""Ejercicio_numpy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/195TeBFA4BssYaMLgbFUP6YxI6n2xRFVG

# Práctica de la librería Numpy

Este es mi notebook relacionado con el ejercicio desarrollado en el curso de Udemy "Python Total".
"""

# Importamos Numpy con su abreviación "np"
import numpy as np

# Podemos crear arrays de una dimensión con la función np.array()
array = np.array([1, 2, 3])
print(array)
print()
# O un array de dos dimensiones (bidimensional)
array_2 = np.array([[4, 5, 6, 5],[3, 2, 1, 6]])
print(array_2)
print()
# O un array de tres dimensiones (tridimensional)
array_3 = np.array([[4, 5, 6],[3, 2, 1],[4, 4, 4]])
print(array_3)

"""Para cada uno de estos arrays, podemos obtener sus propiedades, tales como su "forma", número de dimensiones, tipos de datos y tamaño."""

# Atributos del array unidimensional (forma, número de dimensiones, tipos de datos, tamaño, y tipo)
print(array.shape)
print(array.ndim)
print(array.dtype)
print(array.size)
print(type(array))

# Atributos del array bidimensional
print(array_2.shape)
print(array_2.ndim)
print(array_2.dtype)
print(array_2.size)
print(type(array_2))

# Atributos del array tridimensional
print(array_3.shape)
print(array_3.ndim)
print(array_3.dtype)
print(array_3.size)
print(type(array_3))

# Importamos pandas como pd, y creamos un DataFrame a partir del array bidimensional
import pandas as pd
df = pd.DataFrame(array_2)
print(df)

# Creamos un array de tamaño 5x10, formado únicamente por unos (1)
array_unos = np.ones((5, 10))
print(array_unos)

# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)
array_ceros = np.zeros((2, 3, 4))
print(array_ceros)

# Creamos un array de números en el rango de 0 a 100, con un paso de 5
array_serie = np.arange(0,101,5)
print(array_serie)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)
array_aleatorio = np.random.randint(0, 11, size=(2, 5))
print(array_aleatorio)

# Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5)
array_aleatorio_2 = np.random.rand(3, 5)
print(array_aleatorio_2)

# Establecemos la "semilla" de números aleatorios en 27
np.random.seed(10000)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)
array_aleatorio_3 = np.random.randint(0, 11, size=(2, 5))
print(array_aleatorio_3)

# Encontramos los valores únicos del array_2
print(np.unique(array_2))

# Extraemos el elemento de índice 1 del array_2
print(array_2[1])

# Extraemos la primera fila del array_2
print(array_2[:1])

# Extraemos los dos primeros datos de la primera fila del array_2
print(array_2[:1, :2])

# Creamos dos arrays de tamaño 3x4: uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos
array_5 = np.random.randint(0, 11, size=(3, 4))
array_6 = np.ones((3, 4))
print(array_5)
print()
print(array_6)

# Sumamos los dos arrays
print(array_5 + array_6)

# Creamos ahora un array de tamaño (4,3) lleno de unos
array_7 = np.ones((4, 3))

# Intentaremos sumar los arrays 6 y 7
# print(array_6 + array_7)

# Entonces crearemos otro array de tamaño (4,3) lleno de unos
array_8 = np.ones((4, 3))

# Restamos el array_8 al array_7
print(array_7 - array_8)

# Creamos otros dos arrays de tamaño 3x3 con números aleatorios del 1 al 5
array_9 = np.random.randint(1, 6, size=(3, 3))
array_10 = np.random.randint(1, 6, size=(3, 3))
print(array_9)
print()
print(array_10)

# Multiplicamos los últimos dos arrays entre sí
print(array_9*array_10)

# Elevamos el array_9 al cuadrado
print(array_9*array_9)

# Buscamos la raíz cuadrada del array_10
print(np.sqrt(array_9))

# Hallamos el promedio de los valores del array_9
print(np.mean(array_9))

# Hallamos el valor máximo de los valores del array_9
print(np.max(array_9))

# Hallamos el valor mínimo de los valores del array_9
print(np.min(array_9))

# Cambiamos la forma del array_9 por una de 9x1, y lo almacenamos como array_11
array_11 = array_9.reshape(9, 1)
print(array_11)

# Transponemos el array_11
print(np.transpose(array_11))

# Comparamos el array_9 y el array_10, para saber cuáles elementos del array_9 son mayores a los del array_10
array_12 = array_9 > array_10
print(array_12)

"""¿Qué tipos de datos forman parte del array de resultados?"""

# Veamos sus nuevos tipos de datos
print(array_12.dtype)

# Alguno de los elementos del array_9 es igual su equivalente del array_10?
print(array_9 > array_10)

# Comparamos nuevamente ambos arrays, en esta ocasión con >=
print(array_9 >= array_10)

# Buscamos los elementos del array_9 que son mayores a 2
print(array_9 > 2)

# Ordenamos de menor a mayor los elementos dentro del array_9
print(np.sort(array_9))