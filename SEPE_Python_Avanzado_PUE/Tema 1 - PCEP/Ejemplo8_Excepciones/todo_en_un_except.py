import traceback

# sumar los numeros de una lista
datos = ['1', '2', 'tres', '4', '5']
suma = 0

for idx in range(len(datos) + 1):   # 0, 1, 2, 3, 4, 5
    try:
        # acceder al dato
        dato = datos[idx]
        
        # lo convierto a numero
        numero = int(dato)
        
        # mostramos el numero obtenido
        print("Numero:" + numero) # + solo permite concatenar textos
    
    except (IndexError, ValueError, TypeError, BaseException) as ex:
        print("Error de tipo", type(ex))
        print("Mensaje del error", ex)
        traceback.print_exc()
    else:
        # sumar el numero
        suma += numero
        
print("Suma:", suma)

''' otro ejemplo simple '''
try:
    div = 7/0
except (ValueError, Exception) as e:
    print("error!!!", e)
    traceback.print_exc()
print("Fin")