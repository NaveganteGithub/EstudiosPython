"""
Aunque no se utilice en el codigo la libreria pytest se 
debe de importar para poder usar el comando pytest
"""
import pytest
import datetime
# Si utilizas esta importacion pytest dara error, pytest no admite importaciones relativas
# from .mi_persona import Persona
from SRC.PyTest.Persona import Persona

class TestPersona:

    def test_prueba(self):
        assert 0 == 0 # No da ningun error porque la condicion es correcta
        """
        Da error porque la condicion no es correcta, 
        y si da error detiene la prueba unitaria en
        donde se sucedio dicho error
        """
        # assert 0 != 0 
        assert 2 > 0
    
    # Podemos hacer pruebas de muchos tipos
        
    def test_constructor(self): # Pruebas para ver si el constructor y sus getters funciona
        persona = Persona(nombre="Diego", edad=25)
        assert persona.dar_nombre() == "Diego"
        assert persona.dar_edad() == 25

    def test_asignacion(self): # Pruebas para ver si los setters funcionan
        persona = Persona(nombre="Diego", edad=25)
        persona.asignar_nombre("Adriana")
        persona.asignar_edad(28)

        assert persona.dar_nombre() != "Diego"
        assert persona.dar_edad() != 25

        assert persona.dar_nombre() == "Adriana"
        assert persona.dar_edad() == 28

    def test_contiene_texto(self): # Pruebas para ver si una subcadena esta dentro de una cadena
        persona = Persona(nombre="María Alejandra", edad=22)
        assert "Alejandra" in persona.dar_nombre()

    def test_anio_nacimiento(self): # Pruebas para ver si ciertos calculos son correctos
        persona = Persona(nombre="María Alejandra", edad=22)

        assert persona.calcular_anio_nacimiento(True) == datetime.datetime.now().year - 22
        assert persona.calcular_anio_nacimiento(False) == datetime.datetime.now().year - 22 + 1
        