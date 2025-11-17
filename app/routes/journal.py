from flask import Blueprint, request, jsonify
from app.services.journal_service import (
    listar_registros,
    listar_registros_por_usuario,
    buscar_registro_por_id,
    buscar_registro_por_data,
    criar_registro,
    atualizar_registro,
    excluir_registro
)


journal_bp = Blueprint('journal', __name__, url_prefix='/api')


@journal_bp.route('/journal', methods=['GET', 'OPTIONS'])
def get_journal_entries():
    """Endpoint para listar todos os registros diários"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    registros = listar_registros()
    return jsonify(registros), 200


@journal_bp.route('/journal/<int:registro_id>', methods=['GET', 'OPTIONS'])
def get_journal_entry(registro_id):
    """Endpoint para buscar um registro específico"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    registro = buscar_registro_por_id(registro_id)
    
    if registro:
        return jsonify(registro), 200
    else:
        return jsonify({"erro": "Registro não encontrado"}), 404


@journal_bp.route('/journal', methods=['POST'])
def create_journal_entry():
    """Endpoint para criar um novo registro diário"""
    data = request.get_json()
    
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    conteudo = data.get('conteudo')
    user_id = data.get('user_id')
    data_registro = data.get('data')
    
    resultado = criar_registro(conteudo, user_id, data_registro)

    if resultado['sucesso']:
        # Sempre retornamos 201 para nova criação
        return jsonify({
            "mensagem": resultado['mensagem'],
            "registro": resultado['registro']
        }), 201
    else:
        return jsonify({"erro": resultado['mensagem']}), 400


@journal_bp.route('/journal/<int:registro_id>', methods=['PUT'])
def update_journal_entry(registro_id):
    """Endpoint para atualizar um registro existente"""
    data = request.get_json()
    
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    conteudo = data.get('conteudo')
    user_id = data.get('user_id')
    
    resultado = atualizar_registro(registro_id, conteudo, user_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "registro": resultado['registro']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 404


@journal_bp.route('/journal/<int:registro_id>', methods=['DELETE'])
def delete_journal_entry(registro_id):
    """Endpoint para excluir um registro"""
    data = request.get_json()
    user_id = data.get('user_id') if data else None
    
    resultado = excluir_registro(registro_id, user_id)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "registro": resultado['registro']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 404


@journal_bp.route('/journal/user/<int:user_id>', methods=['GET', 'OPTIONS'])
def get_user_journal_entries(user_id):
    """Endpoint para listar registros de um usuário específico"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    registros = listar_registros_por_usuario(user_id)
    return jsonify(registros), 200


@journal_bp.route('/journal/user/<int:user_id>/date/<data>', methods=['GET', 'OPTIONS'])
def get_journal_by_date(user_id, data):
    """Endpoint para buscar registro de um usuário em uma data específica"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    registros = buscar_registro_por_data(user_id, data)
    # Retorna lista (pode estar vazia)
    return jsonify(registros), 200
