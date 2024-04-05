import pytest
from calculator import square

'''
Cuando utilices pytest ten en cuenta que puede analizar
los resultados de los assert de cada funcion por lo que
es buena idea hacer las pruebas en funciones separadas
'''

def test_square():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_cero():
    assert square(0) == 0

def test_str():
    '''
    with es una funcion de python que sirve para ejecutar
    codigo con los recursos que se le pasen en la sintaxis
    esto puede servir para ejecutar varias funciones con
    un recurso y tambien sirve para ejecutar recursos sin
    olvidar de cerrarlos dado que una vez termine el with
    el recurso utilizado para ejecutar el codigo es cerrado
    por el with
    '''
    with pytest.raises(TypeError): # Recurso
        square("cat") # Codigo, funciones, etc ...