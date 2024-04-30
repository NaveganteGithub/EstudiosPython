import xml.etree.ElementTree as xml_tree

# Elegir el documento.xml que vamos a procesar
empleados = xml_tree.parse('empleados.xml')

# Nos posicionamos en la raiz del documento (root)
root = empleados.getroot()

# Crear un nuevo empleado
nuevo_empleado = xml_tree.Element('empleado')

# Crear las propiedades o subelementos de empleado
xml_tree.SubElement(nuevo_empleado, 'id').text = '0014'
xml_tree.SubElement(nuevo_empleado, 'inombre').text = 'Fernando Alvarez'
xml_tree.SubElement(nuevo_empleado, 'email').text = 'feral@gmail.com'
xml_tree.SubElement(nuevo_empleado, 'dpto').text = 'Contabilidad'
xml_tree.SubElement(nuevo_empleado, 'sueldo', {"moneda": "libras"}).text = '53000'

# Agregamos el nuevo empleado al root
root.append(nuevo_empleado)

# Escribimos el archivo
empleados.write("empleados_2.xml", method='')
