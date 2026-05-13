from src.api.time_service import obter_data_hora


def test_obter_data_hora_deve_retornar_formato_valido():
    """Teste de integracao: chama a API externa (com fallback local) e valida o formato."""
    resultado = obter_data_hora()

    assert "data" in resultado
    assert "hora" in resultado
    assert len(resultado["data"]) == 10
    assert len(resultado["hora"]) == 5
