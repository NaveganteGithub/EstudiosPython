import xml.etree.ElementTree as Xml

fichero = Xml.parse('empleados2.xml')

raiz = fichero.getroot()

elementos = fichero.findall('empleado')

for e in elementos:
    element_remove = e.find('Genero')
    e.remove(element_remove)

fichero.write('empleados3.xml')
