from dataclasses import dataclass, field
from typing import List
from uuid import uuid4


@dataclass
class Medicamento:
    nome: str
    dosagem: str
    horarios: List[str]
    id: str = field(default_factory=lambda: str(uuid4()))
    horarios_tomados: List[str] = field(default_factory=list)

    def para_dicionario(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "dosagem": self.dosagem,
            "horarios": self.horarios,
            "horarios_tomados": self.horarios_tomados,
        }

    @staticmethod
    def de_dicionario(dados: dict) -> "Medicamento":
        return Medicamento(
            id=dados.get("id") or str(uuid4()),
            nome=dados["nome"],
            dosagem=dados["dosagem"],
            horarios=dados["horarios"],
            horarios_tomados=dados.get("horarios_tomados", []),
        )