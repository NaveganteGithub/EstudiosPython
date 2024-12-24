import base64
import py3base92 as base92
from PIL import Image
import pickle, io

class codificacion_objetos():

    def codificar_imagenes(self, ruta: str) -> str:
        # Abre la imagen con PIL
        image_pil = Image.open(ruta)

        # Guarda la imagen en un objeto BytesIO
        buffer = io.BytesIO()
        image_pil.save(buffer, format="JPEG")

        # Codifica los bytes en base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return image_base64

    def codificar_clases(self, clase: object):
        # Serializar la instancia en bytes
        objeto_bytes = pickle.dumps(clase)
        return base64.b64encode(objeto_bytes).decode("utf-8")
    
class decodificacion_objetos():
    
    def decodificar_imagenes(self, codificacion: str, ruta_nueva_guardar_imagen: str):
        # Decodifica el base64
        decoded_bytes = base64.b64decode(codificacion)

        # Crea una nueva imagen desde los bytes decodificados
        restored_image = Image.open(io.BytesIO(decoded_bytes))

        # Guarda la imagen restaurada
        restored_image.save(ruta_nueva_guardar_imagen)
        
    def decodificar_clases(self, codificacion: str) -> object:
        
        # Decodificar el base64
        decoded_bytes = base64.b64decode(codificacion)

        # Restaurar la instancia desde los bytes decodificados
        objeto_restaurado = pickle.loads(decoded_bytes)

        return objeto_restaurado

