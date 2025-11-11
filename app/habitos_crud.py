from datetime import date
from funcoes import carregar_dados, salvar_dados

def criar_habito(habitos):
    titulo = input("Título do hábito: ")
    tempo_habito = input("Tempo de prática (em minutos): ")

    habito = {
        "id": len(habitos) + 1,
        "titulo": titulo,
        "tempo": tempo_habito,
        "data_criacao": str(date.today())
    }

    habitos.append(habito)
    salvar_dados(habitos)
    print(f"Hábito '{titulo}' adicionado com sucesso!\n")


def ler_todos(habitos):

    if not habitos:
        print("Nenhum hábito cadastrado.\n")
        return

    print("\n📚 Lista de Hábitos:")
    for h in habitos:
        print(f"ID: {h['id']} | {h['titulo']} - {h['tempo']} - {h['data_criacao']}")
    print()


def ler_um(habitos):
    if not habitos:
        print("Nenhum hábito cadastrado.\n")
        return

    try:
        id_habito = int(input("Digite o ID do hábito: "))
        for h in habitos:
            if h["id"] == id_habito:
                print("\n📚 Detalhes do Hábito:")
                print(f"Data de Criação: {h['data_criacao']}")
                print(f"Título: {h['titulo']}")
                print(f"Tempo: {h['tempo']}")
                
                return
        print("Hábito não encontrado.\n")
    except ValueError: 
        print("ID inválido.\n")


def atualizar_habito(habitos):
    ler_todos(habitos)
    try:
        id_habito = int(input("Digite o ID do hábito que deseja atualizar: "))
        for h in habitos:
            if h["id"] == id_habito:
                print(f"Editando: {h['titulo']}")
                h["titulo"] = input("Novo título: ") or h["titulo"]
                h["tempo"] = input("Novo tempo (em minutos): ") or h["tempo"]
                h["data_criacao"] = input("Nova data de criação (YYYY-MM-DD): ") or h["data_criacao"]
                salvar_dados(habitos)
                print("Hábito atualizado com sucesso!\n")
                return
        print("Hábito não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")


def excluir_habito(habitos):
    ler_todos(habitos)
    try:
        id_habito = int(input("Digite o ID do hábito que deseja excluir: "))
        for h in habitos:
            if h["id"] == id_habito:
                habitos.remove(h)
                salvar_dados(habitos)
                print(f"Hábito '{h['titulo']}' removido com sucesso!\n")
                return
        print("Hábito não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")
