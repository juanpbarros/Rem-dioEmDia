from datetime import datetime
import zoneinfo


def obter_data_hora():
    fuso = zoneinfo.ZoneInfo("America/Sao_Paulo")
    agora = datetime.now(fuso)

    return {
        "data": agora.strftime("%Y-%m-%d"),
        "hora": agora.strftime("%H:%M"),
    }
