from funcoes import carregar_dados
from habitos_crud import criar_habito, ler_todos, ler_um, atualizar_habito, excluir_habito
from relatorios_habitos import exibir_menu_relatorios  

def exibir_menu():
    habitos = carregar_dados()

    while True:
        print("========== 🎞️ MENU – GERENCIADOR DE HÁBITOS ==========")
        print("1. Cadastrar novo hábito")
        print("2. Ler todos os hábitos")
        print("3. Ler um hábito específico")
        print("4. Atualizar hábito")
        print("5. Excluir hábito")
        print("6. Relatórios")
        print("7. Sair")
        print("======================================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_habito(habitos)
        elif opcao == "2":
            ler_todos(habitos)
        elif opcao == "3":
            ler_um(habitos)
        elif opcao == "4":
            atualizar_habito(habitos)
        elif opcao == "5":
            excluir_habito(habitos)
        elif opcao == "6":
            exibir_menu_relatorios()
        elif opcao == "7":
            print("👋 Saindo... até a próxima!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")
