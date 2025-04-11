# -*- coding: utf-8 -*-
"""Ejercicio_Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p1uTgixBV8z5X92Py__XHuNm5wTT3Omv

# Práctica de la librería Matplotlib

Este es mi notebook relacionado con el ejercicio desarrollado en el curso de Udemy "Python Total".
"""

# Commented out IPython magic to ensure Python compatibility.
# Importamos el módulo de Matplotlib como plt
import matplotlib.pyplot as plt

# La siguiente linea nos permite ver los gráficos directamente al ejecutarlos en el notebook
# %matplotlib inline

# Creamos un gráfico utilizando plt.plot()
plt.plot()

# Graficamos una lista de números
plt.plot([1,2,3,4,5])

# Creamos dos listas, x e y. Llenamos a la lista x de valores del 1 al 100.
x = list(range(101))

# Los valores de y van a equivaler al cuadrado del respectivo valor en x con el mísmo índice
y = list(map(lambda x: x**2, x))

# Graficamos ambas listas creadas
plt.plot(x,y)

"""Hay otra manera de crear gráficos en Matplotlib, utilizando el método orientado a objetos (OO)."""

# Creamos el gráfico utilizando plt.subplots()
fig, ax = plt.subplots()
ax.plot(x,y)

"""Veamos cómo sería un flujo de trabajo en Matplotlib"""

# Commented out IPython magic to ensure Python compatibility.
# Importar y preparar la librería
import matplotlib.pyplot as plt
# %matplotlib inline

# Preparar los datos
x = list(range(101))
y = list(map(lambda x: x**2, x))

# Preparamos el área del gráfico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots()

# Añadimos los datos al gráfico
ax.plot(x,y)

# Personalizamos el gráfico añadiendo título al gráfico y a los ejes x e y
ax.set(title = "Covicho", xlabel = "dias", ylabel = "casos")

# Guardamos nuestro gráfico empleando fig.savefig()
fig.savefig("\Enejmplo.png")

"""Veamos ahora un gráfico de dispersión:"""

#creamos un nuveo set de datos utilizando la librería Numpy
import numpy as np
x_1 = np.linspace(0,100, 20)
y_1 = x_1**2

# Creamos el gráfico de dispersión de x vs y
fig, ax = plt.subplots()
ax.scatter(x_1,y_1)

# Visualizamos ahora la función seno, utilizando np.sin(X)
fig, ax = plt.subplots()
x_2 = np.linspace(-10,10, 100)
y_2 = np.sin(x_2)

ax.scatter(x_2,y_2)

"""Veamos ahora otro tipo de gráfico. Por ejemplo, un gráfico de barras, que por lo general asocia resultados numéricos a variables categóricas (categorías)"""

# Creemos un diccionario con tres platos y su respectivo precio
# Las claves del diccionario serán los nombres de las comidas, y los valores asociados, su precio
comidas = {"pizza":350, "sopa":150, "pollito": 200}

# Crearemos un gráfico de barras donde el eje x está formado por las claves del diccionario,
# y el eje y contiene los valores.
fig, ax = plt.subplots()
ax.bar(comidas.keys(), comidas.values())

# Añadimos los títulos correspondientes
ax.set(title="Precios de comidas", xlabel = "Nombres", ylabel = "Costos")

# Probemos a continuación con un gráfico de barras horizontales
fig, ax = plt.subplots()
ax.barh(comidas.keys(), comidas.values())

# Añadimos los títulos correspondientes
ax.set(title="Precios de comidas", xlabel = "Nombres", ylabel = "Costos")

"""Un gráfico semejante es un histograma. Podemos generar números aleatorios que siguen una distribución normal (que se acumulan en torno a un valor central), con la función randn:"""

# Creamos una distribución de 1000 valores aleatorios distribuidos normalmente
x = np.random.randn(1000)

# Creamos el histograma
fig, ax = plt.subplots()
ax.hist(x)

"""Veamos ahora un caso más complejo, trabajando con subplots, o figuras que cotienen varios gráficos:"""

# Creamos una figura con 4 subgráficos (2 por fila)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

"""Añadimos datos a cada uno de los gráficos (axes)"""

# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax1.plot(x_1, y_1)

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax2.scatter(x_2, y_2)

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values())

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(x)

"""Matplotlib tiene un conjunto de varios estilos disponibles, podemos verificarlos de la siguiente manera:"""

# Verificamos estilos disponibles
plt.style.available

# Cambiamos el estilo predeterminado por "seaborn-whitegrid"
plt.style.use('seaborn-v0_8-darkgrid')

"""Habiendo cambiado el estilo (el cambio más evidente que veremos será una grilla en el fondo de cada gráfico), cambiaremos también los colores de las líneas, puntos y barras en cada uno de los gráficos por códigos hex a nuestra preferencia:

"""

# Copiamos los valores de los gráficos anteriores
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax1.plot(x_1, y_1, color="#fcba03")

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax2.scatter(x_2, y_2, color="#fcba03")

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values(), color="#fcba03")

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(x, color="#fc036b")