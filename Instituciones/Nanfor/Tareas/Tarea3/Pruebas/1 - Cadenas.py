cadena = "Soy Ismael Montoro Peñasco, soy de Madrid, tengo 22 años, ahora mismo estoy estudiando."
nombre = "Ismael"

print(len(cadena))
print(max(cadena))

print(min(nombre))

print(cadena.upper())
print(cadena.lower())
print(cadena.title())
print(cadena.capitalize())

print("\n")

cadena = "Soy {}, soy de Madrid, tengo {} años, ahora mismo estoy {}."
print(cadena.format("Ismael Montoro Peñasco", 22, "estudiando"))
cadena = "Soy {2}, soy de Madrid, tengo {0} años, ahora mismo estoy {1}."
print(cadena.format(53, "trabajando", "Lucia Palomares Peña"))
cadena = "Soy {nombre}, soy de Madrid, tengo {edad} años, ahora mismo estoy {estado}."
print(cadena.format(estado="trabajando", nombre="Lucia Palomares Peña", edad=53))

cadena = "Soy {:>8}, soy de Madrid, tengo {:5d} años, ahora mismo estoy {:7}."
print(cadena.format("Ismael Montoro Peñasco", 22, "estudiando"))