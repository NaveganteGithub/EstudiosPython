import xml.etree.ElementTree as Xml

fichero = Xml.parse('empleados.xml')

raiz = fichero.getroot()

empleados = raiz.findall("empleado")

for e in raiz:
    Xml.SubElement(e, "Genero").text = "Hombre"

fichero.write("empleados2.xml")
