import os
import json
from datetime import datetime

CATEGORIAS_FILE = "data/categorias.json"
CATEGORIAS_USUARIO_FILE = "data/categorias_usuario.json"

def carregar_categorias():
    try:
        if os.path.exists(CATEGORIAS_FILE):
            with open(CATEGORIAS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []

def carregar_categorias_usuario():
    try:
        if os.path.exists(CATEGORIAS_USUARIO_FILE):
            with open(CATEGORIAS_USUARIO_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []

def salvar_categorias_usuario(categorias):
    with open(CATEGORIAS_USUARIO_FILE, 'w', encoding='utf-8') as file:
        json.dump(categorias, file, ensure_ascii=False, indent=4)

def gerar_id_categoria(categorias):
    if not categorias:
        return 1
    ids_numericos = [c.get('id', 0) for c in categorias if isinstance(c.get('id'), int)]
    return max(ids_numericos) + 1 if ids_numericos else 1

def listar_todas_categorias(user_id=None):
    categorias_padrao = carregar_categorias()
    categorias_usuario = carregar_categorias_usuario()
    
    if user_id:
        categorias_usuario_filtradas = [c for c in categorias_usuario if c.get('user_id') == user_id]
        return categorias_padrao + categorias_usuario_filtradas
    
    return categorias_padrao

def buscar_categoria_por_id(categoria_id):
    categorias_padrao = carregar_categorias()
    for cat in categorias_padrao:
        if cat.get('id') == categoria_id:
            return cat
    
    categorias_usuario = carregar_categorias_usuario()
    for cat in categorias_usuario:
        if cat.get('id') == categoria_id:
            return cat
    
    return None

def criar_categoria_usuario(nome, emoji, descricao, cor, user_id):
    if not nome or not user_id:
        return {"sucesso": False, "mensagem": "Nome e ID do usuário são obrigatórios"}
    
    categorias_usuario = carregar_categorias_usuario()
    
    nova_categoria = {
        "id": gerar_id_categoria(categorias_usuario),
        "nome": nome,
        "emoji": emoji or "📌",
        "descricao": descricao or "",
        "cor": cor or "#A8DADC",
        "user_id": user_id,
        "data_criacao": str(datetime.now().date())
    }
    
    categorias_usuario.append(nova_categoria)
    salvar_categorias_usuario(categorias_usuario)
    
    return {"sucesso": True, "mensagem": "Categoria criada com sucesso", "categoria": nova_categoria}

def atualizar_categoria_usuario(categoria_id, nome=None, emoji=None, descricao=None, cor=None, user_id=None):
    categorias_usuario = carregar_categorias_usuario()
    
    for categoria in categorias_usuario:
        if categoria.get('id') == categoria_id:
            if user_id and categoria.get('user_id') != user_id:
                return {"sucesso": False, "mensagem": "Você não tem permissão para editar esta categoria"}
            
            if nome is not None:
                categoria['nome'] = nome
            if emoji is not None:
                categoria['emoji'] = emoji
            if descricao is not None:
                categoria['descricao'] = descricao
            if cor is not None:
                categoria['cor'] = cor
            
            salvar_categorias_usuario(categorias_usuario)
            return {"sucesso": True, "mensagem": "Categoria atualizada com sucesso", "categoria": categoria}
    
    return {"sucesso": False, "mensagem": "Categoria não encontrada"}

def excluir_categoria_usuario(categoria_id, user_id):
    categorias_usuario = carregar_categorias_usuario()
    
    for i, categoria in enumerate(categorias_usuario):
        if categoria.get('id') == categoria_id:
            if categoria.get('user_id') != user_id:
                return {"sucesso": False, "mensagem": "Você não tem permissão para excluir esta categoria"}
            
            categoria_removida = categorias_usuario.pop(i)
            salvar_categorias_usuario(categorias_usuario)
            return {"sucesso": True, "mensagem": "Categoria excluída com sucesso", "categoria": categoria_removida}
    
    return {"sucesso": False, "mensagem": "Categoria não encontrada"}

def listar_categorias_usuario_por_id(user_id):
    categorias_usuario = carregar_categorias_usuario()
    return [c for c in categorias_usuario if c.get('user_id') == user_id]
