from unittest.mock import patch
from src.api.time_service import obter_data_hora


@patch("src.api.time_service.requests.get")
def test_deve_obter_data_e_hora(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "date": "2026-05-06",
        "time": "14:30"
    }

    resultado = obter_data_hora()

    assert resultado["data"] == "2026-05-06"
    assert resultado["hora"] == "14:30"