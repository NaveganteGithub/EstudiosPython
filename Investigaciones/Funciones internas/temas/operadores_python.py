a = 5  # Representación binaria: 0b0101
b = 3  # Representación binaria: 0b0011

# Consejo mira la tabla ASCII binaria
# AND
result = a & b
print(result)  # Salida: 1 (0b0001)

# XOR
result = a ^ b
print(result)  # Salida: 6 (0b0110)

# NOT
result = ~a
print(result)  # Salida: -6 (0b1010)

# OR
result = a | b
print(result)  # Salida: 7 (0b0111)

# left shift - Desplazamiento a izquierda
result = a << 1
print(result)  # Salida: 10 (0b1010)

# right shift - Desplazamiento a derecha
result = a >> 1
print(result)  # Salida: 2 (0b0010)


##################################
cadena_a = ord("a")
cadena_b = ord("b")

# AND
result = cadena_a & cadena_b
print(result, bin(result))

# XOR
result = cadena_a ^ cadena_b
print(result, bin(result))

# NOT
result = ~cadena_a
print(result, bin(result))

# OR
result = cadena_a | cadena_b
print(result, bin(result))

result = cadena_a >> 1
print(bin(cadena_a), result, bin(result))

result = cadena_a << 1
print(bin(cadena_a), result, bin(result))

result = cadena_a << 2
print(bin(cadena_a), result, bin(result))