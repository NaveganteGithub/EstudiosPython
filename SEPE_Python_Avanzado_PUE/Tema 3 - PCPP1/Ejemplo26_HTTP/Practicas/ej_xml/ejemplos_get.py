import requests
import xml.etree.ElementTree as Xml

# https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml

try:
    respuesta = requests.get("http://localhost:3000/empleados.xml")
    conversion = Xml.fromstring(respuesta.text)

    # Metodo 1

    for child in conversion:

        for data in child:
            print(data.tag, data.attrib, data.text)

    # Metodo 2

    empleados = conversion.findall('empleado')
    print(empleados)

    for dato in empleados:
        print(dato.find('sueldo').text)

except requests.RequestException as error:
    print(error)
else:
    print(respuesta.headers)
