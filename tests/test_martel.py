from funciones.martel import multiplicacion_martel


def test_multiplicacion_martel():
    assert multiplicacion_martel(3, 5) == 15
    assert multiplicacion_martel(3, 4) == 12
    assert multiplicacion_martel(-2, 5) == -10
