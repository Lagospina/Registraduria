from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_cors import cross_origin
import json
from waitress import serve



app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado


miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorPartido = ControladorPartido()
miControladorResultado = ControladorResultado()

@app.route("/resultados", methods=['GET'])
def getResultados():
    json =miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/<string:id>", methods = ['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

@app.route("/resultados/mesas/<string:id_mesa>/candidatos/<string:id_candidato>", methods = ['POST'])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json =miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/mesas/<string:id_mesa>/candidatos/<string:id_candidato>", methods = ['PUT'])
def modificarResultado(id_resultado, id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.update(data, id_resultado, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>", methods = ['DELETE'])
def eliminarResultado(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)

##################candidatos#########################
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods = ['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods = ['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods = ['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods = ['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

##############partidos###############################
@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods = ['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods = ['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods = ['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods = ['DELETE'])
def eliminarpartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/candidato/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartidoACandidato(id, id_partido):
    json = miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)

###############Mesas######################################
@app.route("/mesas", methods = ['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods = ['POST'])
def crearMesas():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods = ['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods = ['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods = ['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("server running: "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app, host = dataConfig["url-backend"], port = dataConfig["port"])