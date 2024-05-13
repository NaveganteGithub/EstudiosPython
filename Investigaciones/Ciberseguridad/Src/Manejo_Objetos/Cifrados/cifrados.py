__autor__ = "Ismael Montoro Peñasco"
__copyright__ = "Copyright 2024, CipherI"
__credits__ = ["Ismael Montoro Peñasco"]

__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "Stable"
__maintainer__ = "Ismael Montoro Peñasco"
__email__ = "ismaelmontorop@protonmail.com"

import random, zlib, binascii, random, time, hashlib, crc32c, gostcrypto, rsa, pyaes
from Lib.funcionalidades.directorios import os, archivos, posicionamiento
import Lib.cifrados.whirlpool as whirlpool
import Lib.pyJava.modulopythonjava as traductor
from hashbase import *
from MD6 import MD6

class cifrados_hash():
    """
    # Cifrados Hash
    Esta clase provee de una interfaz para poder utilizar algunos 
    de los hash mas conocidos y utilizados, y otros hash que no son
    conocidos por la mayoria.

    Todos los metodos de esta clase utilizan solamente como parametro
    el mensaje que quieras cifrar, es decir, para utilizar esta clase
    solo tienes que llamar al metodo cuyo cifrado hash quieres aplicar
    y por ultimo pasarle el mensaje a cifrar.
    """
    def __init__(self) -> None:
        pass
    
    def md2(self, texto = "hello") -> str:
        return MD2().generate_hash(texto)
    
    def md4(self, texto = "hello") -> str:
        return MD4().generate_hash(texto)
    
    def md5(self, texto = "hello") -> str:
        return MD5().generate_hash(texto)
    
    def md6(self, texto = "hello", size = 256, level = 64, key = "") -> dict:
        md6 = MD6(size=size, levels=level, key=key)
        md6_hash = md6(texto)
        return {"hash": str(md6_hash), "hash_raw": md6_hash.raw()}
    
    def sha1(self, texto = "hello") -> str:
        return hashlib.sha1(texto.encode(encoding="utf-8")).hexdigest()
    
    def sha224(self, texto = "hello") -> str:
        return hashlib.sha224(texto.encode(encoding="utf-8")).hexdigest()
    
    def sha256(self, texto = "hello") -> str:
        return hashlib.sha256(texto.encode(encoding="utf-8")).hexdigest()
    
    def sha384(self, texto = "hello") -> str:
        return hashlib.sha384(texto.encode(encoding="utf-8")).hexdigest()
    
    def sha512(self, texto = "hello") -> str:
        return hashlib.sha512(texto.encode(encoding="utf-8")).hexdigest()
    
    def sha512_224(self, texto = "hello") -> str:
        return SHA512_224().generate_hash(texto)
    
    def sha512_256(self, texto = "hello") -> str:
        return SHA512_256().generate_hash(texto)
    
    def sha3(self, texto = "hello") -> dict:
        
        diccionario_hashes = dict()
        versiones = ("SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512")
        hash_sha3 = traductor.sha3(texto)

        for version in range(4):
            diccionario_hashes[versiones[version]] = hash_sha3[version]

        return diccionario_hashes

    def ripemd128(self, texto = "hello"):
        """
        Los algoritmos de ripemd sirven para trabajar con aplicaciones 
        que prefieren utilizar valores de hash muy grandes y no les es
        necesario tener un nivel de seguridad alto
        """
        return RIPEMD128().generate_hash(texto)
    
    def ripemd160(self, texto = "hello") -> str:
        """
        Los algoritmos de ripemd sirven para trabajar con aplicaciones 
        que prefieren utilizar valores de hash muy grandes y no les es
        necesario tener un nivel de seguridad alto
        """
        return RIPEMD160().generate_hash(texto)
    
    def ripemd256(self, texto = "hello") -> str:
        """
        Los algoritmos de ripemd sirven para trabajar con aplicaciones 
        que prefieren utilizar valores de hash muy grandes y no les es
        necesario tener un nivel de seguridad alto
        """
        return RIPEMD256().generate_hash(texto)
    
    def ripemd320(self, texto = "hello") -> str:
        """
        Los algoritmos de ripemd sirven para trabajar con aplicaciones 
        que prefieren utilizar valores de hash muy grandes y no les es
        necesario tener un nivel de seguridad alto
        """
        return RIPEMD320().generate_hash(texto)
    
    def whirlpool(self, texto = "hello") -> str:
        lib_whirlpool = whirlpool.new()
        lib_whirlpool.update(texto)
        return lib_whirlpool.hexdigest()
    
    def gost(self, texto = "hello", modo: int = 0) -> str:
        modos = ('streebog256', 'streebog512')
        conversion_bytes = texto.encode()
        gost_obj = gostcrypto.gosthash.new(modos[modo], data=conversion_bytes)
        gost_hash = gost_obj.hexdigest()
        return gost_hash
    
    def ghost(self, texto = "hello"):
        pass

    def crc8(self, texto = "hello") -> str:
        return CRC8().generate_hash(texto)
    
    def crc16(self, texto = "hello") -> str:
        return CRC16().generate_hash(texto)
    
    def crc32(self, texto = "hello") -> str:
        conversion_bytes = texto.encode()
        return hex(binascii.crc32(conversion_bytes))
    
    def crc32b(self, texto = "hello") -> str:
        
        crc = 0xffffffff
        data = texto.encode()

        """
        El origen de la tabla se saco de un codigo en
        C++ que se puede encontrar en este repositorio
        https://github.com/unclejimbo/Klein/blob/bf0f91161ea583d4b053ebae17b92ed57680d8a4/external/imgui/imgui.cpp
        
        Los codigos de la tabla estan en la linea 1500 
        del codigo C++ a fecha del 20/02/2024

        Luego el algoritmo fue creado por Bing IA

        https://crccalc.com/?crc=hello&method=crc32&datatype=ascii&outtype=0
        """
        table = [
            0x00000000,0x77073096,0xEE0E612C,0x990951BA,0x076DC419,0x706AF48F,0xE963A535,0x9E6495A3,0x0EDB8832,0x79DCB8A4,0xE0D5E91E,0x97D2D988,0x09B64C2B,0x7EB17CBD,0xE7B82D07,0x90BF1D91,
            0x1DB71064,0x6AB020F2,0xF3B97148,0x84BE41DE,0x1ADAD47D,0x6DDDE4EB,0xF4D4B551,0x83D385C7,0x136C9856,0x646BA8C0,0xFD62F97A,0x8A65C9EC,0x14015C4F,0x63066CD9,0xFA0F3D63,0x8D080DF5,
            0x3B6E20C8,0x4C69105E,0xD56041E4,0xA2677172,0x3C03E4D1,0x4B04D447,0xD20D85FD,0xA50AB56B,0x35B5A8FA,0x42B2986C,0xDBBBC9D6,0xACBCF940,0x32D86CE3,0x45DF5C75,0xDCD60DCF,0xABD13D59,
            0x26D930AC,0x51DE003A,0xC8D75180,0xBFD06116,0x21B4F4B5,0x56B3C423,0xCFBA9599,0xB8BDA50F,0x2802B89E,0x5F058808,0xC60CD9B2,0xB10BE924,0x2F6F7C87,0x58684C11,0xC1611DAB,0xB6662D3D,
            0x76DC4190,0x01DB7106,0x98D220BC,0xEFD5102A,0x71B18589,0x06B6B51F,0x9FBFE4A5,0xE8B8D433,0x7807C9A2,0x0F00F934,0x9609A88E,0xE10E9818,0x7F6A0DBB,0x086D3D2D,0x91646C97,0xE6635C01,
            0x6B6B51F4,0x1C6C6162,0x856530D8,0xF262004E,0x6C0695ED,0x1B01A57B,0x8208F4C1,0xF50FC457,0x65B0D9C6,0x12B7E950,0x8BBEB8EA,0xFCB9887C,0x62DD1DDF,0x15DA2D49,0x8CD37CF3,0xFBD44C65,
            0x4DB26158,0x3AB551CE,0xA3BC0074,0xD4BB30E2,0x4ADFA541,0x3DD895D7,0xA4D1C46D,0xD3D6F4FB,0x4369E96A,0x346ED9FC,0xAD678846,0xDA60B8D0,0x44042D73,0x33031DE5,0xAA0A4C5F,0xDD0D7CC9,
            0x5005713C,0x270241AA,0xBE0B1010,0xC90C2086,0x5768B525,0x206F85B3,0xB966D409,0xCE61E49F,0x5EDEF90E,0x29D9C998,0xB0D09822,0xC7D7A8B4,0x59B33D17,0x2EB40D81,0xB7BD5C3B,0xC0BA6CAD,
            0xEDB88320,0x9ABFB3B6,0x03B6E20C,0x74B1D29A,0xEAD54739,0x9DD277AF,0x04DB2615,0x73DC1683,0xE3630B12,0x94643B84,0x0D6D6A3E,0x7A6A5AA8,0xE40ECF0B,0x9309FF9D,0x0A00AE27,0x7D079EB1,
            0xF00F9344,0x8708A3D2,0x1E01F268,0x6906C2FE,0xF762575D,0x806567CB,0x196C3671,0x6E6B06E7,0xFED41B76,0x89D32BE0,0x10DA7A5A,0x67DD4ACC,0xF9B9DF6F,0x8EBEEFF9,0x17B7BE43,0x60B08ED5,
            0xD6D6A3E8,0xA1D1937E,0x38D8C2C4,0x4FDFF252,0xD1BB67F1,0xA6BC5767,0x3FB506DD,0x48B2364B,0xD80D2BDA,0xAF0A1B4C,0x36034AF6,0x41047A60,0xDF60EFC3,0xA867DF55,0x316E8EEF,0x4669BE79,
            0xCB61B38C,0xBC66831A,0x256FD2A0,0x5268E236,0xCC0C7795,0xBB0B4703,0x220216B9,0x5505262F,0xC5BA3BBE,0xB2BD0B28,0x2BB45A92,0x5CB36A04,0xC2D7FFA7,0xB5D0CF31,0x2CD99E8B,0x5BDEAE1D,
            0x9B64C2B0,0xEC63F226,0x756AA39C,0x026D930A,0x9C0906A9,0xEB0E363F,0x72076785,0x05005713,0x95BF4A82,0xE2B87A14,0x7BB12BAE,0x0CB61B38,0x92D28E9B,0xE5D5BE0D,0x7CDCEFB7,0x0BDBDF21,
            0x86D3D2D4,0xF1D4E242,0x68DDB3F8,0x1FDA836E,0x81BE16CD,0xF6B9265B,0x6FB077E1,0x18B74777,0x88085AE6,0xFF0F6A70,0x66063BCA,0x11010B5C,0x8F659EFF,0xF862AE69,0x616BFFD3,0x166CCF45,
            0xA00AE278,0xD70DD2EE,0x4E048354,0x3903B3C2,0xA7672661,0xD06016F7,0x4969474D,0x3E6E77DB,0xAED16A4A,0xD9D65ADC,0x40DF0B66,0x37D83BF0,0xA9BCAE53,0xDEBB9EC5,0x47B2CF7F,0x30B5FFE9,
            0xBDBDF21C,0xCABAC28A,0x53B39330,0x24B4A3A6,0xBAD03605,0xCDD70693,0x54DE5729,0x23D967BF,0xB3667A2E,0xC4614AB8,0x5D681B02,0x2A6F2B94,0xB40BBE37,0xC30C8EA1,0x5A05DF1B,0x2D02EF8D
        ]

        for b in data:
            crc = table[(b ^ crc) & 0xff] ^ (crc >> 8)

        return hex(crc)
    
    def crc32c(self, texto = "hello") -> str:
        conversion_bytes = texto.encode()
        return hex(crc32c.crc32c(conversion_bytes))
    
    def adler32(self, texto = "hello") -> str:
        conversion_bytes = texto.encode()
        return hex(zlib.adler32(conversion_bytes))
    
    def haval(self, texto: str, version: int = 0):
        """
        Para usar esta funcion tienes que pasar el texto a cifrar y 
        el tipo de hash haval a utilizar mediante un numero entero positivo
        aqui dejo un listado de las opciones que tienes disponibles.

        Recomendacion: usa la funcion una vez, y utiliza el diccionario
        devuelto por la funcion para evitar tener que usar la funcion una
        y otra vez, asi tu programa ira mas rápido y será más eficiente, es decir,
        guarda el diccionario que tenga la funcion en una variable.
        
        Listado: 
            "ALL"           0 (Recomendado)\n
            "Haval128,3"    1\n
            "Haval160,3"    2\n
            "Haval192,3"    3\n
            "Haval224,3"    4\n
            "Haval256,3"    5\n
            "Haval128,4"    6\n
            "Haval160,4"    7\n
            "Haval192,4"    8\n
            "Haval224,4"    9\n
            "Haval256,4"    10\n
            "Haval128,5"    11\n
            "Haval160,5"    12\n
            "Haval192,5"    13\n
            "Haval224,5"    14\n
            "Haval256,5"    15
        """
        if version >= 0 and version <= 15:
            versiones = ("ALL", "Haval128,3", "Haval160,3", "Haval192,3", "Haval224,3", "Haval256,3", "Haval128,4", "Haval160,4", "Haval192,4", "Haval224,4", "Haval256,4", "Haval128,5", "Haval160,5", "Haval192,5", "Haval224,5", "Haval256,5")
            eleccion = versiones[version]
            cifrados_haval = traductor.cifradosHaval(texto)
            
            if eleccion == "ALL":
                return cifrados_haval
            
            return str(cifrados_haval[eleccion])
        
        return "Opcion no valida, introduce un número del 0 al 15, para elegir una opción."

