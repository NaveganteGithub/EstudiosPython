class TrackVariable:
    def __init__(self, value):
        self.value = value
        self.old_value = value

    def set_value(self, new_value):
        self.old_value = self.value
        self.value = new_value

    def has_changed(self):
        return self.old_value != self.value

x = TrackVariable("Palpito")

for linea in range(100):
        cambio = False

        if True:
            continue
        elif True:
            capitulo = linea.split(" ")[1].replace("\n", "")
            x.set_value(capitulo)
            cambio = x.has_changed()
            # print("C: ", capitulo)
        else:
            versiculo = linea.split(" ")[0]
            # print("V: ", versiculo)

        if capitulo and versiculo and not cambio:
            # print(capitulo, versiculo)
            lista_Fichero.append([capitulo, versiculo])