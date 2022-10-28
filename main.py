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
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorPartido import ControladorPartido

miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()
miControladorPartido = ControladorPartido()

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

# Métodos controladorResultado
@app.route("/resultado", methods=['GET'])
def getResultado():
    json = miControladorResultado.index()
    return jsonify(json)

@app.route("/resultado", methods=['POST'])
def crearResultado():
    data = request.get_json()
    json = miControladorResultado.create(data)
    return jsonify(json)

@app.route("/resultado/<string:id>", methods=['GET'])
def getResultados(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

@app.route("/resultado/<string:id>", methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json = miControladorResultado.update(id, data)
    return jsonify(json)

@app.route("/resultado/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)
# Finaliza controladorResultado

# Métodos controladorPartido
@app.route("/partido", methods=['GET'])
def getPartido():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['GET'])
def getPartidos(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)
# Finaliza controladorPartido

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
