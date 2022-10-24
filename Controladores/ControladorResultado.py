from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todos los resultados")

    def create(self, elResultado):
        print("Crear un resultado")

    def show(self, id):
        print("Mostrando un resultado con id ", id)

    def update(self, id, elResultado):
        print("Actualizando resultado con id ", id)

    def delete(self, id):
        print("Elimiando resultado con id ", id)
