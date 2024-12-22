# Evita los espacios en blanco innecesarios

## Bueno
mi_abecedario = ["a", {5: "Cinco"}, 0b010010, 0x5f41a59e, (1,2,3,4,5)]
print(mi_abecedario[0:2])
print(mi_abecedario[0::2])
print(mi_abecedario[1:5:3])
print(mi_abecedario[1:5:])

manzanas = 5
platanos = 10
frutas = manzanas + platanos
fruta_texto = "Fruta" * frutas

## Malo
mi_abecedario = ["a" , { 5:  "Cinco" }, 0b010010   , 0x5f41a59e, (1, 2, 3, 4, 5)]
print(mi_abecedario[0 : 2])
print(mi_abecedario[0 : : 2])
print(mi_abecedario[1 :5 :3])
print(mi_abecedario[1: 5:])

manzanas        = 5
platanos        = 10
frutas          = manzanas  + platanos
fruta_texto     = "Fruta"   * frutas
