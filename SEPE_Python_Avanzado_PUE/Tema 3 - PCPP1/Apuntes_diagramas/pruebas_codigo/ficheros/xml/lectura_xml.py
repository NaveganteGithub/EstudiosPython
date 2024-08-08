import xml.etree.ElementTree as xml

fichero = xml.parse('empleados.xml')

raiz = fichero.getroot()

elementos = raiz.findall('empleado')

for e in elementos:
    print(e.find("sueldo").text)


elemento = raiz.find('empleado')

salario = elemento.find('sueldo')

print(salario.text)
