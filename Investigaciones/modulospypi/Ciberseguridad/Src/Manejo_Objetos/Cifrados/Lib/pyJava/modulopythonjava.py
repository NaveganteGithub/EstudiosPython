import subprocess

def cifradosHaval(texto: str) -> dict:
    """
    Devolvera todos los hashes de haval 
    del texto que pases por parametro
    """
    resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.cifradosHaval', texto], \
            capture_output=True, text=True)
    salida = resultado.stdout.split("\n")
    
    procesamiento = dict()
    try:
        for haval in salida:
            hash = haval.split(" ")
            procesamiento[hash[0]] = hash[1]
    except:
        pass
    
    return procesamiento

def sha3(texto: str) -> list:
    
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas', \
        'Src.pyJava.componentesJava.SHA3', texto], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado

def encriptaciones(mensaje: str, clave: str, encriptacion: str, hash: str, pad: str):
    resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.Encriptaciones', mensaje, clave, encriptacion, hash, pad], \
            capture_output=True, text=True)
        
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def desencriptaciones(mensaje_encriptado: str, clave: str, encriptacion: str, hash: str, pad: str):
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.Desencriptaciones', mensaje_encriptado, clave, encriptacion, hash, pad], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]


"""
def cifrar_twofish(texto: str, clave: str) -> str:
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.TwofishCifrar', texto, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def descifrar_twofish(texto_cifrado: str, clave: str) -> str: 
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.TwofishDescifrar', texto_cifrado, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def cifrar_DES(texto: str, clave: str) -> str:
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.DESCifrar', texto, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def descifrar_DES(texto_cifrado: str, clave: str) -> str: 
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.DESDescifrar', texto_cifrado, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def cifrar_TripleDES(texto: str, clave: str) -> str:
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.TripleDESCifrar', texto, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def descifrar_TripleDES(texto_cifrado: str, clave: str) -> str: 
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.TripleDESDescifrar', texto_cifrado, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def cifrar_TripleDES(texto: str, clave: str) -> str:
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.TripleDESCifrar', texto, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def descifrar_TripleDES(texto_cifrado: str, clave: str) -> str: 
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.TripleDESDescifrar', texto_cifrado, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def cifrar_Blowfish(texto: str, clave: str) -> str:
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.BlowfishCifrar', texto, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]

def descifrar_Blowfish(texto_cifrado: str, clave: str) -> str: 
    resultado = subprocess.run(['java', '-cp', \
        'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
        'Src.pyJava.componentesJava.BlowfishDescifrar', texto_cifrado, clave], \
        capture_output=True, text=True)
    
    resultado = resultado.stdout.split("\n")

    return resultado[0]
"""

if __name__ == "__main__":
    
    def haval_prueba():
        # Recuerda primero instalar el entorno de Java JDK, 
        # puedes utilizar el instalador que hay dentro del 
        # directorio
            # https://www.java.com/es/download/
            # https://www.oracle.com/java/technologies/downloads/#java21
        """
        Para gestionar el archivo generador de hashes Haval hay que hacerlo directamente desde aqui
        y el archivo cifradosHaval, es decir, que para hacer labores de modificacion del archivo
        java y los subprocess hay que realizarlos primero en este entorno de pruebas debajo del if
        """

        """
        Primero hay que compilar el archivo java indicando
        las dependecias y el archivo java con la ruta absoluta
        """
        '''
        Version 1
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\JavaEnPython.java"])
        Version 2
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\JavaEnPython.java"])
        '''
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\cifradosHaval.java"])

        """
        Segundo hay que abrir al archivo java, y en la primera linea justomente en la
        linea de package, declararemos la ruta no desde la raiz del proyecto, es decir,
        no desde "espadas", sino una carpeta más abajo despues de la carpeta raiz, es 
        decir, desde la carpeta "Src".

        Tercero declaramos en este subproceses dos rutas en tercer parametro,
        la ruta absoluta desde la raiz del sistema hasta la raiz del proyecto
        seria la primera, y la segunda seria la ruta absoluta desde la raiz del
        sistema hasta la libreria que es el archivo .jar
        """
        '''
        Version 1:
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\gnu-crypto.jar', \
            'Src.pyJava.JavaEnPython', 'hola'], \
            capture_output=True, text=True)
        Version 2:
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.JavaEnPython', 'hola'], \
            capture_output=True, text=True)
        '''
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.cifradosHaval', 'Hola'], \
            capture_output=True, text=True)
        # print(resultado)
        resultado = resultado.stdout.split("\n")

        for haval in resultado:
            print(haval)

    def sha3_prueba():
        subprocess.run(["javac", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\SHA3.java"])
        
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas', \
            'Src.pyJava.componentesJava.SHA3', 'Hola'], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        for sha3 in resultado:
            print(sha3)

    def Twofish_prueba():
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\TwofishCifrar.java"])
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\TwofishDescifrar.java"])
        
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.TwofishCifrar', 'I am text to be hidden away', "1234567812345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.TwofishDescifrar', resultado[0], "1234567812345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

    def DES_prueba():
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\DESCifrar.java"])
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\DESDescifrar.java"])
        
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.DESCifrar', 'I am text to be hidden away', "12345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.DESDescifrar', resultado[0], "12345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])
    
    def TripleDES_prueba():
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\TripleDESCifrar.java"])
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\TripleDESDescifrar.java"])
        
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.TripleDESCifrar', 'I am text to be hidden away', "123456781234567812345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.TripleDESDescifrar', resultado[0], "123456781234567812345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])
    
    def Blowfish_prueba():
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\BlowfishCifrar.java"])
        
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\BlowfishDescifrar.java"])
        
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.BlowfishCifrar', 'I am text to be hidden away', "123456781234567812345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.BlowfishDescifrar', resultado[0], "123456781234567812345678"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

    def encriptaciones():
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\Encriptaciones.java"])
        
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.Encriptaciones', 'I am text to be hidden away', "123456781234567812345678", "8", "6", "2"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

    def desencriptaciones():
        subprocess.run(["javac", "-cp", \
                        "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar", \
                            "C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\Desencriptaciones.java"])
        
        resultado = subprocess.run(['java', '-cp', \
            'C:\\Users\\ismae\\git\\espadas;C:\\Users\\ismae\\git\\espadas\\Src\\pyJava\\componentesJava\\lib\\gnu-crypto.jar', \
            'Src.pyJava.componentesJava.Desencriptaciones', 'BBBkkg5GAaMrahelifvf6GhwoD26fn/03Gf7vE7HA8A=', "123456781234567812345678", "8", "6", "2"], \
            capture_output=True, text=True)
        
        resultado = resultado.stdout.split("\n")

        print(resultado[0])

    # Cuando sea necesario lo descomentas, pero sino dejalo comentado
    
    haval_prueba()
    sha3_prueba()
    """
    Twofish_prueba()
    DES_prueba()
    TripleDES_prueba()
    Blowfish_prueba()
    """
    encriptaciones()
    desencriptaciones()