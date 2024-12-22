# No uses operadores == o != usa "is" o "is not" en su lugar

numero = 5
mi_valor_booleano = numero > 2

## Limpio

if mi_valor_booleano:
    print("Correcto")
else:
    print("Incorrecto")

## Bien

if mi_valor_booleano is True:
    print("Correcto")
else:
    print("Incorrecto")

## Mal

if mi_valor_booleano == True:
    print("Correcto")
else:
    print("Incorrecto")

# Usa is not cuando quieras negar un caso is

## Bien

if mi_valor_booleano is not True:
    print("Correcto")

## Mal

if not mi_valor_booleano is True:
    print("Correcto")