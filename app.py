# Aqui importamos os módulos da nossa aplicação
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

"""
Se quiser importar um arquivo, basta seguir o padrão:

import pasta.arquivo

ou se quiser importar funções específicas, use:

from pasta.nome_arquivo import funcao(ou '*' para importar todas de uma vez)
"""

server = Flask(__name__)
CORS(server)

@server.route('/')
def response():
    return 'Hello, and welcome to my page.'

@server.route('/habits')
def data():
    with open("data/habits.json", "r", encoding="utf-8") as file:
        habits = json.load(file)
    return jsonify(habits)
    


if __name__ == "__main__":
    server.run()


