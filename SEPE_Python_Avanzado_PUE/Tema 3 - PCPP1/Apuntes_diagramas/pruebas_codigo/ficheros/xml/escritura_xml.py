import xml.etree.ElementTree as Xml

elemento_nuevo = Xml.Element('empleado')
Xml.SubElement(elemento_nuevo, "sueldo", {"saldo": "neto"}).text = "2100"

xml_abierto = Xml.parse('empleados.xml')

raiz_xml = xml_abierto.getroot()
raiz_xml.append(elemento_nuevo)

xml_abierto.write("empleados.xml")
