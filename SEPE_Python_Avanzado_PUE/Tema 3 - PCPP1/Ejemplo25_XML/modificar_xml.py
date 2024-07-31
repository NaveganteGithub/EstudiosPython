import xml.etree.ElementTree as xml_tree

empleados = xml_tree.parse("empleados_2.xml")
root = empleados.getroot()

for hijo in root:
    asignado = xml_tree.SubElement(hijo, 'asignado', {'proyecto': 'BBVA'})

empleados.write("empleado_4.xml", method='')
