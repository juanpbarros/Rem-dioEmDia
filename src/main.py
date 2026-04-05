from medication_manager import GerenciadorMedicamentos


def mostrar_menu():
    print("\n=== Remédio em Dia ===")
    print("1. Cadastrar medicamento")
    print("2. Listar medicamentos")
    print("3. Marcar dose como tomada")
    print("4. Remover medicamento")
    print("5. Sair")


def tela_cadastrar_medicamento(gerenciador: GerenciadorMedicamentos):
    print("\n--- Cadastro de medicamento ---")
    nome = input("Nome do medicamento: ").strip()
    dosagem = input("Dosagem: ").strip()
    horarios_input = input("Horários (separados por vírgula, ex: 08:00,20:00): ").strip()

    horarios = [horario.strip() for horario in horarios_input.split(",") if horario.strip()]

    try:
        gerenciador.adicionar_medicamento(nome, dosagem, horarios)
        print("Medicamento cadastrado com sucesso.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def tela_listar_medicamentos(gerenciador: GerenciadorMedicamentos):
    print("\n--- Lista de medicamentos ---")
    medicamentos = gerenciador.listar_medicamentos()

    if not medicamentos:
        print("Nenhum medicamento cadastrado.")
        return

    for indice, medicamento in enumerate(medicamentos, start=1):
        print(f"{indice}. {medicamento.nome} - {medicamento.dosagem}")
        print(f"   Horários: {', '.join(medicamento.horarios)}")
        print(
            "   Doses tomadas: "
            f"{', '.join(medicamento.horarios_tomados) if medicamento.horarios_tomados else 'Nenhuma'}"
        )


def tela_marcar_dose(gerenciador: GerenciadorMedicamentos):
    print("\n--- Marcar dose como tomada ---")
    tela_listar_medicamentos(gerenciador)

    medicamentos = gerenciador.listar_medicamentos()
    if not medicamentos:
        return

    try:
        indice = int(input("Digite o número do medicamento: ").strip()) - 1
        horario = gerenciador.marcar_dose_como_tomada(indice)
        print(f"Dose das {horario} marcada como tomada.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def tela_remover_medicamento(gerenciador: GerenciadorMedicamentos):
    print("\n--- Remover medicamento ---")
    tela_listar_medicamentos(gerenciador)

    medicamentos = gerenciador.listar_medicamentos()
    if not medicamentos:
        return

    try:
        indice = int(input("Digite o número do medicamento a remover: ").strip()) - 1
        gerenciador.remover_medicamento(indice)
        print("Medicamento removido com sucesso.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def main():
    gerenciador = GerenciadorMedicamentos()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tela_cadastrar_medicamento(gerenciador)
        elif opcao == "2":
            tela_listar_medicamentos(gerenciador)
        elif opcao == "3":
            tela_marcar_dose(gerenciador)
        elif opcao == "4":
            tela_remover_medicamento(gerenciador)
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()