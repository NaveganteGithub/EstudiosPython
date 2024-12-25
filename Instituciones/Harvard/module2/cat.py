i = 1

"""
Si te encuentras con un bucle infinito en linux
tienes la opcion de Ctrl + C para pararlo
"""
"""
while i < 3:
    print("meow")
    i+=1
"""
"""
for i in [0,1,2]:
    print(f"meow {i}")
"""
"""
for i in range(1000000):
    print(f"meow {i}")
"""

"""
En caso de no necesitar una variable se tiene que utilizar _ para indicar que
no se tiene que usar

for _ in range(1000000):
    print("meow")
"""
# Se puede repetir texto sin necesitadad de un bucle
# print("meow" * 3)
# print("meow\n" * 3)
# print("meow\n" * 3, end="")

"""
En vez de utilizar este algoritmo para realizar un bucle que dure x veces
n = -1 # Valor inneceario
while n < 0:
    n = int(input("What´s n? "))
"""
"""
Utiliza este en el cual no tienes que almacenar valores innecesarios


while True:
    n = int(input("What´s n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What´s n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()