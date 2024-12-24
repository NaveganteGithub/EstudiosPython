import pypdf as pdftotext
import re

capitulos = ["Mateo", "Marcos", "Lucas", "Juan", "Hechos de los apóstoles", "Romanos", 
             "1ª Corintios 1", "2ª Corintios 2", "Gálatas", "Efesios", "Filipenses", 
             "Colosenses", "1ª Tesalonicenses", "2ª Tesalonicenses", "1ª Timoteo", 
             "2º Timoteo", "Tito", "Filemon", "Hebreos", "Santiago", "1ª Pedro", 
             "2ª Pedro", "1ª Juan", "2ª Juan", "3ª Juan", "Judas", "Apocalipsis"]
cont_cap = 0
primero = True

pdf = pdftotext.PdfReader("Src\\NTBIZMAB.pdf")
num_paginas = len(pdf.pages)

with open("Src\\NTBIZMAB.txt", "w", encoding="utf-8") as file:
    for page in range(9, num_paginas):
        pagina = pdf.pages[page]
        extraccion = pagina.extract_text()
        for linea in extraccion.split("\n"):
            if re.match(r"\([0-9]+\:[0-9]+\)", linea):
                if re.match(r"\([1]\:[1]\)", linea):
                    if not primero: cont_cap += 1
                    else: primero = False
                file.write("\n" + capitulos[cont_cap] + " " + linea)
            elif re.match(r"[\u0370-\u03FF]", linea):
                file.write(linea)