class cifrado_aplicado():
    """
    # Cifrado Aplicado
    Esta clase provee de cifrados que no tienen una clave generada, 
    sino que son cifrados que utilizando cierta logica nos permite
    aplicar cifrado a un mensaje.
    """
    
    # https://www.youtube.com/watch?v=SLO_Tr2mHDA
    def cifrado_ROT13(self, cadena: str = "hello"):
        
        def busqueda(abecedario: tuple, letra: str):
            posicion = -1
            try:
                posicion = abecedario.index(letra)
            except:
                pass
                
            return posicion
        
        cifrado = ""
        conversion = cadena.lower()
        abecedario_1 = ("a","b","c","d","e","f","g","h","i","j","k","l","m")
        abecedario_2 = ("n","o","p","q","r","s","t","u","v","w","x","y","z")
        for caracter in conversion:
            posicion_abecedario_1 = busqueda(abecedario_1, caracter)
            posicion_abecedario_2 = busqueda(abecedario_2, caracter)
            if posicion_abecedario_1 != -1:
                cifrado += abecedario_2[posicion_abecedario_1]
            elif posicion_abecedario_2 != -1:
                cifrado += abecedario_1[posicion_abecedario_2]

        return cifrado

    def cifrado_cesar(self, texto: str, con_cambio: bool = False, clave_de_cambio: int = 7):
        # https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar
        texto_plano = texto.upper()
        texto_cifrado = ""

        if con_cambio: # Aqui tenemos el cifrado cesar con cambio
            # https://www.youtube.com/watch?v=kciDyNZblsU
            
            abecedario_original = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            abecedario_movil = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

            for _ in range(clave_de_cambio):
                abecedario_movil = abecedario_movil[1:] + abecedario_movil[0]

            for caracter in texto_plano:
                busqueda = abecedario_original.index(caracter)
                texto_cifrado += abecedario_movil[busqueda]
                abecedario_movil = abecedario_movil[1:] + abecedario_movil[0]

        else: # Este es el metodo tradicional y el más conocido
            abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" + "ABCDE"    
            
            for caracter in texto_plano:
                posicion = abecedario.index(caracter)
                resultado = posicion + 3
                texto_cifrado += abecedario[resultado]
                
        return texto_cifrado

    def descifrado_cesar(self, texto_cifrado: str, con_cambio: bool = False, clave_de_cambio: int = 7):
        # https://www.youtube.com/watch?v=kciDyNZblsU
        texto_descifrado = ""
        
        if con_cambio:
            abecedario_original = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            abecedario_movil = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            longitud_abecedario = len(abecedario_movil) - 1
            longitud_texto_cifrado = len(texto_cifrado)
            resultado = clave_de_cambio + longitud_texto_cifrado
            
            for _ in range(resultado):
                abecedario_movil = abecedario_movil[1:] + abecedario_movil[0]

            for caracter in reversed(texto_cifrado):
                abecedario_movil = abecedario_movil[longitud_abecedario] + abecedario_movil[:longitud_abecedario]
                busqueda = abecedario_movil.index(caracter)
                texto_descifrado += abecedario_original[busqueda]
            
            texto_descifrado  = "".join(list(reversed(texto_descifrado)))
        else:    
            abecedario = "VWXYZ" + "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            
            for caracter in texto_cifrado:
                posicion = abecedario.rindex(caracter)
                resultado = posicion - 3
                texto_descifrado += abecedario[resultado]
        
        return texto_descifrado
    
    def cifrado_fracmason(self, texto: str = "hello"):
        # Tupla de letras
        letras = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        )

        # Tupla de símbolos
        simbolos = (
            '⠈⠑', '⠉⠊', '⠉⠉', '⠙⠑', '⠑', '⠋⠉', '⠛⠑', '⠊⠊', '⠊', '⠚⠑',
            '⠅⠑', '⠇⠊', '⠍⠊', '⠝⠊', '⠕⠊', '⠏⠊', '⠟⠊', '⠗⠊', '⠎⠊',
            '⠞⠊', '⠥⠊', '⠧⠊', '⠺⠊', '⠭⠊', '⠽⠊', '⠵⠊'
        )

        texto_plano = texto.upper()
        texto_cifrado = ""

        if not texto_plano.isalpha():
            raise ValueError("Solo está permitido utilizar letras mayusculas y minusculas.")
        
        for caracter in texto_plano:
            resultado_busqueda = letras.index(caracter)
            texto_cifrado += simbolos[resultado_busqueda]

        return texto_cifrado

    def cifrado_atbash(self, texto: str = "hello"):
        def busqueda(abecedario: tuple, letra: str):
            posicion = -1
            try:
                posicion = abecedario.index(letra)
            except:
                pass
                
            return posicion
    
        abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        abecedario_invertido = list(reversed(abecedario))
        
        cifrado = ""
        conversion = texto.lower()
        
        for caracter in conversion:
            posicion_abecedario = busqueda(abecedario, caracter)
            if posicion_abecedario != -1:
                cifrado += abecedario_invertido[posicion_abecedario]
        
        return cifrado

    def cifrado_vigenere(self, texto: str):
        
        # https://es.wikipedia.org/wiki/Cifrado_de_Vigen%C3%A8re#Funcionamiento
        abecedario = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
                        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
                        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14,
                        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 
                        'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 
                        'Y': 25, 'Z': 26}
        abecedario_valores = list(abecedario.keys())
        
        # Nos aseguramos de que la clave tenga la misma longitud que el texto
        longitud_texto = len(texto)
        clave = ""
        for _ in range(longitud_texto):
            clave += str(random.choice(list(abecedario.keys())))
        
        texto_plano = texto.upper()
        texto_cifrado = ""
        for caracter_texto_plano, caracter_clave in zip(texto_plano, clave):
            posicion_caracter_texto = abecedario[caracter_texto_plano]
            posicion_caracter_clave = abecedario[caracter_clave]
            resultado = (posicion_caracter_texto + posicion_caracter_clave) % len(abecedario)
            texto_cifrado += abecedario_valores[resultado]
        
        return {"texto_cifrado": texto_cifrado, "clave": clave}
    
    def descifrado_vigenere(self, texto_cifrado: str, clave: str):
        
        # https://es.wikipedia.org/wiki/Cifrado_de_Vigen%C3%A8re#Funcionamiento
        abecedario = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
                        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
                        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14,
                        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 
                        'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 
                        'Y': 25, 'Z': 26}
        abecedario_valores = list(abecedario.keys())
        
        longitud_abecedario = len(abecedario)
        resultado = None
        texto_descifrado = ""

        for caracter_texto_cifrado, caracter_clave in zip(texto_cifrado, clave):
            
            posicion_texto_cifrado = abecedario[caracter_texto_cifrado]
            posicion_clave = abecedario[caracter_clave]
            
            resultado_medida = posicion_texto_cifrado - posicion_clave
            if resultado_medida >= 0:
                resultado = resultado_medida % longitud_abecedario
            elif resultado_medida < 0:
                resultado = (resultado_medida + longitud_abecedario) % longitud_abecedario

            texto_descifrado += abecedario_valores[resultado]

        return texto_descifrado

    def cifrado_hill_2_2(self, texto: str, matriz: list):
        # https://www.youtube.com/watch?v=ChOhsL-zvBo
        abecedario = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 
                      'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 
                      'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 
                      'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'None': 26}

        texto_mayusculas = texto.upper()

        # Pasamos las letras a numeros
        codificacion = list()
        for caracter in texto_mayusculas:
            codificacion.append(abecedario[caracter])

        # Nos aseguramos que el numero de longitud de la cadena sea multiplo del tamaño de la matriz
        while len(codificacion) % len(matriz[0]) != 0:
            codificacion.append(26)

        # Dividir la lista del mensaje (codificacion) en bloques, tal que la longitud de cada bloque sea igual al ancho de la fila de la matriz cuadrada
        ancho_matriz = len(matriz[0])
        codificacion = [codificacion[i:i + ancho_matriz] for i in range(0, len(codificacion), ancho_matriz)]

        # Realizamos el calculo de matrices. A Bloques de codificacion y B seria la matriz cuadrada.
        a_rows, a_cols = len(codificacion), len(codificacion[0])
        b_rows, b_cols = len(matriz), len(matriz[0])
        c = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
        
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(a_cols):
                    c[i][j] += codificacion[i][k] * matriz[k][j]
        
        # Convertirmos la matriz c en el texto cifrado
        return "".join(chr(numero) for sublist in c for numero in sublist)

    def descifrado_hill_2_2(self, texto_cifrado: str, matriz: list):
        
        def calcular_determinante(matriz):
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

        def calcular_matriz_inversa(matriz):
            det = calcular_determinante(matriz)
            if det == 0:
                raise ValueError("La matriz no es invertible (determinante igual a 0)")

            inversa = [[matriz[1][1] / det, -matriz[0][1] / det],
                    [-matriz[1][0] / det, matriz[0][0] / det]]
            return inversa
        
        caracteres_cifrado = list(texto_cifrado)
        cifrado = [ord(caracter) for caracter in caracteres_cifrado]
        
        ancho_matriz = len(matriz[0])
        codificacion = [cifrado[i:i + ancho_matriz] for i in range(0, len(cifrado), ancho_matriz)]
        
        matriz_inversa = calcular_matriz_inversa(matriz)
        
        mensaje_original = []
        for fila in codificacion:
            fila_original = [round(fila[0] * matriz_inversa[0][0] + fila[1] * matriz_inversa[1][0]),
                            round(fila[0] * matriz_inversa[0][1] + fila[1] * matriz_inversa[1][1])]
            
            if 26 in fila_original:
                fila_original.remove(26)

            mensaje_original.extend(fila_original)

        abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mensaje_descifrado = ''.join(abecedario[numero % 26] for numero in mensaje_original)
        return mensaje_descifrado

    def cifrado_hill_3_3(self, texto: str, matriz_clave: list):
        # https://es.wikipedia.org/wiki/Cifrado_Hill
        ####### Preparar el mensaje, tenemos que poner el texto en mayusculas #######
        mensaje = texto.upper()

        ####### Crear el diccionario con el alfabeto, asignando un numero a cada letra #######
        # text_abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        text_abecedario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        abecedario = dict()
        for id, caracter in enumerate(list(text_abecedario)):
            abecedario[caracter] = id

        abecedario_claves = list(abecedario.keys())
        abecedario_valores = list(abecedario.values())
        ####### Definimos el modulo con el que se trabajara, el modulo es el número de letras del abecedario #######
        modulo = len(abecedario)

        ####### Definimos el tamaño de los "bloques" #######
        bloque = 3

        ####### Definimos la matriz clave #######
        """ 
        REQUISITOS
        0º La matriz clave tiene que ser una matriz cuadrada (nxn).
        1º La matriz clave tiene que tener un determinante (K)
        distinto a cero, para que este sea invertible, 
        es decir, que podamos a partir de ella obtener 
        su matriz inversa.
        2º La matriz clave tiene que tener numeros cuyo modulo 
        sea el mismo que el modulo definido anteriormente,
        es decir, los numeros tienen que ser iguales o superiores 
        a cero y inferiores al modulo definido anteriormente.
        3º El determinante de la matriz clave tiene que ser coprimo 
        del modulo definido, para ello se busca el MCD entre el 
        determinante (a) y el modulo (b).
        NOTA:
        Sublistas (filas); posiciones (Columnas)"""
        
        ## Requisito 0 ##
        if len(matriz_clave) != len(matriz_clave[0]):
            exit(0)

        ## Requisito 1 ##
        def calcular_determinante(matriz: list):
            matriz_sarrus = matriz.copy()[0:2]
            matriz_calculo = list()
            matriz_calculo.extend(matriz)
            matriz_calculo.extend(matriz_sarrus)
            resultado_diagonales_izquierda = (matriz_calculo[0][0] * matriz_calculo[1][1] * matriz_calculo[2][2]) + (matriz_calculo[1][0] * matriz_calculo[2][1] * matriz_calculo[3][2]) + (matriz_calculo[2][0] * matriz_calculo[3][1] * matriz_calculo[4][2])
            resultado_diagonales_derecha = (matriz_calculo[0][2] * matriz_calculo[1][1] * matriz_calculo[2][0]) + (matriz_calculo[1][2] * matriz_calculo[2][1] * matriz_calculo[3][0]) + (matriz_calculo[2][2] * matriz_calculo[3][1] * matriz_calculo[4][0])
            resultado = resultado_diagonales_izquierda - (resultado_diagonales_derecha)
            return resultado

        determinante = calcular_determinante(matriz_clave)
        determinante_mod = determinante % modulo

        if determinante_mod == 0:
            exit(0)

        ## Requisito 2 ##

        for fila in matriz_clave:
            for celda in fila:
                if celda > modulo or celda < 0:
                    exit(0)

        ## Requisito 3 ##

        def es_coprimo(a, b):
            # Calculamos el MCD de los dos numeros
            while b != 0:
                a, b = b, a % b

            mcd = a # Guardaremos el resultado
            # Determinaremos si es coprimo
            return mcd == 1
        
        if not es_coprimo(determinante_mod, modulo):
            exit(0)

        ####### Codificar el mensaje a decimales #######
        mensaje_codificado = list()

        for caracter in mensaje:
            mensaje_codificado.append(abecedario[caracter])

        ####### Agrupar los digitos en bloques #######
        # Asegurarse de que el mensaje codificado se multiplo de 3 para que todos 
        # los bloques sean de 3x3 y asi cuadre con el algoritmo hill de matriz 3x3
        longitud_mensaje = len(mensaje_codificado)
        if longitud_mensaje % 3 != 0:
            for _ in range(3 + 1):
                mensaje_codificado.append(modulo - 1)
                longitud_mensaje = len(mensaje_codificado)
                if longitud_mensaje % 3 == 0: break
        
        # Después agrupar los digitos del mensaje codificado en "bloques" de 3, cada bloque tiene como nombre P
        mensaje_en_bloques = list()
        bloque = list()

        for decimal in mensaje_codificado:
            bloque.append(decimal)
            if len(bloque) == 3:
                mensaje_en_bloques.append(bloque)
                bloque = list()

        ####### Realizar el calculo de matrices para el cifrado #######
        cifrado = ""
        for bloque in mensaje_en_bloques: 
            for claves in matriz_clave:
                resultado_P1 = bloque[0] * claves[0]
                resultado_P2 = bloque[1] * claves[1]
                resultado_P3 = bloque[2] * claves[2]
                resultado_suma = sum([resultado_P1, resultado_P2, resultado_P3])
                resultado_modulo = resultado_suma % modulo
                cifrado += abecedario_claves[resultado_modulo]
                
        return cifrado

    def descifrado_hill_3_3(self, texto_cifrado: str, matriz_clave: list):
        # Necesitaremos todos los recursos utilizados para el cifrado
        text_abecedario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        abecedario_descifrado = dict()
        for id, caracter in enumerate(list(text_abecedario)):
            abecedario_descifrado[caracter] = id

        abecedario_claves_descifrado = list(abecedario_descifrado.keys())
        abecedario_valores_descifrado = list(abecedario_descifrado.values())
        
        modulo_descifrado = len(abecedario_descifrado)
        
        matriz_clave_descifrado = matriz_clave.copy()

        ####### Hallar la matriz transpuesta #######

        bloque = list()
        matriz_transpuesta = list()
        posicion = 0
        for id, columna in enumerate(matriz_clave_descifrado * 3):
            bloque.append(columna[posicion])
            if (id + 1) % 3 == 0:
                matriz_transpuesta.append(bloque)
                posicion += 1
                bloque = list()
        
        if len(matriz_clave) != len(matriz_clave[0]):
            exit(0)

        def matriz_adjunta(matriz: list):
            result_posicion_1_1 = (matriz[1][1] * matriz[2][2]) - (matriz[2][1] * matriz[1][2])
            result_posicion_1_2 = -1 * ((matriz[1][0] * matriz[2][2]) - (matriz[2][0] * matriz[1][2]))
            result_posicion_1_3 = (matriz[1][0] * matriz[2][1]) - (matriz[2][0] * matriz[1][1])
            result_posicion_2_1 = -1 * ((matriz[0][1] * matriz[2][2]) - (matriz[2][1] * matriz[0][2]))
            result_posicion_2_2 = (matriz[0][0] * matriz[2][2]) - (matriz[2][0] * matriz[0][2])
            result_posicion_2_3 = -1 * ((matriz[0][0] * matriz[2][1]) - (matriz[2][0] * matriz[0][1]))
            result_posicion_3_1 = (matriz[0][1] * matriz[1][2]) - (matriz[1][1] * matriz[0][2])
            result_posicion_3_2 = -1 * ((matriz[0][0] * matriz[1][2]) - (matriz[1][0] * matriz[0][2]))
            result_posicion_3_3 = (matriz[0][0] * matriz[1][1]) - (matriz[1][0] * matriz[0][1])
            
            resultado = [[result_posicion_1_1, result_posicion_2_1, result_posicion_3_1], 
                        [result_posicion_1_2, result_posicion_2_2, result_posicion_3_2], 
                        [result_posicion_1_3, result_posicion_2_3, result_posicion_3_3]]
            return resultado

        matriz_adjunta_descifrado = matriz_adjunta(matriz_clave_descifrado)

        def calcular_determinante(matriz: list):
            matriz_sarrus = matriz.copy()[0:2]
            matriz_calculo = list()
            matriz_calculo.extend(matriz)
            matriz_calculo.extend(matriz_sarrus)
            resultado_diagonales_izquierda = (matriz_calculo[0][0] * matriz_calculo[1][1] * matriz_calculo[2][2]) + (matriz_calculo[1][0] * matriz_calculo[2][1] * matriz_calculo[3][2]) + (matriz_calculo[2][0] * matriz_calculo[3][1] * matriz_calculo[4][2])
            resultado_diagonales_derecha = (matriz_calculo[0][2] * matriz_calculo[1][1] * matriz_calculo[2][0]) + (matriz_calculo[1][2] * matriz_calculo[2][1] * matriz_calculo[3][0]) + (matriz_calculo[2][2] * matriz_calculo[3][1] * matriz_calculo[4][0])
            resultado = resultado_diagonales_izquierda - (resultado_diagonales_derecha)
            return resultado

        determinante = calcular_determinante(matriz_clave)

        determinante_descifrado = determinante

        ##### Hallamos el equivalente modular en modulo (modulo) de la matriz inversa #####

        ## Hallar el modulo del determinante, es decir hacer la operacion de mod al determinante por el modulo especificado anteriormente ##

        resultado_determinante_mod = determinante_descifrado % modulo_descifrado

        ## Encontraremos el inverso modular multiplicativo ##
        def inverso_modular(a, m):
            
            def euclides_extendido(a, b):
                if a == 0:
                    return b, 0, 1
                else:
                    mcd, x, y = euclides_extendido(b % a, a)
                    return mcd, y - (b // a) * x, x
            
            mcd, x, y = euclides_extendido(a, m)
            if mcd != 1:
                raise ValueError(f"No existe inverso modular para {a} módulo {m}")
            else:
                return x % m
            
        inverso_modular_resultado = inverso_modular(resultado_determinante_mod, modulo_descifrado)

        if ((inverso_modular_resultado * resultado_determinante_mod) % modulo_descifrado) != 1:
            exit(0)

        ## Crear matriz inversa, recuerda que el resultado de este calculo tiene que ser igual o inferior a la variable modulo (numero de letras del abecedarios) ##

        matriz_inversa = list()
        bloque = list()
        for fila in matriz_adjunta_descifrado:
            bloque.append([(fila[0] * inverso_modular_resultado) % modulo_descifrado, (-1855 * inverso_modular_resultado) % modulo_descifrado][0])
            bloque.append([(fila[1] * inverso_modular_resultado) % modulo_descifrado, (-1855 * inverso_modular_resultado) % modulo_descifrado][0])
            bloque.append([(fila[2] * inverso_modular_resultado) % modulo_descifrado, (-1855 * inverso_modular_resultado) % modulo_descifrado][0])
            matriz_inversa.append(bloque)
            bloque = list()

        ##### Dividiremos el texto cifrado en bloques de 3 #####

        texto_cifrado_bloques = list()
        bloque = list()
        for id, caracter in enumerate(texto_cifrado):
            bloque.append(abecedario_descifrado[caracter])
            if (id + 1) % 3 == 0:
                texto_cifrado_bloques.append(bloque)
                bloque = list()

        ##### Descifrar el texto cifrado #####

        texto_descifrado = ""
        for bloque in texto_cifrado_bloques:
            for fila in matriz_inversa:
                resultado_P1 = bloque[0] * fila[0]
                resultado_P2 = bloque[1] * fila[1]
                resultado_P3 = bloque[2] * fila[2]
                resultado_suma = sum([resultado_P1, resultado_P2, resultado_P3])
                resultado_modulo = resultado_suma % modulo_descifrado
                texto_descifrado += abecedario_claves_descifrado[resultado_modulo]

        return texto_descifrado

    def cifrado_mob_of_the_dead(self):
        # https://www.youtube.com/watch?v=P_nL1aJjgBQ
        pass

    def cifrado_polibio(self, texto: str):
        # https://www.youtube.com/watch?v=kblUbwG4xOA
        # https://museo.inf.upv.es/blog/2021/05/14/cifrado-de-polibio/

        abecedario = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 
              'F': 21, 'G': 22, 'H': 23, 'I': 24, 'J': 24, 
              'K': 25, 'L': 31, 'M': 32, 'N': 33, 'O': 34, 
              'P': 35, 'Q': 41, 'R': 42, 'S': 43, 'T': 44, 
              'U': 45, 'V': 51, 'W': 52, 'X': 53, 'Y': 54, 
              'Z': 55}

        texto_cifrado = ""
        texto_plano = texto.upper()
        for caracter in texto_plano:
            texto_cifrado += str(abecedario[caracter])
        return texto_cifrado

    def descifrar_polibio(texto_cifrado: str):
        # https://es.wikipedia.org/wiki/Cuadrado_de_Polibio
        abecedario = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 
                    'F': 21, 'G': 22, 'H': 23, 'I': 24, 'J': 24, 
                    'K': 25, 'L': 31, 'M': 32, 'N': 33, 'O': 34, 
                    'P': 35, 'Q': 41, 'R': 42, 'S': 43, 'T': 44, 
                    'U': 45, 'V': 51, 'W': 52, 'X': 53, 'Y': 54, 
                    'Z': 55}
        abecedario_clave  = list(abecedario.keys())
        abecedario_valores = list(abecedario.values())
        texto_descifrado = ""
        
        for i in range(0, len(texto_cifrado), 2):
            posicion = texto_cifrado[i] + texto_cifrado[i+1]
            posicion = int(posicion)
            posicion_letra = abecedario_valores.index(posicion)
            texto_descifrado += abecedario_clave[posicion_letra]
            
        return texto_descifrado
    
    def cifrado_alberti(self, texto: str, clave: int, rotacion: str = "derecha"):
        """
        Este cifrado fue creado por Leon Battista Alberti creador del criptoanalisis
        sustitucion poli alfabetica. Tradicionalmente este cifrado se hace con un
        mecanismo de dos discos un disco fijo y otro movil, se ajusta el movil para
        que coincida sus caracteres con los caracteres del disco fijo, 
        posicionando el disco movil como queramos.

            https://www.youtube.com/watch?v=k1Dq0c1CzQw
            https://www.youtube.com/watch?app=desktop&v=JTm-bTK5TiE
        """
        rueda_fija = "DX1CGKB8M4RFUIY2L6ÑSHQ5W7EV9NJPZT3AO"
        rueda_movil = "yqva!x0jt@$gzw&eoph%ñdr=cs?m#nfkulib"
        numero_letras = len(rueda_movil)
        resultado = ""

        comparacion = rotacion.lower()
        if comparacion == "derecha":
            for _ in range(clave):
                ultima_letra = rueda_movil[numero_letras - 1]
                sub_cadena = rueda_movil[:numero_letras - 1]
                rueda_movil = ultima_letra + sub_cadena
        elif comparacion == "izquierda":
            for _ in range(clave):
                primera_letra = rueda_movil[0]
                sub_cadena = rueda_movil[1:]
                rueda_movil = sub_cadena + primera_letra

        for caracter in texto.upper():
            posicion = rueda_fija.index(caracter)
            resultado += rueda_movil[posicion]

        return resultado

