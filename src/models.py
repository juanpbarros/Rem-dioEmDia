from dataclasses import dataclass, field
from typing import List


@dataclass
class Medicamento:
    nome: str
    dosagem: str
    horarios: List[str]
    horarios_tomados: List[str] = field(default_factory=list)

    def para_dicionario(self) -> dict:
        return {
            "nome": self.nome,
            "dosagem": self.dosagem,
            "horarios": self.horarios,
            "horarios_tomados": self.horarios_tomados,
        }

    @staticmethod
    def de_dicionario(dados: dict) -> "Medicamento":
        return Medicamento(
            nome=dados["nome"],
            dosagem=dados["dosagem"],
            horarios=dados["horarios"],
            horarios_tomados=dados.get("horarios_tomados", []),
        )