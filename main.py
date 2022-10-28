from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()

# Métodos controladorCandidato
@app.route("/candidatos", methods=['GET'])
def getCandidato():
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidatos(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)
# Finaliza controladorCandidato

# Métodos controladorMesa
@app.route("/mesas", methods=['GET'])
def getMesa():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:numero>", methods=['GET'])
def getMesas(numero):
    json = miControladorMesa.show(numero)
    return jsonify(json)

@app.route("/mesas/<string:numero>", methods=['PUT'])
def modificarMesa(numero):
    data = request.get_json()
    json = miControladorMesa.update(numero, data)
    return jsonify(json)

@app.route("/mesas/<string:numero>", methods=['DELETE'])
def eliminarMesa(numero):
    json = miControladorMesa.delete(numero)
    return jsonify(json)
# Finaliza controladorMesa

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
