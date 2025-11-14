from funciones.dividir_tevez import dividir_tevez

def test_dividir():
    assert dividir_tevez(10, 2) == 5
    assert dividir_tevez(5, 0) is None
