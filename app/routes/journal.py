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

@journal_bp.route('/journal', methods=['GET'])
def get_journal_entries():
    registros = listar_registros()
    return jsonify(registros), 200

@journal_bp.route('/journal/<int:registro_id>', methods=['GET'])
def get_journal_entry(registro_id):
    registro = buscar_registro_por_id(registro_id)
    
    if registro:
        return jsonify(registro), 200
    else:
        return jsonify({"erro": "Registro não encontrado"}), 404

@journal_bp.route('/journal', methods=['POST'])
def create_journal_entry():
    data = request.get_json()
    
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    conteudo = data.get('conteudo')
    user_id = data.get('user_id')
    data_registro = data.get('data')
    
    resultado = criar_registro(conteudo, user_id, data_registro)

    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "registro": resultado['registro']
        }), 201
    else:
        return jsonify({"erro": resultado['mensagem']}), 400

@journal_bp.route('/journal/<int:registro_id>', methods=['PUT'])
def update_journal_entry(registro_id):
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
    try:
        data = request.get_json() or {}
        user_id = data.get('user_id')
        
        print(f"[DELETE JOURNAL] ID: {registro_id}, User ID: {user_id}")
        print(f"[DELETE JOURNAL] Request data: {data}")
        
        resultado = excluir_registro(registro_id, user_id)
        
        print(f"[DELETE JOURNAL] Resultado: {resultado}")
        
        if resultado['sucesso']:
            return jsonify({
                "mensagem": resultado['mensagem'],
                "registro": resultado['registro']
            }), 200
        else:
            return jsonify({"erro": resultado['mensagem']}), 404
    except Exception as e:
        print(f"[DELETE JOURNAL] Erro: {str(e)}")
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@journal_bp.route('/journal/user/<int:user_id>', methods=['GET'])
def get_user_journal_entries(user_id):
    registros = listar_registros_por_usuario(user_id)
    return jsonify(registros), 200

@journal_bp.route('/journal/user/<int:user_id>/date/<data>', methods=['GET'])
def get_journal_by_date(user_id, data):
    registros = buscar_registro_por_data(user_id, data)
    return jsonify(registros), 200
