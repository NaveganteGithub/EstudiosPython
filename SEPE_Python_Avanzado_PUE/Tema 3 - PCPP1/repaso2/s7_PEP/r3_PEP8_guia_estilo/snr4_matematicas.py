# Según Donald Knuth el código es mucho más legible si
# se hace un salto de línea antes de cada operador.

manzanas = 8
platano = 9
peras = 10
naranjas = 25
albaricoque = 2
coco = 8
racimos_uvas = 70

manzanas_vendidas = 2
peras_vendidas = 3

oferta = 2

## Bueno
frutas_disponibles = ((manzanas - manzanas_vendidas)
                      + platano
                      + (peras - peras_vendidas)
                      + naranjas
                      + albaricoque
                      + coco
                      + racimos_uvas
                      * oferta)

## Malo

frutas_disponibles = ((manzanas - manzanas_vendidas) + platano + (peras - peras_vendidas) + naranjas + albaricoque
                      + coco + racimos_uvas * oferta)
