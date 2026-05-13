import pytest

from src.medication_manager import GerenciadorMedicamentos


@pytest.fixture
def client(tmp_path, monkeypatch):
    from src.web import app as web_app

    arquivo_teste = tmp_path / "test_data.json"
    gerenciador_teste = GerenciadorMedicamentos(arquivo_teste)

    monkeypatch.setattr("src.web.app.gerenciador", gerenciador_teste)

    web_app.app.config["TESTING"] = True
    with web_app.app.test_client() as client:
        yield client


def test_home_deve_retornar_200(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_adicionar_medicamento_pela_web(client):
    resp = client.post(
        "/adicionar",
        data={
            "nome": "Dipirona",
            "dosagem": "500 mg",
            "horarios": "08:00,20:00",
        },
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert "Dipirona" in resp.data.decode("utf-8")


def test_adicionar_medicamento_com_dados_invalidos(client):
    resp = client.post(
        "/adicionar",
        data={
            "nome": "",
            "dosagem": "500 mg",
            "horarios": "08:00",
        },
        follow_redirects=False,
    )
    assert resp.status_code == 400
    assert "Erro" in resp.data.decode("utf-8")


def test_remover_medicamento_pela_web(client):
    from src.web.app import gerenciador

    gerenciador.adicionar_medicamento("Teste", "10 mg", ["08:00"])
    med_id = gerenciador.listar_medicamentos()[0].id

    resp = client.get(
        f"/remover/{med_id}",
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert len(gerenciador.listar_medicamentos()) == 0


def test_marcar_dose_pela_web(client):
    from src.web.app import gerenciador

    gerenciador.adicionar_medicamento("Teste", "10 mg", ["08:00", "20:00"])
    med_id = gerenciador.listar_medicamentos()[0].id

    resp = client.get(
        f"/marcar/{med_id}/08:00",
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert "08:00" in gerenciador.listar_medicamentos()[0].horarios_tomados
