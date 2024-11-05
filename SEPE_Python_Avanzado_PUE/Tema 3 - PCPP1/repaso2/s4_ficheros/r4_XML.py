import xml.etree.ElementTree as xml
from xml.dom import minidom

# Crear un documento XML
# https://www.geeksforgeeks.org/create-xml-documents-using-python/

# OPCION 1
documento = minidom.Document()

elemento_raiz = documento.createElement("Empleados")
documento.appendChild(elemento_raiz)

primer_elemento = documento.createElement('Empleado')
elemento_raiz.appendChild(primer_elemento)

segundo_elemento = documento.createElement('Nombre')
segundo_elemento.setAttribute("Completo", "True")
segundo_elemento.TEXT_NODE = "Elena Castellon"
primer_elemento.appendChild(segundo_elemento)

tercer_elemento = documento.createElement('Sueldo')
tercer_elemento.TEXT_NODE = "4150.21"
primer_elemento.appendChild(tercer_elemento)

texto_xml = documento.toprettyxml(indent="\t")

with open("archivo.xml", "wt", encoding="utf-8") as archivo:
    archivo.write(texto_xml)

# OPCION 2 - Esta es la que recomiendo para empezar, porque es bastante corta y facil de aprender

elemento_raiz = xml.Element("Empleados")  # Creas la Raiz

# Creas la etiqueta las subetiquetas
elemento = xml.Element("Empleado")
subelemento1 = xml.SubElement(elemento, "Nombre", {"Completo": "True"}).text = "Daniel Aragón"
subelemento2 = xml.SubElement(elemento, "Sueldo").text = "2000.12"

# Unes el elemento raiz con toda la estructura creada
elemento_raiz.append(elemento)

arbol_xml = xml.ElementTree(elemento_raiz)

with open("archivo2.xml", "wb") as archivo:
    arbol_xml.write(archivo)

# Escribir un documento XML

fichero = xml.parse('./archivo2.xml')
raiz = fichero.getroot()

elemento = xml.Element("Empleado")
subelemento1 = xml.SubElement(elemento, "Nombre", {"Completo": "False"}).text = "David"
subelemento2 = xml.SubElement(elemento, "Sueldo").text = "1587.34"

raiz.append(elemento)

fichero.write("archivo3.xml")

# Leer un documento XML

fichero = xml.parse('./archivo3.xml')
raiz = fichero.getroot()

for empleado in raiz.findall("Empleado"):
    print(empleado)
    print(empleado.find("Nombre").text)
