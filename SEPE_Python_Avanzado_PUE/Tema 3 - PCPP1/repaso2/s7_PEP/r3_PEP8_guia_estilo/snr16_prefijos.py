# En vez de usar slides para examinar prefijos y sufijos, usa los métodos startswith() y endswith()

texto = "Adan el primer humano, Jesus el hijo de Dios"

## Bien
if texto.endswith("Jesus el hijo de Dios"):
    print("El humano renacido o levantado")

if texto.startswith("Adan el primer humano"):
    print("El humano caido")

## Mal
if texto[:21] == "Adan el primer humano":
    print("El humano caido")
