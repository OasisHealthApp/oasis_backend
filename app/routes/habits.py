from flask import Blueprint, request, jsonify
from app.services.habit_service import (
    listar_habitos, 
    buscar_habito_por_id, 
    criar_habito, 
    atualizar_habito, 
    excluir_habito,
    alternar_completado,
    listar_habitos_por_usuario
)


habits_bp = Blueprint('habits', __name__, url_prefix='/api')


@habits_bp.route('/habits', methods=['GET', 'OPTIONS'])
def get_habits():
    """Endpoint para listar todos os hábitos"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        return response, 200
    
    habitos = listar_habitos()
    return jsonify(habitos), 200


@habits_bp.route('/habits/<int:habito_id>', methods=['GET', 'OPTIONS'])
def get_habit(habito_id):
    """Endpoint para buscar um hábito específico"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, DELETE, OPTIONS')
        return response, 200
    
    habito = buscar_habito_por_id(habito_id)
    
    if habito:
        return jsonify(habito), 200
    else:
        return jsonify({"erro": "Hábito não encontrado"}), 404


@habits_bp.route('/habits', methods=['POST'])
def create_habit():
    """Endpoint para criar um novo hábito"""
    data = request.get_json()
    
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    titulo = data.get('titulo')
    descricao = data.get('descricao')
    categoria = data.get('categoria')
    repetir = data.get('repetir', False)
    tipo_repeticao = data.get('tipo_repeticao', 'diario')
    user_id = data.get('user_id')
    
    resultado = criar_habito(titulo, descricao, categoria, repetir, tipo_repeticao, user_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "habito": resultado['habito']
        }), 201
    else:
        return jsonify({"erro": resultado['mensagem']}), 400


@habits_bp.route('/habits/<int:habito_id>', methods=['PUT'])
def update_habit(habito_id):
    """Endpoint para atualizar um hábito existente"""
    data = request.get_json()
    
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    titulo = data.get('titulo')
    descricao = data.get('descricao')
    categoria = data.get('categoria')
    repetir = data.get('repetir')
    tipo_repeticao = data.get('tipo_repeticao')
    
    resultado = atualizar_habito(habito_id, titulo, descricao, categoria, repetir, tipo_repeticao)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "habito": resultado['habito']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 404


@habits_bp.route('/habits/<int:habito_id>', methods=['DELETE'])
def delete_habit(habito_id):
    """Endpoint para excluir um hábito"""
    resultado = excluir_habito(habito_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "habito": resultado['habito']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 404


@habits_bp.route('/habits/<int:habito_id>/toggle', methods=['POST', 'OPTIONS'])
def toggle_habit_complete(habito_id):
    """Endpoint para alternar status de completado do hábito"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response, 200
    
    resultado = alternar_completado(habito_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "habito": resultado['habito']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 404


@habits_bp.route('/habits/user/<int:user_id>', methods=['GET', 'OPTIONS'])
def get_user_habits(user_id):
    """Endpoint para listar hábitos de um usuário específico"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    habitos = listar_habitos_por_usuario(user_id)
    return jsonify(habitos), 200
