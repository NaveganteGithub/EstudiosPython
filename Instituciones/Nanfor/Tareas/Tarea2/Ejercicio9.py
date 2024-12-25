import pandas as pd

datos_importados_automoviles = pd.read_csv('Tarea2\\Automobile_data.csv', sep=',')

automoviles = pd.DataFrame(datos_importados_automoviles)

# Pedir una lista de datos de una columna sin duplicados
list_companies = list(automoviles.loc[:, 'company'].drop_duplicates())

'''
fabricantes = pd.DataFrame(
    datos_importados_automoviles,
    columns=['company']
).drop_duplicates()

fabricantes = fabricantes.values.tolist()
'''

'''
Puedes resolver problemas de logica con los bucles copiando el
codigo de dentro y repitiendolo 2 veces o mas para ver lo que 
pasa, sin olvidarse de los print para poder ver el problema

inplace permite decidir si remplazar (True) o no (False) los valores del 
objeto DataFrame por los de la query, por defecto no remplazara los valores
del DataFrame existente (False)

automoviles.query('company == \'alfa-romero\'', inplace=True)
print(automoviles)

automoviles.query('company == \'volvo\'', inplace=True)
print(automoviles)

automoviles.query('company == \'audi\'', inplace=True) 
print(automoviles)

alfa = automoviles.query('company == \'alfa-romero\'')
print(alfa)
'''

'''
Hay que tener cuidado con el tema de las comas, los espacios, 
las tildes y las concatenaciones, el mas minimo fallo puede 
hacer que tu programa no funcione

Problema
company = automoviles.query(('company == ' + company_now))
print(company)

Solucion
consulta = 'company == \'' + list_companies[0] + '\''
print(consulta)
company = automoviles.query(consulta)
print(company)
'''

'''
Para realizar consultas del tipo group by de sql tienes que hacer lo siguiente.

for company_now in list_companies:
    company = automoviles.query(('company == \'' + company_now + '\''))
    print(company)
'''

'''
Para realizar filtrados personalizados con operaciones especificas

for company_now in list_companies:
    precios = automoviles.query(('company == \'' + company_now + '\'')).loc[:, 'price']
    media_precios = sum(precios) / len(precios)
    print(precios)
    print(media_precios)

# Lo dejo aqui por si acaso hay que hacer la operacion con datos numericos sin duplicados
# precios = automoviles.query(('company == \'' + company_now + '\'')).loc[:, 'price'].drop_duplicates()
'''

for company_now in list_companies:
    precio = automoviles.query(('company == \'' + company_now + '\'')).loc[:, 'price'].mean()
    print('La media de la compañia', company_now, 'tiene una media de', precio, 'euros.')