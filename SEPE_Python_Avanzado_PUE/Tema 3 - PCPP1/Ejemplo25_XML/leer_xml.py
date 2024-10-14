import xml.etree.ElementTree as xml_tree

# Elegir el documento.xml que vamos a procesar
empleados = xml_tree.parse('empleados.xml')

# Nos posicionamos en la raiz del documento (root)
root = empleados.getroot()
print(root.tag)

# Recorrer los empleados que tenemos en el documento
for empleado in empleados.findall('empleado'):
    print(empleado.tag)
    for propiedad in empleado:
        if propiedad.tag == 'sueldo':
            print(propiedad.tag, ":", propiedad.text, propiedad.attrib['moneda'])
        else:
            print(propiedad.tag, ":", propiedad.text)


empleado = empleados.find('empleado')
print("Mi empleado unico", empleado.text)
print("Mi empleado unico", empleado.find('id').text)

