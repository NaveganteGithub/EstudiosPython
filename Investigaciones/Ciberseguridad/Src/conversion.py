def string_to_32bit_pairs(s):
    # Divide el string en partes de 8 caracteres (32 bits cada uno)
    parts = [s[i:i + 8] for i in range(0, len(s), 8)]

    # Convierte cada parte a un entero hexadecimal y almacena en una tupla
    result = tuple(int(part, 16) for part in parts)

    return result


# Ejemplo de uso
string = "0123456789abcdef"
tupla = string_to_32bit_pairs(string)
print(tupla)  # Output: (19088743, 2309737967)




def pairs_to_string(pairs):
    # Convierte cada entero a un string hexadecimal y elimina el prefijo '0x'
    hex_parts = [hex(pair)[2:] for pair in pairs]

    # Asegúrate de que cada parte tenga 8 caracteres (rellenar con ceros a la izquierda si es necesario)
    hex_parts = [part.zfill(8) for part in hex_parts]

    # Une todas las partes en un solo string
    result = ''.join(hex_parts)

    return result


# Ejemplo de uso
tupla = (0x01234567, 0x89abcdef)
string = pairs_to_string(tupla)
print(string)  # Output: 0123456789abcdef
