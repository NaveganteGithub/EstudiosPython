# crear un conjunto con las letras de la palabra 'abracadabra'
# que no sean a, ni b, n c

PALABRA = 'abracadabra'

# codigo completo

palabra_nueva = set()

for letra in PALABRA:
    if letra not in ['a', 'b', 'c']:
        palabra_nueva.add(letra)

print(palabra_nueva)

# compresion

palabra_nueva = {letra for letra in PALABRA if letra not in ['a', 'b', 'c']}
print(palabra_nueva)

# Manuel Guirado Muñoz
# Código completo
palabra = {'a','b','r','a','c','a','d','a','b','r','a'}
quitar = {'a','b','c'}
# Compresión
print(palabra.difference(quitar))

# Sebastian Luna Sanchez
print(set('abracadabra') - {'a','b','c'})