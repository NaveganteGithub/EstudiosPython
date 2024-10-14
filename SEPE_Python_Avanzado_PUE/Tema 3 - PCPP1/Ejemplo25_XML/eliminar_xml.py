import xml.etree.ElementTree as xml_tree

empleados = xml_tree.parse("empleados_2.xml")
root = empleados.getroot()

for hijo in root:
    hijo.remove(hijo.find("sueldo"))

empleados.write("empleados_3.xml")
