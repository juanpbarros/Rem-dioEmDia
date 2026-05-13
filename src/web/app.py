from flask import Flask, render_template, request, redirect, url_for

from src.api.time_service import obter_data_hora
from src.medication_manager import GerenciadorMedicamentos

app = Flask(__name__)

gerenciador = GerenciadorMedicamentos()


@app.route("/")
def home():
    medicamentos = gerenciador.listar_medicamentos()

    try:
        info = obter_data_hora()
    except Exception:
        info = None

    return render_template(
        "index.html",
        medicamentos=medicamentos,
        info=info,
        gerenciador=gerenciador,
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    dosagem = request.form["dosagem"]

    horarios = [
        horario.strip()
        for horario in request.form["horarios"].split(",")
        if horario.strip()
    ]

    try:
        gerenciador.adicionar_medicamento(nome, dosagem, horarios)
    except ValueError as erro:
        return f"Erro: {erro}", 400

    return redirect(url_for("home"))


@app.route("/remover/<id>")
def remover(id):
    try:
        gerenciador.remover_medicamento(id)
    except ValueError as erro:
        return f"Erro: {erro}", 400

    return redirect(url_for("home"))


@app.route("/marcar/<id>/<horario>")
def marcar(id, horario):
    try:
        gerenciador.marcar_dose_como_tomada(id, horario)
    except ValueError as erro:
        return f"Erro: {erro}", 400

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
