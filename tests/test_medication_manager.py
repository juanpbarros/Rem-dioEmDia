from pathlib import Path

from medication_manager import GerenciadorMedicamentos


def test_deve_adicionar_medicamento_com_sucesso(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento("Dipirona", "500 mg", ["08:00", "20:00"])

    medicamentos = gerenciador.listar_medicamentos()
    assert len(medicamentos) == 1
    assert medicamentos[0].nome == "Dipirona"
    assert medicamentos[0].dosagem == "500 mg"
    assert medicamentos[0].horarios == ["08:00", "20:00"]


def test_nao_deve_adicionar_medicamento_com_nome_vazio(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.adicionar_medicamento("", "500 mg", ["08:00"])
        assert False
    except ValueError as erro:
        assert str(erro) == "O nome do medicamento não pode ser vazio."


def test_nao_deve_adicionar_medicamento_sem_horarios(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.adicionar_medicamento("Dipirona", "500 mg", [])
        assert False
    except ValueError as erro:
        assert str(erro) == "É necessário informar pelo menos um horário."


def test_deve_marcar_dose_como_tomada(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento("Losartana", "50 mg", ["08:00", "20:00"])
    horario_marcado = gerenciador.marcar_dose_como_tomada(0)

    medicamentos = gerenciador.listar_medicamentos()
    assert horario_marcado == "08:00"
    assert medicamentos[0].horarios_tomados == ["08:00"]


def test_deve_remover_medicamento(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento("Dipirona", "500 mg", ["08:00"])
    gerenciador.remover_medicamento(0)

    medicamentos = gerenciador.listar_medicamentos()
    assert len(medicamentos) == 0


def test_nao_deve_marcar_dose_de_medicamento_inexistente(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.marcar_dose_como_tomada(0)
        assert False
    except ValueError as erro:
        assert str(erro) == "Medicamento não encontrado."


def test_nao_deve_remover_medicamento_inexistente(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.remover_medicamento(0)
        assert False
    except ValueError as erro:
        assert str(erro) == "Medicamento não encontrado."