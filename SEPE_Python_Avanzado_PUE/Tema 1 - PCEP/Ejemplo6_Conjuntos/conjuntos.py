# conjuntos: colecciones sin orden, no usamos indices
# No permite elementos duplicados, los ignora
# No se garantiza el orden de entrada de los elementos
# Como todas las colecciones, permite elementos de diferentes tipos
# Se crean: {}

frutas = {'manzana', 'naranja', 'pera', 'naranja', 'platano'}

# mostrar el conjunto por pantalla
print(frutas)

# mostrar el tipo del conjunto
print(type(frutas))   # <class 'set'>

# agregar fresas
frutas.add('fresas')
print(frutas)

# eliminar platano
# del borra por posicion
frutas.remove("platano")
print(frutas)

# longitud
print(len(frutas))

# Recorrer conjuntos
for fruta in frutas:
    print(fruta, end=" ")
print()

# Copiar 
otra = frutas.copy()
print(otra)

# Operadores in y not in
print("platano" not in frutas)
print("fresas" in frutas)

# Borrar todos los elementos
frutas.clear()
print(frutas)

