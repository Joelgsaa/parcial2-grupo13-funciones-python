from funciones.restar_saavedra import restar_saavedra

def test_restar_saavedra():
    assert restar_saavedra(10, 4) == 6
    assert restar_saavedra(5, 10) == -5
