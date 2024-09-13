import xml.etree.ElementTree as xml

io_stream = xml.parse('empleados.xml')

elemento1 = xml.Element("empleado", {"id": "00001"})
elemento2 = xml.Element("empleado", {"id": "00002"})
elemento3 = xml.Element("empleado", {"id": "00003"})

xml.SubElement(elemento1, "nombre").text = "Andrea"
xml.SubElement(elemento1, "trabajo").text = "Directora"
xml.SubElement(elemento1, "salario", {"divisa": "euros"}).text = "2000"

xml.SubElement(elemento2, "nombre").text = "Daniel"
xml.SubElement(elemento2, "trabajo").text = "Gerente"
xml.SubElement(elemento2, "salario", {"divisa": "dolar"}).text = "2500"

xml.SubElement(elemento3, "nombre").text = "Alvaro"
xml.SubElement(elemento3, "trabajo").text = "Limpiador"
xml.SubElement(elemento3, "salario", {"divisa": "euros"}).text = "1000"

raiz = io_stream.getroot()
raiz.append(elemento1)
raiz.append(elemento2)
raiz.append(elemento3)

io_stream.write('empleados2.xml')


for tag in io_stream.getroot().findall('empleado'):
    print(tag.attrib['id'])

    print(tag.find('nombre').text)
    print(tag.find('salario').text)