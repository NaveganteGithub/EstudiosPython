from Instituciones.Harvard.module6.hello import hello



def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Ismael") == "hello, Ismael"