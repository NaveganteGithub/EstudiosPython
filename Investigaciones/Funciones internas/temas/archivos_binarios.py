
array_bytes = None
ruta = "Investigaciones\\Python\\temas\\"
with open(ruta + "miktex.exe", "rb") as lectura:
    array_bytes = lectura.read()

    print(array_bytes[0:155])
    
    for byte in array_bytes:
        print(byte, end=" ")
        print(chr(byte), end=" ")
        print(bin(byte), end=" ")

print()

with open(ruta + "miktex_2.exe", "wb") as escritura:
    escritura.write(array_bytes)
