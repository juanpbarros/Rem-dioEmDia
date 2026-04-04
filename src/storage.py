import json
from pathlib import Path
from typing import List

from models import Medicamento


ARQUIVO_DADOS = Path("data/medications.json")


def carregar_medicamentos() -> List[Medicamento]:
    if not ARQUIVO_DADOS.exists():
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return [Medicamento.de_dicionario(item) for item in dados]


def salvar_medicamentos(medicamentos: List[Medicamento]) -> None:
    ARQUIVO_DADOS.parent.mkdir(parents=True, exist_ok=True)

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            [medicamento.para_dicionario() for medicamento in medicamentos],
            arquivo,
            ensure_ascii=False,
            indent=4,
        )