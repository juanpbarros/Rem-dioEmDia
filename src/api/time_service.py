import requests


def obter_data_hora():
    url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Sao_Paulo"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return {
            "data": data["date"],      # ex: 2026-05-06
            "hora": data["time"]       # ex: 14:30
        }

    except requests.exceptions.RequestException:
        raise Exception("Erro ao conectar com a API de data/hora")