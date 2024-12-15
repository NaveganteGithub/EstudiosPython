# Flat is better than nested. -- Plano mejor que anidado
nivel = 5

## Anidado
if type(nivel) is int:
    if nivel == 5:
        if len(str(nivel)) == 1:
            print("Nivel correcto")

## Plano
### Ejemplo 1
if type(nivel) is int and nivel == 5 and len(str(nivel)) == 1:
    print("Nivel correcto")

### Ejemplo 2
autentificador = True
if type(nivel) is not int:
    autentificador = False

if nivel >= 10:
    autentificador = False

if len(str(nivel)) > 1:
    autentificador = False

if autentificador:
    print("Nivel correcto")
