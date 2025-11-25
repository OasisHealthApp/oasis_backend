import os
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


HABITS_FILE = "data/habitos.json"


def calcular_proxima_data(data_referencia, tipo_repeticao):
    if isinstance(data_referencia, str):
        data_ref = datetime.strptime(data_referencia, '%Y-%m-%d')
    else:
        data_ref = data_referencia
    
    if tipo_repeticao == 'diario':
        proxima = data_ref + timedelta(days=1)
    elif tipo_repeticao == 'semanal':
        proxima = data_ref + timedelta(weeks=1)
    elif tipo_repeticao == 'mensal':
        # Usa relativedelta para lidar corretamente com meses diferentes
        proxima = data_ref + relativedelta(months=1)
        
        # Trata caso especial: se o dia não existe no próximo mês (ex: 31 em fevereiro)
        # relativedelta já ajusta automaticamente para o último dia do mês
    else:
        # Padrão: diário
        proxima = data_ref + timedelta(days=1)
    
    return proxima.strftime('%Y-%m-%d')


def carregar_habitos():
    try:
        if os.path.exists(HABITS_FILE):
            with open(HABITS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []


def salvar_habitos(habitos):
    """Salva hábitos no arquivo JSON"""
    with open(HABITS_FILE, 'w', encoding='utf-8') as file:
        json.dump(habitos, file, ensure_ascii=False, indent=4)


def gerar_id_habito(habitos):
    """Gera um ID único para novo hábito"""
    if not habitos:
        return 1
    return max(h.get('id', 0) for h in habitos) + 1


def listar_habitos():
    """Retorna todos os hábitos"""
    return carregar_habitos()


def buscar_habito_por_id(habito_id):
    """Busca um hábito específico pelo ID"""
    habitos = carregar_habitos()
    for habito in habitos:
        if habito.get('id') == habito_id:
            return habito
    return None


def criar_habito(titulo, descricao=None, categoria=None, repetir=False, tipo_repeticao='diario', user_id=None):
    """Cria um novo hábito"""
    if not titulo:
        return {"sucesso": False, "mensagem": "Título é obrigatório"}
    
    if not categoria:
        return {"sucesso": False, "mensagem": "Categoria é obrigatória"}
    
    # Valida tipo de repetição
    tipos_validos = ['diario', 'semanal', 'mensal']
    if tipo_repeticao not in tipos_validos:
        tipo_repeticao = 'diario'
    
    habitos = carregar_habitos()
    data_hoje = str(datetime.now().date())
    
    # Calcula próxima data se repetir está ativo
    proxima_data = None
    if repetir:
        proxima_data = calcular_proxima_data(data_hoje, tipo_repeticao)
    
    novo_habito = {
        "id": gerar_id_habito(habitos),
        "titulo": titulo,
        "descricao": descricao or "",
        "categoria": categoria,
        "repetir": repetir,
        "tipo_repeticao": tipo_repeticao if repetir else None,
        "dia_referencia": data_hoje,
        "proxima_data": proxima_data,
        "completado": False,
        "ultimo_completado": None,
        "sequencia_atual": 0,
        "melhor_sequencia": 0,
        "data_criacao": data_hoje,
        "user_id": user_id
    }
    
    habitos.append(novo_habito)
    salvar_habitos(habitos)
    
    return {"sucesso": True, "mensagem": "Hábito criado com sucesso", "habito": novo_habito}


def atualizar_habito(habito_id, titulo=None, descricao=None, categoria=None, repetir=None, tipo_repeticao=None):
    """Atualiza um hábito existente"""
    habitos = carregar_habitos()
    
    for habito in habitos:
        if habito.get('id') == habito_id:
            if titulo is not None:
                habito['titulo'] = titulo
            if descricao is not None:
                habito['descricao'] = descricao
            if categoria is not None:
                habito['categoria'] = categoria
            if repetir is not None:
                habito['repetir'] = repetir
                # Se desativar repetição, limpa campos relacionados
                if not repetir:
                    habito['tipo_repeticao'] = None
                    habito['proxima_data'] = None
            if tipo_repeticao is not None and habito.get('repetir'):
                tipos_validos = ['diario', 'semanal', 'mensal']
                if tipo_repeticao in tipos_validos:
                    habito['tipo_repeticao'] = tipo_repeticao
                    # Recalcula próxima data
                    dia_ref = habito.get('dia_referencia') or habito.get('ultimo_completado') or str(datetime.now().date())
                    habito['proxima_data'] = calcular_proxima_data(dia_ref, tipo_repeticao)
            
            salvar_habitos(habitos)
            return {"sucesso": True, "mensagem": "Hábito atualizado com sucesso", "habito": habito}
    
    return {"sucesso": False, "mensagem": "Hábito não encontrado"}


def excluir_habito(habito_id):
    """Exclui um hábito"""
    habitos = carregar_habitos()
    
    for i, habito in enumerate(habitos):
        if habito.get('id') == habito_id:
            habito_removido = habitos.pop(i)
            salvar_habitos(habitos)
            return {"sucesso": True, "mensagem": "Hábito excluído com sucesso", "habito": habito_removido}
    
    return {"sucesso": False, "mensagem": "Hábito não encontrado"}


def alternar_completado(habito_id):
    """Alterna o status de completado de um hábito"""
    habitos = carregar_habitos()
    
    for habito in habitos:
        if habito.get('id') == habito_id:
            habito['completado'] = not habito.get('completado', False)
            data_hoje = str(datetime.now().date())
            
            if habito['completado']:
                habito['ultimo_completado'] = data_hoje
                habito['sequencia_atual'] = habito.get('sequencia_atual', 0) + 1
                
                # Atualiza melhor sequência
                if habito['sequencia_atual'] > habito.get('melhor_sequencia', 0):
                    habito['melhor_sequencia'] = habito['sequencia_atual']
                
                # Se o hábito tem repetição, calcula a próxima data
                if habito.get('repetir') and habito.get('tipo_repeticao'):
                    habito['dia_referencia'] = data_hoje
                    habito['proxima_data'] = calcular_proxima_data(data_hoje, habito['tipo_repeticao'])
                else:
                    habito['proxima_data'] = None
            else:
                habito['sequencia_atual'] = 0
            
            salvar_habitos(habitos)
            return {"sucesso": True, "mensagem": "Status atualizado", "habito": habito}
    
    return {"sucesso": False, "mensagem": "Hábito não encontrado"}


def listar_habitos_por_usuario(user_id):
    """Retorna todos os hábitos de um usuário específico"""
    habitos = carregar_habitos()
    habitos_usuario = [h for h in habitos if h.get('user_id') == user_id]
    return habitos_usuario
