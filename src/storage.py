import json
from pathlib import Path
from typing import List

from models import Medicamento


ARQUIVO_DADOS = Path("data/medications.json")


def carregar_medicamentos(caminho_arquivo: Path = ARQUIVO_DADOS) -> List[Medicamento]:
    if not caminho_arquivo.exists():
        return []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return [Medicamento.de_dicionario(item) for item in dados]


def salvar_medicamentos(
    medicamentos: List[Medicamento], caminho_arquivo: Path = ARQUIVO_DADOS
) -> None:
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(
            [medicamento.para_dicionario() for medicamento in medicamentos],
            arquivo,
            ensure_ascii=False,
            indent=4,
        )