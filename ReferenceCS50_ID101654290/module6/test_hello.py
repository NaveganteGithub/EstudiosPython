from hello import hello

'''
Cuando utilices pytest ten en cuenta que puede analizar
los resultados de los assert de cada funcion por lo que
es buena idea hacer las pruebas en funciones separadas
'''

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Ron", "Harry"]:
        assert hello(name) == f"hello, {name}"