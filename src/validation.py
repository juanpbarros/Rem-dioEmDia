from datetime import datetime


def validar_nome(nome: str) -> None:
    if not nome.strip():
        raise ValueError("O nome do medicamento não pode ser vazio.")


def validar_dosagem(dosagem: str) -> None:
    if not dosagem.strip():
        raise ValueError("A dosagem não pode ser vazia.")


def validar_horarios(horarios: list[str]) -> None:
    if not horarios:
        raise ValueError("É necessário informar pelo menos um horário.")

    for horario in horarios:
        try:
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            raise ValueError(f"Horário inválido: {horario}")
