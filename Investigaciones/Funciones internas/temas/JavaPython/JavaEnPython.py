# Recuerda primero instalar el entorno de Java JDK, 
# puedes utilizar el instalador que hay dentro del 
# directorio
    # https://www.java.com/es/download/
    # https://www.oracle.com/java/technologies/downloads/#java21

import subprocess

"""# Compila tu archivo Java con la gnu-crypto jar
subprocess.run(["javac", "-cp", \
                "C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\gnu-crypto.jar", \
                    "C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\JavaEnPython.java"])

# Ejecuta tu archivo Java con la gnu-crypto jar
subprocess.run(["java", "-cp", \
                "C:\\Users\\ismae\\Downloads\\EstudiosPython;C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\gnu-crypto.jar", \
                    "Librerias.SRC.JavaEnPython"])"""
"""# Compila tu archivo Java con la gnu-crypto jar
subprocess.run(["javac", "-cp", \
                "C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\gnu-crypto.jar", \
                    "C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\JavaEnPython.java"])

# Ejecuta tu archivo Java con la gnu-crypto jar
resultado = subprocess.run(["java", "-cp", \
                "C:\\Users\\ismae\\Downloads\\EstudiosPython;C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\gnu-crypto.jar", \
                    "Librerias.SRC.JavaEnPython", "hola"], capture_output=True, text=True)

print(resultado.stdout)"""

# Compila tu archivo Java con la gnu-crypto jar
subprocess.run(["javac", "-cp", \
                "C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\JavaPython\\gnu-crypto.jar", \
                    "C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\JavaPython\\JavaEnPython.java"])

# Ejecuta tu archivo Java con la gnu-crypto jar
resultado = subprocess.run(["java", "-cp", \
                "C:\\Users\\ismae\\Downloads\\EstudiosPython;C:\\Users\\ismae\\Downloads\\EstudiosPython\\Librerias\\SRC\\JavaPython\\gnu-crypto.jar", \
                    "Librerias.SRC.JavaPython.JavaEnPython", "hola"], capture_output=True, text=True)

resultado = resultado.stdout.split("\n")

if __name__ == "__main__":
    for haval in resultado:
        print(haval)