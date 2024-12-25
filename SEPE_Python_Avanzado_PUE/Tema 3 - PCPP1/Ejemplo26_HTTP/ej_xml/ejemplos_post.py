import requests
import xml.etree.ElementTree as xml

xml_contenido = """
<empleado>
    <id>00134</id>
    <nombre>Daniel Salazar</nombre>
    <email>danisal@gmail.com</email>
    <dpto>Mantenimiento</dpto>
    <sueldo moneda="euros">1500</sueldo>
</empleado>
"""
cabecera = {"Content-type": "application/xml"}


try:
    requests.post("http://localhost/empleados.xml", headers=cabecera, data=xml_contenido)
    resultado = requests.get("http://localhost/empleados.xml")
    print(resultado.text)
except requests.RequestException as e:
    print("Ha fallado", e)
