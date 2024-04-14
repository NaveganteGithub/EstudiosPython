# Las cadenas de texto se consideran listas de caracteres
texto = "bienvenidos al curso de Python"

# Mostrar solo la palabra bienvenidos
print(texto[0:11])
print(texto.index(" ")) # 11
print(texto[0:texto.index(" ")])

# Mostrar solo la palabra Python
print(texto[texto.index("P"):])
print(texto[24:30])
print(texto[-6:])

# Mostrar solo la palabra curso
print(texto[15:20])
print(texto.index("c"))  # 15
print(texto.index(" ", texto.index("c"))) # 20
print(texto[texto.index("c"):texto.index(" ", texto.index("c"))])

# Mostrar todas las letras de la frase de izda a dcha
print(texto[:])
print(texto[0:])
print(texto[0:len(texto)])

# Mostrar todas las letras de la frase de dcha a izda
print(texto[::-1])

# Mostrar todas las letras de 2 en 2
print(texto[::2])
