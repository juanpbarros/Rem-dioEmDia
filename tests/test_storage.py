from pathlib import Path

from models import Medicamento
from storage import carregar_medicamentos, salvar_medicamentos


def test_deve_salvar_e_carregar_medicamentos(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos.json"

    medicamentos = [
        Medicamento(
            nome="Losartana",
            dosagem="50 mg",
            horarios=["08:00", "20:00"],
            horarios_tomados=["08:00"],
        )
    ]

    salvar_medicamentos(medicamentos, arquivo_teste)
    medicamentos_carregados = carregar_medicamentos(arquivo_teste)

    assert len(medicamentos_carregados) == 1
    assert medicamentos_carregados[0].nome == "Losartana"
    assert medicamentos_carregados[0].dosagem == "50 mg"
    assert medicamentos_carregados[0].horarios == ["08:00", "20:00"]
    assert medicamentos_carregados[0].horarios_tomados == ["08:00"]