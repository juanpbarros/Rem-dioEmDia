from models import Medicamento
from storage import carregar_medicamentos, salvar_medicamentos


class GerenciadorMedicamentos:
    def __init__(self):
        self.medicamentos = carregar_medicamentos()

    def adicionar_medicamento(self, nome: str, dosagem: str, horarios: list[str]) -> None:
        if not nome.strip():
            raise ValueError("O nome do medicamento não pode ser vazio.")

        if not dosagem.strip():
            raise ValueError("A dosagem não pode ser vazia.")

        if not horarios:
            raise ValueError("É necessário informar pelo menos um horário.")

        self.medicamentos.append(Medicamento(nome=nome, dosagem=dosagem, horarios=horarios))
        salvar_medicamentos(self.medicamentos)

    def listar_medicamentos(self) -> list[Medicamento]:
        return self.medicamentos