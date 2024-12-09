# Simple is better than complex. - Simple mejor que complejo

## Complejo
import heapq

numeros = [-1, 12, -5, 0, 7, 21, 15, 1]
heapq.heapify(numeros)

numeros_ordenados = []

while numeros:
    numeros_ordenados.append(heapq.heappop(numeros))

print(numeros_ordenados)


## Simple
numeros = [-1, 12, -5, 0, 7, 21, 15, 1]
numeros.sort()

print(numeros)
