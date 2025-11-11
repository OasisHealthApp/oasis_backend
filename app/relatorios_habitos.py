from funcoes import carregar_dados

def relatorio_quantidade():
    habitos = carregar_dados()
    print(f"\nTotal de hábitos cadastrados: {len(habitos)}\n")


def relatorio_por_titulo():
    habitos = carregar_dados()
    if not habitos:
        print("Nenhum hábito cadastrado.\n")
        return

    titulos = {}
    for h in habitos:
        title = h["titulo"].title()
        titulos[title] = titulos.get(title, 0) + 1

    print("\nHábitos por Título:")
    for title, qtd in titulos.items():
        print(f"- {title}: {qtd}")
    print()


def relatorio_por_data():
    habitos = carregar_dados()
    if not habitos:
        print("Nenhum hábito cadastrado.\n")
        return

    datas = {}
    for h in habitos:
        data = h["data_criacao"].title()
        datas[data] = datas.get(data, 0) + 1

    print("\nHábitos por Data:")
    for data, qtd in datas.items():
        print(f"- {data}: {qtd}")
    print()


def exibir_menu_relatorios():
    """Menu de relatórios para o console."""
    while True:
        print("========== RELATÓRIOS ==========")
        print("1. Total de hábitos cadastrados")
        print("2. Quantidade por título")
        print("3. Quantidade por data de criação")
        print("4. Voltar ao menu principal")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_quantidade()
        elif opcao == "2":
            relatorio_por_titulo()
        elif opcao == "3":
            relatorio_por_data()
        elif opcao == "4":
            print("↩Voltando ao menu principal...\n")
            break
        else:
            print("Opção inválida!\n")