class cifrado_sincrono():
    """
    NOTA: para la instalacion ejecuta esta clase varias 
    veces hasta que se genere la cache, porque falla las 
    primeras veces, supongo yo que porque realiza operaciones
    matematicas demasido grandes.
    """

    class cifrar_DES():
        
        def __init__(self) -> None:
            pass

        def cifrar(self, texto: str = "hello", clave: str = "12345678") -> str:
            return traductor.encriptaciones(texto, clave, "3", "6", "2")
            # return traductor.cifrar_DES(texto, clave)

        def descifrar(self, texto_cifrado: str, clave: int) -> str:
            return traductor.desencriptaciones(texto_cifrado, clave, "3", "6", "2")
            # return traductor.descifrar_DES(texto_cifrado, clave)

    class cifrar_3DES():
        
        def __init__(self) -> None:
            pass

        def cifrar(self, texto: str = "hello", clave: str = "123456781234567812345678") -> str:
            return traductor.encriptaciones(texto, clave, "8", "6", "2")
            # return traductor.cifrar_TripleDES(texto, str(clave))

        def descifrar(self, texto_cifrado: str, clave: int) -> str:
            return traductor.desencriptaciones(texto_cifrado, clave, "8", "6", "2")
            # return traductor.descifrar_TripleDES(texto_cifrado, str(clave))
        
    class cifrar_AES():

        def __init__(self, modo: int = 0) -> None:
            """
            # Modos de longitud para AES
            Una clave de 128 bit (16 byte)
            Una clave de 192 bit (24 byte)
            Una clave de 256 bit (32 byte)
            """
            modos = (16, 24, 32)

            if modo > 2 or modo < 0:
                raise IndexError
            
            self.key = os.urandom(modos[modo])
            self.initial_value = random.randint(1, 10000000)
        
        def get_key(self):
            return self.key

        def get_initial_value(self):
            return self.initial_value
        
        def encriptar(self, texto: str = "hello") -> bytes:
            counter = pyaes.Counter(initial_value = self.initial_value) # To use a custom initial value
            aes = pyaes.AESModeOfOperationCTR(self.key, counter = counter)
            ciphertext = aes.encrypt(texto.encode())
            return ciphertext
        
        def desencriptar(self, texto_cifrado: bytes, clave: bytes, inicial_Counter: int) -> str:
            # The counter mode of operation maintains state, so decryption requires
            # a new instance be created
            counter = pyaes.Counter(initial_value = inicial_Counter)
            aes = pyaes.AESModeOfOperationCTR(clave, counter = counter)
            decrypted = aes.decrypt(texto_cifrado)
            return decrypted
        
    class cifrar_Blowfish():

        def __init__(self) -> None:
            pass

        def cifrar(self, texto: str, clave: str) -> str:
            return traductor.encriptaciones(texto, clave, "1", "6", "2")
            # return traductor.cifrar_Blowfish(texto, str(clave))

        def descifrar(self, texto_cifrado: str, clave: str) -> str:
            return traductor.desencriptaciones(texto_cifrado, clave, "1", "6", "2")
            # return traductor.descifrar_Blowfish(texto_cifrado, str(clave))

    class cifrar_Twofish():
        
        def __init__(self) -> None:
            pass

        def cifrar(self, texto: str = "hello", clave: str = "1234567812345678") -> str:
            return traductor.encriptaciones(texto, clave, "9", "6", "2")
            # return traductor.cifrar_twofish(texto, str(clave))

        def descifrar(self, texto_cifrado: str, clave: int) -> str:
            return traductor.desencriptaciones(texto_cifrado, clave, "9", "6", "2")
            # return traductor.descifrar_twofish(texto_cifrado, str(clave))

    class cifrar_Serpent():
        
        def __init__(self) -> None:
            pass

        def cifrar(self, texto: str = "hello", clave: str = "1234567812345678") -> str:
            return traductor.encriptaciones(texto, clave, "6", "6", "2")
            

        def descifrar(self, texto_cifrado: str, clave: int) -> str:
            return traductor.desencriptaciones(texto_cifrado, clave, "6", "6", "2")
            
            
    class cifrar_IDEA(): # International Data Encryption Algorithm
        pass
    
    class cifrar_RC4():

        # El codigo de esta clase a sigo generado gracias a ChatGPT

        def __ksa(self, key):
            """Key Scheduling Algorithm (KSA)"""
            S = list(range(256))
            j = 0
            for i in range(256):
                j = (j + S[i] + key[i % len(key)]) % 256
                S[i], S[j] = S[j], S[i]
            return S

        def __prga(self, S, plaintext):
            """Pseudo-Random Generation Algorithm (PRGA)"""
            i = j = 0
            ciphertext = []
            for char in plaintext:
                i = (i + 1) % 256
                j = (j + S[i]) % 256
                S[i], S[j] = S[j], S[i]
                ciphertext.append(char ^ S[(S[i] + S[j]) % 256])
            return bytes(ciphertext)

        def encriptar(self, plaintext: str, key: str):
            S = self.__ksa(key.encode())
            return self.__prga(S, plaintext.encode())

        def desencriptar(self, ciphertext, key: str):
            S = self.__ksa(key.encode())
            return self.__prga(S, ciphertext)
    
    class cifrar_RC5():
        pass
    
    class cifrar_RC6():
        pass
    
    class cifrar_Threefish():
        pass
    
    """
    Lo pongo aqui porque esta basado en DES 
    https://en.wikipedia.org/wiki/MacGuffin_(cipher)#The_algorithm
    """
    class cifrar_Macguffin(): 
        pass
            
