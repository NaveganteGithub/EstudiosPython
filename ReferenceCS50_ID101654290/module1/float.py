x = float(input("What´s x? ")) # Captura el texto y luego lo convierte a numero
y = float(input("What´s y? "))

# z = round(x + y)
# z = x / y
z = round(x / y)

print(f"{z:,}") # : permite dar formato de separacion a una variable

print(f"{z:.2f}")