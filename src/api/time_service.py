import requests
from datetime import datetime
import zoneinfo


def obter_data_hora():
    try:
        response = requests.get(
            "https://timeapi.io/api/Time/current/zone?timeZone=America/Sao_Paulo",
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()
        return {
            "data": data["date"],
            "hora": data["time"],
        }
    except Exception:
        fuso = zoneinfo.ZoneInfo("America/Sao_Paulo")
        agora = datetime.now(fuso)
        return {
            "data": agora.strftime("%Y-%m-%d"),
            "hora": agora.strftime("%H:%M"),
        }
