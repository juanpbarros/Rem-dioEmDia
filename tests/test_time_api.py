from src.api.time_service import obter_data_hora


def test_deve_obter_data_e_hora():
    resultado = obter_data_hora()

    assert "data" in resultado
    assert "hora" in resultado
    assert len(resultado["data"]) == 10
    assert len(resultado["hora"]) == 5
