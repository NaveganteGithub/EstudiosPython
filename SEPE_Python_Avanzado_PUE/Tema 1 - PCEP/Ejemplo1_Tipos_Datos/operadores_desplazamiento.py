# Desplazamientos hacia la derecha
print(17 >> 1)   # 17 // 2 ** 1
print(17 >> 2)   # 17 // 2 ** 2
print(17 >> 3)   # 17 // 2 ** 3

print(-17 >> 3)   # -17 // 2 ** 3
print(17 >> 0)   # 17 // 2 ** 0

# El desplazamiento ha de ser numero positivo sino genera error
# ValueError: negative shift count
#print(17 >> -3) 

# Cualquier desplazamiento derecha o izquierda el resultado es cero 
print(0 >> 3)   # 0 // 2 ** 3



# Desplazamientos hacia la izquierda
print(17 << 1)   # 17 * 2 ** 1
print(17 << 2)   # 17 * 2 ** 2
print(17 << 3)   # 17 * 2 ** 3