class cifrado_asincrono():
    """
    Los cifrados asincronos son aquellos encriptados en los que se generan dos claves, 
    una publica y una privada, por lo general se utilizan para enviar informacion a
    traves de internet. La clave publica debe tenerla el emisor o emisores del mensaje
    o mensajes, mientras que la clave privada debe de tener solo el receptor de los 
    mensajes que es el mismo que genera las claves publica y privada. 
    """

    class cifrado_rsa():

        def __init__(self, modo: int = 3) -> None:
            
            if modo < 0 or modo > 7: 
                raise IndexError
            
            longitud_claves = (128, 256, 384, 512, 1024, 2048, 3072, 4096)
            
            if modo > 4: 
                print("La claves a generar a partir del modo 4, pueden tardar en generarse.")

            self.claves = rsa.newkeys(longitud_claves[modo])

        def get_clave_publica(self):
            return self.claves[0]

        def get_clave_privada(self):
            return self.claves[1]
        
        def encriptar(self, texto: str, clave_publica: bytes) -> bytes:
            return rsa.encrypt(texto.encode(), clave_publica)

        def desencriptar(self, texto_encriptado: bytes, clave_privada: bytes) -> str:
            return rsa.decrypt(texto_encriptado, clave_privada)
        
    class cifrado_elgamal():
        pass

    class cifrado_Diffie_Hellman():
        pass


