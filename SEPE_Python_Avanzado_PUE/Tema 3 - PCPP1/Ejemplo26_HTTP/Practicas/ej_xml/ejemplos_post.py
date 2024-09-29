import requests
import xml.etree.ElementTree as Xml

datos = """
<empleado>
    <id>00134</id>
    <nombre>Daniel Albarez</nombre>
    <email>danialbarez@gmail.com</email>
    <dpto>I+D</dpto>
    <sueldo moneda="dolares">50000</sueldo>
</empleado>
"""
# https://es.stackoverflow.com/questions/79355/cu%C3%A1l-es-la-diferencia-entre-usar-application-xml-y-text-xml
cabecera = {"Content-Type": "application/xml"}

try:
    conversion = Xml.fromstring(datos)
    print(conversion)
    estado = requests.post("http://localhost:3000/empleados.xml", headers=cabecera, data=conversion)
except requests.RequestException as error:
    print(error)
else:
    print(estado.status_code)