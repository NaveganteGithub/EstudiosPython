from odfdo import Document, Paragraph

documento = Document('text')

texto = "Hola mundo!"
parrafo = Paragraph(texto)
documento.body.append(parrafo)

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
documento.body.append(parrafo)

archivo = "1_Crear_documentos.odt"
documento.save(archivo)
