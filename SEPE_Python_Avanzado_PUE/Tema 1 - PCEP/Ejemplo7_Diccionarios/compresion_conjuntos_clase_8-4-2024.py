# crear un conjunto con las letras de la palabra 'abracadabra'
# que no sean a, ni b, ni c

# codigo completo
#print(set("abracadabra"))
def filtrar() :
    resultado = set()
    for letra in 'abracadabra':
        if letra not in 'abc':
            resultado.add(letra)
    return resultado
print(filtrar())

word = "abracadabra"
print("word = ", word)
# set_word = {}  crea un diccionario
set_word = set()
for letter in word :
    if letter not in ["a", "b", "c"]:
        set_word.add(letter)
print("set_word = ", set_word, type(set_word))



palabra = {'a','b','r','a','c','a','d','a','b','r','a'}
quitar = {'a','b','c'}
print(palabra.difference(quitar))

conjunto = set("abracadabra")
conjunto_quitar = {'a','b','c'}
print(conjunto.difference(conjunto_quitar))#{'r', 'd'}
print(conjunto - conjunto_quitar)#{'r', 'd'}

print(set('abracadabra') - {'a','b','c'})


# compresion
conjunto_letras = {letra for letra in 'abracadabra' if letra not in {'a', 'b', 'c'}}
print(conjunto_letras)

set_word = {letter for letter in word if letter not in ["a", "b", "c"]}
print("set_word_COMP = ", set_word, type(set_word))
