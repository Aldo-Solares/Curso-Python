# Projecto 3 - Usando Strings y sus metodos.

texto = input("Ingrese un texto: ")
letras = input("Ingrese 3 letras: ")

# Convert text and entered letters to lowercase
texto = texto.lower()
letras = letras.lower()

letras = list(letras)

# See how many times the letter appears in the text
resultado_l1 = texto.count((letras)[0])
resultado_l2 = texto.count((letras)[1])
resultado_l3 = texto.count((letras)[2])

# See how many words there are in the text
resultado_l4 = len(texto.split())

# See first and last letter
resultado_l5 = texto[0]
resultado_l6 = texto[-1]

# Invert text
resultado_l7 = texto[::-1]

# Check the word python
resultado_l8 = texto.find("python")

if resultado_l8 == -1:
    resultado_l8 = "No esta la palabra python en el texto"
else:
    resultado_l8 = "Si esta la palabra python en el texto"

print(f"La letra '{(letras)[0]}', se encuentra {resultado_l1} veces")
print(f"La letra '{(letras)[1]}', se encuentra {resultado_l2} veces")
print(f"La letra '{(letras)[2]}', se encuentra {resultado_l3} veces")
print(f"El texto '{texto}', tiene {resultado_l4} palabras")
print(f"La primer letra del texto '{texto}', es '{resultado_l5}'")
print(f"La ultima letra del texto '{texto}', es '{resultado_l6}'")
print(f"El texto invertido es '{resultado_l7}'")
print(resultado_l8)