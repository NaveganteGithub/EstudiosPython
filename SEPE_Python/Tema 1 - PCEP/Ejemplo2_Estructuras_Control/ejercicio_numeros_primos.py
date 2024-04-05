# encontrar los numeros primos del 1 al 100
# un numero primo solo es divisible por si mismo y la unidad
# p. e. para probar si 7 es primo, recorremos sus posible divisores del 2 al 6

'''
    Version 1 con variable booleana
'''
for numero in range(2,101) :
    # Doy por hecho que todos los numeros son primos salvo que se demuestre lo contrario
    es_primo = True

    for divisor in range(2, numero) :
        print("Probando divisor", divisor, "para el numero", numero)
        if numero % divisor == 0 :
            es_primo = False
            break  # Damos por terminado el bucle de los divisores
    
    # Cuando termina el bucle de divisores:
    #     puede ocurrir que se ha encontrado un divisor y por tanto no es primo
    #     puede ocurrir que no se han encontrado divisores y el numero  lo consideramos primo      
    if es_primo :
        print(numero, end=" ")
 
        
'''
    Version 2 con contador de divisores
'''
for numero in range (2,101):
    # Contador para llevar la cuenta de los divisores de ese numero
    count = 0
    
    for divisor in range (2, numero): # desde 2 hasta numero-1
        if numero % divisor == 0:
            # Si el numero encuentra un divisor, le sumamos 1 al contador
            count += 1
            break
            
    if count > 0:
        continue
    else:
        print(numero, end=" ")

'''
    Version 3 con bloque else
'''
for numero in range(2, 101):
    for divisor in range(2, numero):
        if numero % divisor == 0:
            break
    else:
        print(numero, end=" ")