from flask import Blueprint, request, jsonify
from app.services.category_service import (
    listar_todas_categorias,
    buscar_categoria_por_id,
    criar_categoria_usuario,
    atualizar_categoria_usuario,
    excluir_categoria_usuario,
    listar_categorias_usuario_por_id
)


categories_bp = Blueprint('categories', __name__, url_prefix='/api')


@categories_bp.route('/categories', methods=['GET', 'OPTIONS'])
def get_categories():
    """Endpoint para listar todas as categorias (padrão + customizadas)"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    user_id = request.args.get('user_id', type=int)
    categorias = listar_todas_categorias(user_id)
    return jsonify(categorias), 200


@categories_bp.route('/categories/<categoria_id>', methods=['GET', 'OPTIONS'])
def get_category(categoria_id):
    """Endpoint para buscar uma categoria específica"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    categoria = buscar_categoria_por_id(categoria_id)
    
    if categoria:
        return jsonify(categoria), 200
    else:
        return jsonify({"erro": "Categoria não encontrada"}), 404


@categories_bp.route('/categories', methods=['POST'])
def create_category():
    """Endpoint para criar uma nova categoria customizada"""
    data = request.get_json()
    
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    nome = data.get('nome')
    emoji = data.get('emoji')
    descricao = data.get('descricao')
    cor = data.get('cor')
    user_id = data.get('user_id')
    
    resultado = criar_categoria_usuario(nome, emoji, descricao, cor, user_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "categoria": resultado['categoria']
        }), 201
    else:
        return jsonify({"erro": resultado['mensagem']}), 400


@categories_bp.route('/categories/<int:categoria_id>', methods=['PUT'])
def update_category(categoria_id):
    """Endpoint para atualizar uma categoria customizada"""
    data = request.get_json()
    
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    nome = data.get('nome')
    emoji = data.get('emoji')
    descricao = data.get('descricao')
    cor = data.get('cor')
    user_id = data.get('user_id')
    
    resultado = atualizar_categoria_usuario(categoria_id, nome, emoji, descricao, cor, user_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "categoria": resultado['categoria']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 404


@categories_bp.route('/categories/<int:categoria_id>', methods=['DELETE'])
def delete_category(categoria_id):
    """Endpoint para excluir uma categoria customizada"""
    data = request.get_json()
    user_id = data.get('user_id') if data else None
    
    if not user_id:
        return jsonify({"erro": "ID do usuário é obrigatório"}), 400
    
    resultado = excluir_categoria_usuario(categoria_id, user_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "categoria": resultado['categoria']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 404


@categories_bp.route('/categories/user/<int:user_id>', methods=['GET', 'OPTIONS'])
def get_user_categories(user_id):
    """Endpoint para listar apenas categorias customizadas de um usuário"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    categorias = listar_categorias_usuario_por_id(user_id)
    return jsonify(categorias), 200
