# las aserciones son afirmaciones que si son:
#   - True no pasa nada
#   - False genera un AssertionError

edad = int(input("Introduce tu edad: "))
assert edad >= 18, "No eres mayor todavia"

print("Eres mayor de edad")