if __name__ == "__main__":

    ##################################### Funciones necesarias ######################################## 

    def separador():
        """
        Esta funcion que lo que hace es dormir la ejecucion del programa
        nos servira para evitar que las encriptaciones que se invocan con
        la libreria subprocess tengan un error interno de sistema.
        """
        time.sleep(7)
        print()

    ######################################## Algoritmos hash ########################################
    print("MD2")
    print("Hola -", cifrados_hash().md2("Hola"))
    print("hello -", cifrados_hash().md2("hello"))
    print()

    print("MD4")
    print("Hola -", cifrados_hash().md4("Hola"))
    print("hello -", cifrados_hash().md4("hello"))
    print()

    print("MD5")
    print("Hola -", cifrados_hash().md5("Hola"))
    print("hello -", cifrados_hash().md5("hello"))
    print()
    
    print("MD6")
    print("Hola -", cifrados_hash().md6("Hola"))
    print("hello -", cifrados_hash().md6("hello"))
    print()

    print("SHA1")
    print("Hola -", cifrados_hash().sha1("Hola"))
    print("hello -", cifrados_hash().sha1("hello"))
    print()

    print("SHA224")
    print("Hola -", cifrados_hash().sha224("Hola"))
    print("hello -", cifrados_hash().sha224("hello"))
    print()

    print("SHA256")
    print("Hola -", cifrados_hash().sha256("Hola"))
    print("hello -", cifrados_hash().sha256("hello"))
    print()

    print("SHA384")
    print("Hola -", cifrados_hash().sha384("Hola"))
    print("hello -", cifrados_hash().sha384("hello"))
    print()

    print("SHA512")
    print("Hola -", cifrados_hash().sha512("Hola"))
    print("hello -", cifrados_hash().sha512("hello"))
    print()

    print("SHA512_224")
    print("Hola -", cifrados_hash().sha512_224("Hola"))
    print("hello -", cifrados_hash().sha512_224("hello"))
    print()

    print("SHA512_256")
    print("Hola -", cifrados_hash().sha512_256("Hola"))
    print("hello -", cifrados_hash().sha512_256("hello"))
    print()
    
    print("SHA3")
    for palabra in ["Hola", "hello", "Emoción"]:
        dict_hashes_sha3 = cifrados_hash().sha3(palabra)
        conversion = dict_hashes_sha3.items()
        
        print(f"Hashes de la cadena {palabra}")
        for tipo_hash, hashes in conversion:
            print(f"\t{tipo_hash}: {hashes}")
        
        print()

    print("RIPEMD128")
    print("Hola -", cifrados_hash().ripemd128("Hola"))
    print("hello -", cifrados_hash().ripemd128("hello"))
    print()

    print("RIPEMD160")
    print("Hola -", cifrados_hash().ripemd160("Hola"))
    print("hello -", cifrados_hash().ripemd160("hello"))
    print()

    print("RIPEMD256")
    print("Hola -", cifrados_hash().ripemd256("Hola"))
    print("hello -", cifrados_hash().ripemd256("hello"))
    print()

    print("RIPEMD320")
    print("Hola -", cifrados_hash().ripemd320("Hola"))
    print("hello -", cifrados_hash().ripemd320("hello"))
    print()
    
    print("RIPEMD320")
    print("Hola -", cifrados_hash().ripemd320("Hola"))
    print("hello -", cifrados_hash().ripemd320("hello"))
    print()
    
    print("GOST32")
    print("Hola -", cifrados_hash().gost("Hola"))
    print("hello -", cifrados_hash().gost("hello"))
    print()

    print("GOST64")
    print("Hola -", cifrados_hash().gost("Hola", 1))
    print("hello -", cifrados_hash().gost("hello", 1))
    print()

    print("CRC8")
    print("Hola -", cifrados_hash().crc8("Hola"))
    print("hello -", cifrados_hash().crc8("hello"))
    print()

    print("CRC16")
    print("Hola -", cifrados_hash().crc16("Hola"))
    print("hello -", cifrados_hash().crc16("hello"))
    print()

    print("CRC32")
    print("Hola -", cifrados_hash().crc32("Hola"))
    print("hello -", cifrados_hash().crc32("hello"))
    print()
    
    print("CRC32B modo CRC-32/JAMCRC")
    print("Hola -", cifrados_hash().crc32b("Hola"))
    print("hello -", cifrados_hash().crc32b("hello"))
    print()

    print("CRC32C")
    print("Hola -", cifrados_hash().crc32c("Hola"))
    print("hello -", cifrados_hash().crc32c("hello"))
    print()

    print("ADLER32")
    print("Hola -", cifrados_hash().adler32("Hola"))
    print("hello -", cifrados_hash().adler32("hello"))
    print()

    print("Whirlpool")
    print("Hola -", cifrados_hash().whirlpool("Hola"))
    print("hello -", cifrados_hash().whirlpool("hello"))
    print("Emoción -", cifrados_hash().whirlpool("Emoción"))
    print()

    print("Haval completo")

    diccionarios = None
    for texto in ["Hola", "hello", "Emoción"]:
        
        print("Hashes de la cadena", texto)
        diccionarios = cifrados_hash().haval(texto)

        for hash in diccionarios.items():
            print("\t", hash[0] + ":", hash[1])

        print()

    print("Haval individual")
    cadena = "hello"
    cifrado = cifrados_hash().haval(cadena, 2)
    print(cadena, "-",cifrado)
    print()

    ######################################## Algoritmos de encriptacion ########################################

    cifrados_aplicados = cifrado_aplicado()

    print("Cifrado Fracmason")
    print("hello -", cifrados_aplicados.cifrado_fracmason())
    texto_cifrado = cifrados_aplicados.cifrado_fracmason("Hola")
    print("Hola -", texto_cifrado)
    # cifrados_aplicados.cifrado_fracmason("5d4as5d4")
    # cifrados_aplicados.cifrado_fracmason("%$asdasd")
    print()

    print("Cifrado Atbash")
    print("hello -", cifrados_aplicados.cifrado_atbash())
    print("Hola -", cifrados_aplicados.cifrado_atbash("Hola"))
    print()

    print("Cifrado ROT13")
    print("hello -", cifrados_aplicados.cifrado_ROT13())
    print("Hola -", cifrados_aplicados.cifrado_ROT13("Hola"))
    print()
    
    print("Cifrado Hill - Matriz 2x2")
    matriz_cuadrada_2_2 = [[12, 23], [14, 7]] # Siempre numeros menores a 26 y mayores a -1
    matriz_cuadrada_2_2 = [[21, 3], [5, 7]] # Siempre numeros menores a 26 y mayores a -1

    texto_cifrado = cifrados_aplicados.cifrado_hill_2_2("Buscar", matriz_cuadrada_2_2)
    print(f"\tCifrado de la cadena Buscar -", texto_cifrado)
    texto_descifrado = cifrados_aplicados.descifrado_hill_2_2(texto_cifrado, matriz_cuadrada_2_2)
    print(f"\tDescifrado de la cadena Buscar -", texto_descifrado)

    for palabra in ["Hola", "Hol", "Adios", "Bienvenido"]:
        texto_cifrado = cifrados_aplicados.cifrado_hill_2_2(palabra, matriz_cuadrada_2_2)
        print(f"\tCifrado de la cadena {palabra} -", texto_cifrado)
        texto_descifrado = cifrados_aplicados.descifrado_hill_2_2(texto_cifrado, matriz_cuadrada_2_2)
        print(f"\tDescifrado de la cadena {palabra} -", texto_descifrado)
    print()
    
    print("Cifrado Hill - Matriz 3x3")
    matriz_cuadrada_3_3 = [
                            [10, 4, 17], 
                            [2, 1, 25], 
                            [1, 9, 3]
                            ]

    texto_cifrado = cifrados_aplicados.cifrado_hill_3_3("Buscar", matriz_cuadrada_3_3)
    print(f"\tCifrado de la cadena Buscar -", texto_cifrado)
    texto_descifrado = cifrados_aplicados.descifrado_hill_3_3(texto_cifrado, matriz_cuadrada_3_3)
    print(f"\tDescifrado de la cadena Buscar -", texto_descifrado)
    print()

    print("Cifrado Alberti")
    cadena = "Hola"
    texto_cifrado = cifrados_aplicados.cifrado_alberti(cadena, 12, "derecha")
    print(cadena + ":derecha -", texto_cifrado)
    texto_cifrado = cifrados_aplicados.cifrado_alberti(cadena, 12, "izquierda")
    print(cadena + ":izquierda -", texto_cifrado)
    print()

    print("Cifrado Cesar")
    cadena = "Hola"
    texto_cifrado = cifrados_aplicados.cifrado_cesar(cadena)
    print(f"\tCifrado de la cadena {cadena} -", texto_cifrado)
    texto_descifrado = cifrados_aplicados.descifrado_cesar(texto_cifrado)
    print(f"\tDescifrado de la cadena {cadena} -", texto_descifrado)
    print()

    print("Cifrado Cesar con Cambio")
    cadena = "Hola"
    texto_cifrado_1 = cifrados_aplicados.cifrado_cesar(cadena, True, 2)
    print(f"\tCifrado de la cadena {cadena} -", texto_cifrado_1)
    texto_cifrado_2 = cifrados_aplicados.cifrado_cesar(cadena, True)
    print(f"\tCifrado de la cadena {cadena} -", texto_cifrado_2)
    texto_descifrado_1 = cifrados_aplicados.descifrado_cesar(texto_cifrado_1, True, 2)
    print(f"\tDescifrado de la cadena {cadena} -", texto_descifrado_1)
    texto_descifrado_2 = cifrados_aplicados.descifrado_cesar(texto_cifrado_2, True)
    print(f"\tDescifrado de la cadena {cadena} -", texto_descifrado_2)
    print()

    ######################################## Algoritmos de encriptacion SINCRONOS ########################################
    
    print("Cifrado DES")
    # Prueba 1
    # clave = "12345678"
    # Prueba 2
    # clave = "01234567"
    # Prueba 3
    # clave = random.randrange(10**7, 10**8 - 1)
    # Prueba 4
    clave = random.randrange(1, 10**8 - 1)
    clave = str(clave).zfill(8)
    
    cifrado_des = cifrado_sincrono().cifrar_DES()
    texto_cifrado = cifrado_des.cifrar("Hola", clave)
    print("Texto cifrado -", texto_cifrado)
    texto_descifrado = cifrado_des.descifrar(texto_cifrado, clave)
    print("Texto descifrado -", texto_descifrado)
    separador()
    
    print("Cifrado TripleDES")
    # Prueba 1
    # clave = "123456781234567812345678"
    # Prueba 2
    # clave = "012345670123456701234567"
    # Prueba 3
    # clave = random.randrange(10**23, 10**24 - 1)
    # Prueba 4
    clave = random.randrange(1, 10**24 - 1)
    clave = str(clave).zfill(24)
    cifrado_des = cifrado_sincrono().cifrar_3DES()
    texto_cifrado = cifrado_des.cifrar("Hola", clave)
    print("Texto cifrado -", texto_cifrado)
    texto_descifrado = cifrado_des.descifrar(texto_cifrado, clave)
    print("Texto descifrado -", texto_descifrado)
    separador()

    print("Cifrado AES-128")
    cifrado_aes = cifrado_sincrono().cifrar_AES()
    texto_encriptado = cifrado_aes.encriptar()
    print("Texto cifrado con AES-128:", texto_encriptado.hex())
    texto_desencriptado = cifrado_aes.desencriptar(texto_encriptado, cifrado_aes.get_key(), cifrado_aes.get_initial_value())
    print("Texto descifrado con AES-128:", texto_desencriptado)
    print()

    print("Cifrado AES-192")
    cifrado_aes = cifrado_sincrono().cifrar_AES(1)
    texto_encriptado = cifrado_aes.encriptar()
    print("Texto cifrado con AES-192:", texto_encriptado.hex())
    texto_desencriptado = cifrado_aes.desencriptar(texto_encriptado, cifrado_aes.get_key(), cifrado_aes.get_initial_value())
    print("Texto descifrado con AES-192:", texto_desencriptado)
    print()

    print("Cifrado AES-256")
    cifrado_aes = cifrado_sincrono().cifrar_AES(2)
    texto_encriptado = cifrado_aes.encriptar()
    print("Texto cifrado con AES-256:", texto_encriptado.hex())
    texto_desencriptado = cifrado_aes.desencriptar(texto_encriptado, cifrado_aes.get_key(), cifrado_aes.get_initial_value())
    print("Texto descifrado con AES-256:", texto_desencriptado)
    print()

    print("Cifrado Blowfish")
    cifrado_blowfish = cifrado_sincrono().cifrar_Blowfish()
    # clave = "123456781234567812345678"
    # clave = "123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678123456781234567812345678"
    # clave = "012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567890123450123456789012345012345678901234501234567"
    # clave = random.randrange(10**32, 10**449 - 1)
    clave = random.randrange(1, 10**449 - 1) # Puede usar claves de esta 448 digitos
    if random.choice([True, False]):
        clave = str(clave).zfill(448)
    else:
        clave = str(clave)
    # contenido = "I am text to be hidden away"
    contenido = "Hola"

    texto_cifrado = cifrado_blowfish.cifrar(contenido, clave)
    print("Texto cifrado -", texto_cifrado)
    texto_descifrado = cifrado_blowfish.descifrar(texto_cifrado, clave)
    print("Texto descifrado -", texto_descifrado)
    separador()

    print("Cifrado Twofish")
    cifrado_twofish = cifrado_sincrono().cifrar_Twofish()
    # clave = "1234567812345678"
    # clave = "0123456789012345"
    # clave = random.randrange(10**15, 10**16 - 1)
    clave = random.randrange(1, 10**16 - 1)
    clave = str(clave).zfill(16)
    # contenido = "I am text to be hidden away"
    contenido = "Hola"
    texto_cifrado = cifrado_twofish.cifrar(contenido, clave)
    print("Texto cifrado -", texto_cifrado)
    texto_descifrado = cifrado_twofish.descifrar(texto_cifrado, clave)
    print("Texto descifrado -", texto_descifrado)
    separador()

    print("Cifrado Serpent")
    clave = random.randrange(1, 10**129 - 1)
    clave = str(clave).zfill(128)
    contenido = "Hola"
    cifrado_serpent = cifrado_sincrono().cifrar_Serpent()
    texto_cifrado = cifrado_serpent.cifrar(contenido, clave)
    print("Texto cifrado -", texto_cifrado)
    texto_descifrado = cifrado_serpent.descifrar(texto_cifrado, clave)
    print("Texto descifrado -", texto_descifrado)
    separador()

    print("Cifrado RC4")
    
    cifrado_rc4 = cifrado_sincrono().cifrar_RC4()
    
    clave = "my_secret_key"
    mensaje = "Hello, RC4!"

    mensaje_cifrado = cifrado_rc4.encriptar(mensaje, clave)
    mensaje_descifrado = cifrado_rc4.desencriptar(mensaje_cifrado, clave)

    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje encriptado: {mensaje_cifrado.hex()}")
    print(f"Mensaje desencriptado: {mensaje_descifrado.decode()}")
    print()

    # print("Cifrado RC5")

    ######################################## Algoritmos de encriptacion ASINCRONOS ########################################

    print("Cifrado RSA")
    cifrado_rsa = cifrado_asincrono().cifrado_rsa()
    # cifrado_rsa = cifrado_asincrono().cifrado_rsa(-1)
    # cifrado_rsa = cifrado_asincrono().cifrado_rsa(8)
    texto_cifrado = cifrado_rsa.encriptar("Hola", cifrado_rsa.get_clave_publica())
    print(texto_cifrado)
    print(hex(int.from_bytes(texto_cifrado)))
    texto_descifrado = cifrado_rsa.desencriptar(texto_cifrado, cifrado_rsa.get_clave_privada())
    print(texto_descifrado)

    print("Clave publica: ", cifrado_rsa.get_clave_publica(), ",\nClave privada: ", cifrado_rsa.get_clave_privada(), sep="")
