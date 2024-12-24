from odfdo import Document, Paragraph, Header, Style

documento = Document('text')

# Crear un parrafo
texto = "Hola mundo!"
parrafo = Paragraph(texto)
documento.body.append(parrafo)

# Crear una cabecera
cabecera = Header(level=1, text="Titulo 1")
documento.body.append(cabecera)

# Niveles de una cabecera
cabecera = Header(1, "Titulo 1.1")
documento.body.append(cabecera)

cabecera = Header(2, "Titulo 2")
documento.body.append(cabecera)

parrafo = Paragraph(texto)
documento.body.append(parrafo)

cabecera = Header(3, "Titulo 3")
documento.body.append(cabecera)

cabecera = Header(4, "Titulo 4")
documento.body.append(cabecera)

cabecera = Header(5, "Titulo 5")
documento.body.append(cabecera)

cabecera = Header(6, "Titulo 6")
documento.body.append(cabecera)

cabecera = Header(7, "Titulo 7")
documento.body.append(cabecera)

cabecera = Header(8, "Titulo 8")
documento.body.append(cabecera)

cabecera = Header(9, "Titulo 9")
documento.body.append(cabecera)

cabecera = Header(10, "Titulo 10")
documento.body.append(cabecera)

# Crear estilos para el documentos

## Creas los estilos
nombre_primer_estilo = "mi_primer_estilo" # Defines el nombre del estilo
estilo_1 = Style( # Creas el estilo
    family="text",
    name=nombre_primer_estilo,
    display_name=nombre_primer_estilo,
    bold=True,
    color="darkgoldenrod",
)
documento.insert_style(estilo_1) # Insertado el estilo en el documento

nombre_segundo_estilo = "mi_segundo_estilo"
estilo_2 = Style(
    family="text",
    name=nombre_segundo_estilo,
    display_name=nombre_segundo_estilo,
    italic=True,
    size="120%",
    color="lime",
)
documento.insert_style(estilo_2)

## Crear parrafo
texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Ut at egestas erat, non gravida tortor. Proin faucibus 
    odio ac arcu gravida consectetur. Donec tristique sed 
    orci eget rutrum. Suspendisse non ullamcorper nulla. 
    Quisque lectus elit, sollicitudin nec posuere eget, 
    pharetra sed ex. Vestibulum ullamcorper, libero sit amet
    scelerisque ultrices, elit leo dapibus nunc, laoreet 
    condimentum lectus risus a quam. Donec leo turpis, 
    pulvinar sed libero quis, pretium ornare dui.
"""
parrafo = Paragraph(texto)

## Insertar los estilos en el parrafo, indicando el texto a formatear
parrafo.set_span(nombre_primer_estilo, regex="dolor") # Editara el primer texto "dolor"
parrafo.set_span(nombre_primer_estilo, regex="Vestibulum ullamcorper, libero")
parrafo.set_span(nombre_segundo_estilo, regex=r"\w+ing") # Puedes indicar los textos a formatear con regex

## Agregamos el parrafo formatado al documento
documento.body.append(parrafo)

archivo = "3_Elementos_documentos.odt"
documento.save(archivo)