class codificacion_datos():
    
    def codificar_binario(self, texto = "hello") -> list:
        paso_bytes = bytes(texto, "utf-8")
        mapeo = map(bin, paso_bytes)
        return list(mapeo)
        
    def codificar_decimal(self, texto = "hello") -> list:
        return [ord(caracter) for caracter in texto]
    
    def codificar_base16(self, texto = "hello") -> str:
        """
        Con esta funcion codificas 
        el texto en base hexadecimal
        """
        codificacion = texto.encode()
        paso_bytes = bytes(codificacion)
        return base64.b16encode(paso_bytes).decode("UTF-8")
    
    def codificar_base32(self, texto = "hello") -> str:
        codificacion = texto.encode()
        paso_bytes = bytes(codificacion)
        return base64.b32encode(paso_bytes).decode("UTF-8")
    
    def codificar_base45(self, texto = "hello"):
        """
        Licencia: GPL version 3
        Github: https://github.com/panfried9/base45/tree/main
        """
        ring_list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G",
            "H","I","J","K","L","M","N","O","P","Q","R", "S","T","U","V","W","X",
            "Y","Z"," ","$","%","*","+","-",".","/",":"]
        
        outchar = ""
        lenin = len(texto) 
        
        for i in range(0, lenin, 2):
            a = int.from_bytes(bytes(texto[i], 'us-ascii'),"little") 
            if i+1 < lenin: 
                b = int.from_bytes(bytes(texto[i+1], 'us-ascii'),"little")  
                ab = int( 256 * a + b ) 
                c = divmod( ab , (45*45) ) 
                de= divmod( c[1], 45)
                outchar += ring_list[de[1]] + ring_list[de[0]] + ring_list[c[0]] 
            else: 
                de = divmod( a , 45 )   
                outchar  += ring_list[de[1]] + ring_list[de[0]]   
        
        return outchar
    
    def codificar_base58(self, texto = "hello"):
        data = texto.encode()

        # Caracteres válidos en Base58
        base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        
        # Convertir los datos binarios a un número entero
        num = int.from_bytes(data, byteorder="big")
        
        # Inicializar la cadena de salida
        encoded = ""
        
        # Realizar la codificación
        while num > 0:
            num, rem = divmod(num, 58)
            encoded = base58_chars[rem] + encoded
        
        # Agregar los caracteres '1' al principio para representar ceros iniciales
        for byte in data:
            if byte == 0:
                encoded = "1" + encoded
            else:
                break
        
        return encoded

    def codificar_base62(self, texto = "hello"):
        BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Convierte el texto en una cadena de bytes
        text_bytes = texto.encode("utf-8")
        
        # Convierte los bytes en un número entero
        num = int.from_bytes(text_bytes, byteorder="big")
        
        # Codifica el número en base62
        s = ""
        while num > 0:
            num, r = divmod(num, 62)
            s = BASE62[r] + s
        return s
    
    def codificar_base64(self, texto = "hello") -> str:
        codificacion = texto.encode()
        paso_bytes = bytes(codificacion)
        return base64.b64encode(paso_bytes).decode("UTF-8")
    
    def codificar_base85(self, texto = "hello") -> str:
        codificacion = texto.encode()
        paso_bytes = bytes(codificacion)
        return base64.b85encode(paso_bytes).decode("UTF-8")
    
    def codificar_base92(self, texto = "hello") -> str:
        codificacion = texto.encode()
        return base92.b92encode(codificacion)
    
    def codificar_a_alfablock2(self, texto = "hello") -> str:
        """
        Esta codificacion me permitira codificar texto 
        alfanumerico con metacaracteres a un formato 
        alfabetico basico en mayusculas, cada caracter
        se codificara en un bloque de 2 letras en mayusculas
        """
        abecedario = {"A": "AA", "B": "AB", "C": "AC", "D": "AD", "E": "AE", 
                      "F": "AF", "G": "AG", "H": "AH", "I": "AI", "J": "AJ", 
                      "K": "AK", "L": "AL", "M": "AM", "N": "AN", "Ñ": "AÑ", 
                      "O": "AO", "P": "AP", "Q": "AQ", "R": "AR", "S": "AS", 
                      "T": "AT", "U": "AU", "V": "AV", "W": "AW", "X": "AX", 
                      "Y": "AY", "Z": "AZ", 
                      "a": "BA", "b": "BB", "c": "BC", "d": "BD", "e": "BE", 
                      "f": "BF", "g": "BG", "h": "BH", "i": "BI", "j": "BJ", 
                      "k": "BK", "l": "BL", "m": "BM", "n": "BN", "ñ": "BÑ", 
                      "o": "BO", "p": "BP", "q": "BQ", "r": "BR", "s": "BS", 
                      "t": "BT", "u": "BU", "v": "BV", "w": "BW", "x": "BX", 
                      "y": "BY", "z": "BZ",
                      "0": "CA", "1": "CB", "2": "CC", "3": "CD", "4": "CE", 
                      "5": "CF", "6": "CG", "7": "CH", "8": "CI", "9": "CJ",
                      " ": "CK", "=": "CL", "!": "CM", "\"": "CN", "'": "CÑ", 
                      "$": "CO", "€": "CP", "%": "CQ", "/": "CR", "&": "CS", 
                      "(": "CT", ")": "CU", "·": "CV", "-": "CW", "_": "CX", 
                      ";": "CY", ":": "CZ"
                      }
        texto_codificado = ""
        for letra in texto:
            texto_codificado += abecedario[letra]

        return texto_codificado
    
    def codificar_a_alfablock3(self, texto = "hello"):
        """
        Esta es una extension de alfablock2 con la diferencia de 
        que aqui se utiliza la tabla unicode y para cada caracter
        de la tabla ascii se utiliza un bloque de codificacion
        de 3 letras alfabeticas mayusculas
        """
        import abecedario_ascii

        texto_codificado = ""
        for letra in texto:
            decimal = ord(letra)
            texto_codificado += abecedario_ascii.diccionario_ascii[decimal]

        del abecedario_ascii
        return texto_codificado
    
    def codificar_a_alfablock5(self, texto = "hello"):
        """
        Esta es una extension de alfablock2 con la diferencia de 
        que aqui se utiliza la tabla unicode y para cada caracter
        de la tabla unicode se utiliza un bloque de codificacion
        de 5 letras alfabeticas mayusculas
        """
        import abecedario_unicode

        texto_codificado = ""
        for letra in texto:
            decimal = ord(letra)
            texto_codificado += abecedario_unicode.diccionario_unicode[decimal]

        del abecedario_unicode
        return texto_codificado

