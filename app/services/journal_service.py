import os
import json
from datetime import datetime


JOURNAL_FILE = "data/registros_diarios.json"


def carregar_registros():
    """Carrega registros diários do arquivo JSON"""
    try:
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []


def salvar_registros(registros):
    """Salva registros diários no arquivo JSON"""
    with open(JOURNAL_FILE, 'w', encoding='utf-8') as file:
        json.dump(registros, file, ensure_ascii=False, indent=4)


def gerar_id_registro(registros):
    """Gera um ID único para novo registro"""
    if not registros:
        return 1
    return max(r.get('id', 0) for r in registros) + 1


def listar_registros():
    """Retorna todos os registros"""
    return carregar_registros()


def listar_registros_por_usuario(user_id):
    """Retorna todos os registros de um usuário específico"""
    registros = carregar_registros()
    registros_usuario = [r for r in registros if r.get('user_id') == user_id]
    # Ordena por data decrescente
    registros_usuario.sort(key=lambda x: x.get('data', ''), reverse=True)
    return registros_usuario


def buscar_registro_por_id(registro_id):
    """Busca um registro específico pelo ID"""
    registros = carregar_registros()
    for registro in registros:
        if registro.get('id') == registro_id:
            return registro
    return None


def buscar_registro_por_data(user_id, data):
    """Busca registro de um usuário em uma data específica"""
    registros = carregar_registros()
    for registro in registros:
        if registro.get('user_id') == user_id and registro.get('data') == data:
            return registro
    return None


def criar_registro(conteudo, user_id, data=None):
    """Cria um novo registro diário"""
    if not conteudo or not user_id:
        return {"sucesso": False, "mensagem": "Conteúdo e ID do usuário são obrigatórios"}
    
    if not data:
        data = str(datetime.now().date())
    
    registros = carregar_registros()
    
    # Verifica se já existe registro para esta data
    registro_existente = buscar_registro_por_data(user_id, data)
    if registro_existente:
        return {"sucesso": False, "mensagem": "Já existe um registro para esta data"}
    
    novo_registro = {
        "id": gerar_id_registro(registros),
        "conteudo": conteudo,
        "data": data,
        "user_id": user_id,
        "data_criacao": str(datetime.now().isoformat())
    }
    
    registros.append(novo_registro)
    salvar_registros(registros)
    
    return {"sucesso": True, "mensagem": "Registro criado com sucesso", "registro": novo_registro}


def atualizar_registro(registro_id, conteudo=None, user_id=None):
    """Atualiza um registro existente"""
    registros = carregar_registros()
    
    for registro in registros:
        if registro.get('id') == registro_id:
            # Verifica se o usuário é o dono do registro
            if user_id and registro.get('user_id') != user_id:
                return {"sucesso": False, "mensagem": "Você não tem permissão para editar este registro"}
            
            if conteudo is not None:
                registro['conteudo'] = conteudo
                registro['data_atualizacao'] = str(datetime.now().isoformat())
            
            salvar_registros(registros)
            return {"sucesso": True, "mensagem": "Registro atualizado com sucesso", "registro": registro}
    
    return {"sucesso": False, "mensagem": "Registro não encontrado"}


def excluir_registro(registro_id, user_id=None):
    """Exclui um registro"""
    registros = carregar_registros()
    
    for i, registro in enumerate(registros):
        if registro.get('id') == registro_id:
            # Verifica se o usuário é o dono do registro
            if user_id and registro.get('user_id') != user_id:
                return {"sucesso": False, "mensagem": "Você não tem permissão para excluir este registro"}
            
            registro_removido = registros.pop(i)
            salvar_registros(registros)
            return {"sucesso": True, "mensagem": "Registro excluído com sucesso", "registro": registro_removido}
    
    return {"sucesso": False, "mensagem": "Registro não encontrado"}
