from flask import Flask, request, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)

# Inicializa o banco de dados
database.init_db()

@app.route('/dispositivos', methods=['POST'])
def adicionar():
    dados = request.json
    ip = dados['ip']
    nome = dados['nome']
    trafego = dados['trafego']
    database.adicionar_dispositivo(ip, nome, trafego)
    return jsonify({'mensagem': 'Dispositivo adicionado com sucesso!'})

@app.route('/dispositivos', methods=['GET'])
def listar():
    dispositivos = database.listar_dispositivos()
    lista = [{
        'id': d[0],
        'ip': d[1],
        'nome': d[2],
        'trafego': d[3]
    } for d in dispositivos]
    return jsonify(lista)

@app.route('/dispositivos/<int:id>', methods=['DELETE'])
def remover(id):
    database.remover_dispositivo(id)
    return jsonify({'mensagem': 'Dispositivo removido com sucesso!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
