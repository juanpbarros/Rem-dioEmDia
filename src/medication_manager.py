from pathlib import Path

from models import Medicamento
from storage import carregar_medicamentos, salvar_medicamentos


class GerenciadorMedicamentos:
    def __init__(self, caminho_arquivo: Path | None = None):
        self.caminho_arquivo = caminho_arquivo
        if caminho_arquivo is None:
            self.medicamentos = carregar_medicamentos()
        else:
            self.medicamentos = carregar_medicamentos(caminho_arquivo)

    def adicionar_medicamento(self, nome: str, dosagem: str, horarios: list[str]) -> None:
        if not nome.strip():
            raise ValueError("O nome do medicamento não pode ser vazio.")

        if not dosagem.strip():
            raise ValueError("A dosagem não pode ser vazia.")

        if not horarios:
            raise ValueError("É necessário informar pelo menos um horário.")

        self.medicamentos.append(
            Medicamento(nome=nome, dosagem=dosagem, horarios=horarios)
        )
        self._salvar()

    def listar_medicamentos(self) -> list[Medicamento]:
        return self.medicamentos

    def marcar_dose_como_tomada(self, indice_medicamento: int) -> str:
        if indice_medicamento < 0 or indice_medicamento >= len(self.medicamentos):
            raise ValueError("Medicamento não encontrado.")

        medicamento = self.medicamentos[indice_medicamento]

        for horario in medicamento.horarios:
            if horario not in medicamento.horarios_tomados:
                medicamento.horarios_tomados.append(horario)
                self._salvar()
                return horario

        raise ValueError("Todas as doses desse medicamento já foram marcadas como tomadas.")

    def remover_medicamento(self, indice_medicamento: int) -> None:
        if indice_medicamento < 0 or indice_medicamento >= len(self.medicamentos):
            raise ValueError("Medicamento não encontrado.")

        self.medicamentos.pop(indice_medicamento)
        self._salvar()

    def _salvar(self) -> None:
        if self.caminho_arquivo is None:
            salvar_medicamentos(self.medicamentos)
        else:
            salvar_medicamentos(self.medicamentos, self.caminho_arquivo)