class decodificacion_datos():

    def decodificar_binario(self, binario: list) -> str:
        conversion = [chr(int(byte, 2)) for byte in binario]
        return "".join(conversion)
        
    def decodificar_decimal(self, decimales: list) -> str:
        return "".join([chr(caracter) for caracter in decimales])
    
    def decodificar_base16(self, hexadecimal: str) -> str:
        codificacion = hexadecimal.encode()
        paso_bytes = bytes(codificacion)
        return base64.b16decode(paso_bytes).decode("UTF-8")
    
    def decodificar_base32(self, codificacion: str) -> str:
        codificacion = codificacion.encode()
        paso_bytes = bytes(codificacion)
        return base64.b32decode(paso_bytes).decode("UTF-8")
    
    def decodificar_base45(self, codificacion: bytes) -> str:
        """
        Licencia: GPL version 3
        Github: https://github.com/panfried9/base45/tree/main
        """
        revring = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15, 
                   "G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30, 
                   "V":31,"W":32,"X":33,"Y":34,"Z":35," ":36,"$":37,"%":38,"*":39,"+":40,"-":41,".":42,"/":43,":":44 }
        
        outchar = "" 
        lenin = len(codificacion) 

        for i in range(0, lenin, 3):
            a = revring[codificacion[i]]
            
            if i+1 < lenin: 
                b = revring[codificacion[i+1]]
            else: 
                b = 0 
            
            if i+2 < lenin:
                c = revring[codificacion[i+2]]
            else: 
                c = 0 
            
            group = a + b * 45 + c * 45 * 45
            b = divmod(group, 256)
            outchar += chr(b[0]) + chr(b[1])

        return outchar 
    
    def decodificar_base58(self, codificacion: str) -> str:
        # Caracteres válidos en Base58
        base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        
        # Convertir la cadena codificada a un número entero
        num = 0
        for char in codificacion:
            num = num * 58 + base58_chars.index(char)
        
        # Convertir el número entero a datos binarios
        decoded = num.to_bytes((num.bit_length() + 7) // 8, byteorder="big")
        
        return decoded.decode()

    def decodificar_base62(self, codificacion) -> str:
        BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Decodifica la cadena base62 al número original
        x, s = 1, 0
        for i in range(len(codificacion) - 1, -1, -1):
            s = int(BASE62.index(codificacion[i])) * x + s
            x *= 62
        
        # Convierte el número en bytes
        text_bytes = s.to_bytes((s.bit_length() + 7) // 8, byteorder="big")
        
        # Decodifica los bytes al texto original
        original_text = text_bytes.decode("utf-8")
        return original_text
    
    def decodificar_base64(self, codificacion: str) -> str:
        codificacion = codificacion.encode()
        paso_bytes = bytes(codificacion)
        return base64.b64decode(paso_bytes).decode("UTF-8")
    
    def decodificar_base85(self, codificacion: str) -> str:
        codificacion = codificacion.encode()
        paso_bytes = bytes(codificacion)
        return base64.b85decode(paso_bytes).decode("UTF-8")
    
    def decodificar_base92(self, codificacion: str) -> str:
        return base92.b92decode(codificacion).decode()
    
    def decodificar_alfablock2(self, codificacion: str) -> str:
        abecedario = {"A": "AA", "B": "AB", "C": "AC", "D": "AD", "E": "AE", 
                      "F": "AF", "G": "AG", "H": "AH", "I": "AI", "J": "AJ", 
                      "K": "AK", "L": "AL", "M": "AM", "N": "AN", "Ñ": "AÑ", 
                      "O": "AO", "P": "AP", "Q": "AQ", "R": "AR", "S": "AS", 
                      "T": "AT", "U": "AU", "V": "AV", "W": "AW", "X": "AX", 
                      "Y": "AY", "Z": "AZ", 
                      "a": "BA", "b": "BB", "c": "BC", "d": "BD", "e": "BE", 
                      "f": "BF", "g": "BG", "h": "BH", "i": "BI", "j": "BJ", 
                      "k": "BK", "l": "BL", "m": "BM", "n": "BN", "ñ": "BÑ", 
                      "o": "BO", "p": "BP", "q": "BQ", "r": "BR", "s": "BS", 
                      "t": "BT", "u": "BU", "v": "BV", "w": "BW", "x": "BX", 
                      "y": "BY", "z": "BZ",
                      "0": "CA", "1": "CB", "2": "CC", "3": "CD", "4": "CE", 
                      "5": "CF", "6": "CG", "7": "CH", "8": "CI", "9": "CJ",
                      " ": "CK", "=": "CL", "!": "CM", "\"": "CN", "'": "CÑ", 
                      "$": "CO", "€": "CP", "%": "CQ", "/": "CR", "&": "CS", 
                      "(": "CT", ")": "CU", "·": "CV", "-": "CW", "_": "CX", 
                      ";": "CY", ":": "CZ"
                      }
        
        texto_decodificado = ""
        lista_letras_abecedario = tuple(abecedario.keys())
        lista_bloques_abecedario = tuple(abecedario.values())
        del abecedario

        def dividir_en_sublistas(cadena): # La subfuncion dividir_en_sublistas a sido generada con ChatGPT
            # Caso base: si la cadena está vacía o tiene una sola letra, retornamos una lista vacía
            if len(cadena) <= 1:
                return []
            # Caso recursivo: dividimos la cadena en dos partes y devolvemos una lista que contiene la primera letra y la segunda letra
            # más una llamada recursiva con el resto de la cadena
            return [list(cadena[:2])] + dividir_en_sublistas(cadena[2:])
        
        texto_codificado = dividir_en_sublistas(codificacion)

        for bloque in texto_codificado:
            bloque_actual = "".join(bloque)
            posicion_bloque = lista_bloques_abecedario.index(bloque_actual)
            texto_decodificado += lista_letras_abecedario[posicion_bloque]

        return texto_decodificado
    
    def decodificar_alfablock3(self, codificacion: str) -> str:
        import abecedario_ascii
        
        texto_decodificado = ""
        lista_abecedario_letras_decimales = tuple(abecedario_ascii.diccionario_ascii.keys())
        lista_abecedario_bloques = tuple(abecedario_ascii.diccionario_ascii.values())
        del abecedario_ascii

        def dividir_en_sublistas(cadena): # La subfuncion dividir_en_sublistas a sido generada con ChatGPT
            # Caso base: si la cadena está vacía o tiene una sola letra, retornamos una lista vacía
            if len(cadena) <= 1:
                return []
            # Caso recursivo: dividimos la cadena en dos partes y devolvemos una lista que contiene la primera letra y la segunda letra
            # más una llamada recursiva con el resto de la cadena
            return [list(cadena[:3])] + dividir_en_sublistas(cadena[3:])
        
        texto_codificado = dividir_en_sublistas(codificacion)

        for bloque in texto_codificado:
            bloque_actual = "".join(bloque)
            posicion_bloque = lista_abecedario_bloques.index(bloque_actual)
            texto_decodificado += chr(lista_abecedario_letras_decimales[posicion_bloque])

        return texto_decodificado
    
    def decodificar_alfablock5(self, codificacion: str) -> str:
        import abecedario_unicode
        
        texto_decodificado = ""
        lista_abecedario_letras_decimales = tuple(abecedario_unicode.diccionario_unicode.keys())
        lista_abecedario_bloques = tuple(abecedario_unicode.diccionario_unicode.values())
        del abecedario_unicode

        def dividir_en_sublistas(cadena): # La subfuncion dividir_en_sublistas a sido generada con ChatGPT
            # Caso base: si la cadena está vacía o tiene una sola letra, retornamos una lista vacía
            if len(cadena) <= 1:
                return []
            # Caso recursivo: dividimos la cadena en dos partes y devolvemos una lista que contiene la primera letra y la segunda letra
            # más una llamada recursiva con el resto de la cadena
            return [list(cadena[:5])] + dividir_en_sublistas(cadena[5:])
        
        texto_codificado = dividir_en_sublistas(codificacion)

        for bloque in texto_codificado:
            bloque_actual = "".join(bloque)
            posicion_bloque = lista_abecedario_bloques.index(bloque_actual)
            texto_decodificado += chr(lista_abecedario_letras_decimales[posicion_bloque])

        return texto_decodificado

if __name__ == "__main__":
    cadena = "Hola"
    codificaciones = codificacion_datos()
    codificacion_binario = codificaciones.codificar_binario(cadena)
    codificacion_decimal = codificaciones.codificar_decimal(cadena)
    codificacion_hexadecimal = codificaciones.codificar_base16(cadena)
    codificacion_base32 = codificaciones.codificar_base32(cadena)
    codificacion_base45 = codificaciones.codificar_base45(cadena)
    codificacion_base58 = codificaciones.codificar_base58(cadena)
    codificacion_base62 = codificaciones.codificar_base62(cadena)
    codificacion_base64 = codificaciones.codificar_base64(cadena)
    codificacion_base85 = codificaciones.codificar_base85(cadena)
    codificacion_base92 = codificaciones.codificar_base92(cadena)
    codificacion_alfablock2 = codificaciones.codificar_a_alfablock2(cadena)
    # codificacion_alfablock2 = codificaciones.codificar_a_alfablock2("Hola 1212$")
    codificacion_alfablock3 = codificaciones.codificar_a_alfablock3(cadena)
    codificacion_alfablock5 = codificaciones.codificar_a_alfablock5(cadena)
    print("Codificacion")
    print("Binario -", codificacion_binario)
    print("Decimal -", codificacion_decimal)
    print("Base16 o Hexadecimal -", codificacion_hexadecimal)
    print("Base32 -", codificacion_base32)
    print("Base45 -", codificacion_base45)
    print("Base58 -", codificacion_base58)
    print("Base62 -", codificacion_base62)
    print("Base64 -", codificacion_base64)
    print("Base85 -", codificacion_base85)
    print("Base92 -", codificacion_base92)
    print("Alfablock2 -", codificacion_alfablock2)
    print("Alfablock3 -", codificacion_alfablock3)
    print("Alfablock5 -", codificacion_alfablock5)
    print()

    decodificaciones = decodificacion_datos()
    decodificacion_binario = decodificaciones.decodificar_binario(codificacion_binario)
    decodificacion_decimal = decodificaciones.decodificar_decimal(codificacion_decimal)
    decodificacion_hexadecimal = decodificaciones.decodificar_base16(codificacion_hexadecimal)
    decodificacion_base32 = decodificaciones.decodificar_base32(codificacion_base32)
    decodificacion_base45 = decodificaciones.decodificar_base45(codificacion_base45)
    decodificacion_base58 = decodificaciones.decodificar_base58(codificacion_base58)
    decodificacion_base62 = decodificaciones.decodificar_base62(codificacion_base62)
    decodificacion_base64 = decodificaciones.decodificar_base64(codificacion_base64)
    decodificacion_base85 = decodificaciones.decodificar_base85(codificacion_base85)
    decodificacion_base92 = decodificaciones.decodificar_base92(codificacion_base92)
    decodificacion_alfablock2 = decodificaciones.decodificar_alfablock2(codificacion_alfablock2)
    decodificacion_alfablock3 = decodificaciones.decodificar_alfablock3(codificacion_alfablock3)
    decodificacion_alfablock5 = decodificaciones.decodificar_alfablock5(codificacion_alfablock5)
    print("Decodificacion")
    print("Binario -", decodificacion_binario)
    print("Decimal -", decodificacion_decimal)
    print("Base16 o Hexadecimal -", decodificacion_hexadecimal)
    print("Base32 -", decodificacion_base32)
    print("Base45 -", decodificacion_base45)
    print("Base58 -", decodificacion_base58)
    print("Base62 -", decodificacion_base62)
    print("Base64 -", decodificacion_base64)
    print("Base85 -", decodificacion_base85)
    print("Base92 -", decodificacion_base92)
    print("Alfablock2 -", decodificacion_alfablock2)
    print("Alfablock3 -", decodificacion_alfablock3)
    print("Alfablock5 -", decodificacion_alfablock5)
    print()

    codificaciones = codificacion_objetos()
    decodificaciones = decodificacion_objetos()
    
    class Identificar():

        def __init__(self) -> None:
            self.identificado = True
            self.hora = "05/03/2024 13:46:00"

        def get_identificado(self):
            return self.identificado
        
        def get_hora(self):
            return self.hora

    print("Codificar clase")
    mi_clase = Identificar()
    clase_codificada = codificaciones.codificar_clases(mi_clase)
    print(clase_codificada)
    clase_decodificada = decodificaciones.decodificar_clases(clase_codificada)
    print(clase_decodificada)
    print(clase_decodificada.get_identificado())
    print(clase_decodificada.get_hora())
    print()

    print("Codificar imagen")
    imagen_a_codificar = "prueba.jpg"
    imagen_codificada = "prueba_destino.jpg"
    # Aqui indicas la imagen a codificar
    imagen_base64 = codificaciones.codificar_imagenes(imagen_a_codificar)
    # print(imagen_base64) # Si utilizas este recuerda que el resultado es muy largo debido al tamaño de la imagen
    print(imagen_base64[0:550])
    # Aqui indicas el texto de la codificacion de la imagen y la ruta donde se guardara la imagen decodificada
    decodificaciones.decodificar_imagenes(imagen_base64, imagen_codificada)

