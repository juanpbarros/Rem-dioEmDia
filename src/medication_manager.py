from datetime import datetime
from pathlib import Path

from src.models import Medicamento
from src.storage import carregar_medicamentos, salvar_medicamentos
from src.validation import validar_nome, validar_dosagem, validar_horarios


class GerenciadorMedicamentos:
    def __init__(self, caminho_arquivo: Path | None = None):
        self.caminho_arquivo = caminho_arquivo

        if caminho_arquivo is None:
            self.medicamentos = carregar_medicamentos()
        else:
            self.medicamentos = carregar_medicamentos(caminho_arquivo)

    def _encontrar_por_id(self, id_medicamento: str) -> Medicamento:
        for med in self.medicamentos:
            if med.id == id_medicamento:
                return med
        raise ValueError("Medicamento não encontrado.")

    def adicionar_medicamento(
        self,
        nome: str,
        dosagem: str,
        horarios: list[str],
    ) -> None:
        validar_nome(nome)
        validar_dosagem(dosagem)
        validar_horarios(horarios)

        self.medicamentos.append(
            Medicamento(
                nome=nome,
                dosagem=dosagem,
                horarios=horarios,
            )
        )

        self._salvar()

    def listar_medicamentos(self) -> list[Medicamento]:
        return sorted(
            self.medicamentos,
            key=lambda m: m.horarios[0] if m.horarios else "",
        )

    def listar_horarios_pendentes(
        self,
        id_medicamento: str,
    ) -> list[str]:
        medicamento = self._encontrar_por_id(id_medicamento)

        return [
            horario
            for horario in medicamento.horarios
            if horario not in medicamento.horarios_tomados
        ]

    def listar_horarios_atrasados(
        self,
        id_medicamento: str,
        hora_atual: str,
    ) -> list[str]:
        medicamento = self._encontrar_por_id(id_medicamento)

        hora_atual_dt = datetime.strptime(hora_atual, "%H:%M")

        atrasados = []

        for horario in medicamento.horarios:
            horario_dt = datetime.strptime(horario, "%H:%M")

            if (
                horario_dt < hora_atual_dt
                and horario not in medicamento.horarios_tomados
            ):
                atrasados.append(horario)

        return atrasados

    def marcar_dose_como_tomada(
        self,
        id_medicamento: str,
        horario_escolhido: str,
    ) -> str:
        medicamento = self._encontrar_por_id(id_medicamento)

        if horario_escolhido not in medicamento.horarios:
            raise ValueError(
                "Horário não pertence ao medicamento selecionado."
            )

        if horario_escolhido in medicamento.horarios_tomados:
            raise ValueError(
                "Esse horário já foi marcado como tomado."
            )

        medicamento.horarios_tomados.append(horario_escolhido)

        self._salvar()

        return horario_escolhido

    def remover_medicamento(
        self,
        id_medicamento: str,
    ) -> None:
        medicamento = self._encontrar_por_id(id_medicamento)
        self.medicamentos.remove(medicamento)
        self._salvar()

    def _salvar(self) -> None:
        if self.caminho_arquivo is None:
            salvar_medicamentos(self.medicamentos)
        else:
            salvar_medicamentos(
                self.medicamentos,
                self.caminho_arquivo,
            )
