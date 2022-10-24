from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los partidos")

    def create(self, elPartido):
        print("Crear un partido")

    def show(self, id):
        print("Mostrando un partido con id ", id)

    def update(self, id, elPartido):
        print("Actualizando partido con id ", id)

    def delete(self, id):
        print("Elimiando partido con id ", id)
