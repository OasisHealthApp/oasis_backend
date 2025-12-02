import os
import json
import jwt
import bcrypt
from datetime import datetime, timedelta

USERS_FILE = "data/users.json"

def carregar_usuarios():
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []

def salvar_usuarios(usuarios):
    with open(USERS_FILE, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, ensure_ascii=False, indent=4)

def gerar_id_usuario(usuarios):
    if not usuarios:
        return 1
    return max(u.get('id', 0) for u in usuarios) + 1

def buscar_usuario_por_email(email):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario.get('email') == email:
            return usuario
    return None

def cadastrar_usuario(nome, email, senha, data_nasc=None, idade=None, sexo=None):
    usuarios = carregar_usuarios()
    
    if buscar_usuario_por_email(email):
        return {"sucesso": False, "mensagem": "Email já cadastrado"}
    
    hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    novo_usuario = {
        "id": gerar_id_usuario(usuarios),
        "nome": nome,
        "email": email,
        "senha": hash_senha,
        "idade": idade,
        "data_nascimento": data_nasc,
        "sexo": sexo,
        "data_criacao": str(datetime.now().date())
    }
    
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    
    return {"sucesso": True, "mensagem": "Usuário cadastrado com sucesso"}

def autenticar_usuario(email, senha):
    usuario = buscar_usuario_por_email(email)
    
    if not usuario:
        return {"sucesso": False, "mensagem": "Credenciais inválidas"}
    
    senha_hash = usuario.get('senha')
    if not senha_hash:
        return {"sucesso": False, "mensagem": "Erro ao verificar credenciais"}
    
    if not bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
        return {"sucesso": False, "mensagem": "Credenciais inválidas"}
    
    SECRET_KEY = os.getenv('SECRET_KEY') or 'secret_key'
    token = jwt.encode({
        'user_id': usuario.get('id'),
        'email': usuario.get('email'),
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')
    
    return {
        "sucesso": True,
        "mensagem": "Login realizado com sucesso",
        "token": token,
        "usuario": {
            "id": usuario.get('id'),
            "nome": usuario.get('nome'),
            "email": usuario.get('email'),
            "data_nascimento": usuario.get('data_nascimento'),
            "data_nasc": usuario.get('data_nascimento'),
            "idade": usuario.get('idade'),
            "sexo": usuario.get('sexo')
        }
    }

def buscar_usuario_por_id(user_id):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario.get('id') == user_id:
            return usuario
    return None

def atualizar_usuario(user_id, dados_atualizacao):
    usuarios = carregar_usuarios()
    usuario_encontrado = None
    indice = None
    
    for i, usuario in enumerate(usuarios):
        if usuario.get('id') == user_id:
            usuario_encontrado = usuario
            indice = i
            break
    
    if not usuario_encontrado:
        return {"sucesso": False, "mensagem": "Usuário não encontrado"}
    
    novo_email = dados_atualizacao.get('email')
    if novo_email and novo_email != usuario_encontrado.get('email'):
        usuario_email_existente = buscar_usuario_por_email(novo_email)
        if usuario_email_existente and usuario_email_existente.get('id') != user_id:
            return {"sucesso": False, "mensagem": "Email já está em uso por outro usuário"}
    
    if 'nome' in dados_atualizacao:
        usuario_encontrado['nome'] = dados_atualizacao['nome']
    
    if 'email' in dados_atualizacao:
        usuario_encontrado['email'] = dados_atualizacao['email']
    
    if 'data_nasc' in dados_atualizacao:
        usuario_encontrado['data_nascimento'] = dados_atualizacao['data_nasc']
    
    if 'idade' in dados_atualizacao:
        usuario_encontrado['idade'] = dados_atualizacao['idade']
    
    if 'sexo' in dados_atualizacao:
        usuario_encontrado['sexo'] = dados_atualizacao['sexo']
    
    if 'senha' in dados_atualizacao and dados_atualizacao['senha']:
        nova_senha = dados_atualizacao['senha']
        if len(nova_senha) < 6:
            return {"sucesso": False, "mensagem": "A senha deve ter no mínimo 6 caracteres"}
        hash_senha = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        usuario_encontrado['senha'] = hash_senha
    
    usuarios[indice] = usuario_encontrado
    salvar_usuarios(usuarios)
    
    usuario_retorno = {k: v for k, v in usuario_encontrado.items() if k != 'senha'}
    
    return {
        "sucesso": True,
        "mensagem": "Usuário atualizado com sucesso",
        "usuario": usuario_retorno
    }

def deletar_usuario(user_id):
    usuarios = carregar_usuarios()
    usuario_encontrado = None
    indice = None
    
    for i, usuario in enumerate(usuarios):
        if usuario.get('id') == user_id:
            usuario_encontrado = usuario
            indice = i
            break
    
    if not usuario_encontrado:
        return {"sucesso": False, "mensagem": "Usuário não encontrado"}
    
    usuarios.pop(indice)
    salvar_usuarios(usuarios)
    
    return {
        "sucesso": True,
        "mensagem": "Usuário deletado com sucesso"
    }
