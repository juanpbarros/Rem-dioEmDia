from pathlib import Path

from src.medication_manager import GerenciadorMedicamentos


def test_deve_adicionar_medicamento_com_sucesso(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Dipirona",
        "500 mg",
        ["08:00", "20:00"],
    )

    medicamentos = gerenciador.listar_medicamentos()

    assert len(medicamentos) == 1
    assert medicamentos[0].nome == "Dipirona"
    assert medicamentos[0].dosagem == "500 mg"
    assert medicamentos[0].horarios == ["08:00", "20:00"]


def test_nao_deve_adicionar_medicamento_com_nome_vazio(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.adicionar_medicamento(
            "",
            "500 mg",
            ["08:00"],
        )

        assert False

    except ValueError as erro:
        assert str(erro) == "O nome do medicamento não pode ser vazio."


def test_nao_deve_adicionar_medicamento_sem_horarios(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.adicionar_medicamento(
            "Dipirona",
            "500 mg",
            [],
        )

        assert False

    except ValueError as erro:
        assert str(erro) == "É necessário informar pelo menos um horário."


def test_deve_listar_horarios_pendentes(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Losartana",
        "50 mg",
        ["08:00", "20:00"],
    )

    med_id = gerenciador.listar_medicamentos()[0].id

    gerenciador.marcar_dose_como_tomada(med_id, "08:00")

    horarios_pendentes = gerenciador.listar_horarios_pendentes(med_id)

    assert horarios_pendentes == ["20:00"]


def test_deve_marcar_horario_escolhido_como_tomado(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Losartana",
        "50 mg",
        ["08:00", "20:00"],
    )

    med_id = gerenciador.listar_medicamentos()[0].id

    horario_marcado = gerenciador.marcar_dose_como_tomada(med_id, "20:00")

    medicamentos = gerenciador.listar_medicamentos()

    assert horario_marcado == "20:00"
    assert medicamentos[0].horarios_tomados == ["20:00"]


def test_nao_deve_marcar_horario_que_nao_pertence_ao_medicamento(
    tmp_path: Path,
):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Losartana",
        "50 mg",
        ["08:00", "20:00"],
    )

    med_id = gerenciador.listar_medicamentos()[0].id

    try:
        gerenciador.marcar_dose_como_tomada(med_id, "12:00")

        assert False

    except ValueError as erro:
        assert (
            str(erro)
            == "Horário não pertence ao medicamento selecionado."
        )


def test_nao_deve_marcar_horario_ja_marcado(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Losartana",
        "50 mg",
        ["08:00", "20:00"],
    )

    med_id = gerenciador.listar_medicamentos()[0].id

    gerenciador.marcar_dose_como_tomada(med_id, "08:00")

    try:
        gerenciador.marcar_dose_como_tomada(med_id, "08:00")

        assert False

    except ValueError as erro:
        assert (
            str(erro)
            == "Esse horário já foi marcado como tomado."
        )


def test_deve_remover_medicamento(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Dipirona",
        "500 mg",
        ["08:00"],
    )

    med_id = gerenciador.listar_medicamentos()[0].id
    gerenciador.remover_medicamento(med_id)

    medicamentos = gerenciador.listar_medicamentos()

    assert len(medicamentos) == 0


def test_nao_deve_marcar_dose_de_medicamento_inexistente(
    tmp_path: Path,
):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.marcar_dose_como_tomada(
            "id-inexistente",
            "08:00",
        )

        assert False

    except ValueError as erro:
        assert str(erro) == "Medicamento não encontrado."


def test_nao_deve_remover_medicamento_inexistente(
    tmp_path: Path,
):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    try:
        gerenciador.remover_medicamento("id-inexistente")

        assert False

    except ValueError as erro:
        assert str(erro) == "Medicamento não encontrado."


def test_deve_listar_horarios_atrasados(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"

    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Dipirona",
        "500 mg",
        ["08:00", "20:00"],
    )

    med_id = gerenciador.listar_medicamentos()[0].id

    horarios_atrasados = gerenciador.listar_horarios_atrasados(
        med_id,
        "14:00",
    )

    assert horarios_atrasados == ["08:00"]


def test_deve_listar_medicamentos_ordenados_por_horario(tmp_path: Path):
    arquivo_teste = tmp_path / "medicamentos_teste.json"
    gerenciador = GerenciadorMedicamentos(arquivo_teste)

    gerenciador.adicionar_medicamento(
        "Remedio B",
        "10 mg",
        ["12:00"],
    )

    gerenciador.adicionar_medicamento(
        "Remedio A",
        "5 mg",
        ["08:00"],
    )

    medicamentos = gerenciador.listar_medicamentos()

    assert medicamentos[0].nome == "Remedio A"
    assert medicamentos[1].nome == "Remedio B"
