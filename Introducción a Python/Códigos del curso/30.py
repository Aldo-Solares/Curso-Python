import matplotlib.pyplot as plt

# Preparar los datos
x = list(range(101))
y = list(map(lambda x: x**2, x))

# Preparamos el área del gráfico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots()

# Añadimos los datos al gráfico
ax.plot(x,y)

# Personalizamos el gráfico añadiendo título al gráfico y a los ejes x e y
ax.set(title = "Covicho", xlabel = "dias", ylabel = "casos")

plt.show()