from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos las mesas")

    def create(self, elMesa):
        print("Crear una mesa")

    def show(self, id):
        print("Mostrando una mesa con id ", id)

    def update(self, id, elMesa):
        print("Actualizando mesa con id ", id)

    def delete(self, id):
        print("Elimiando mesa con id ", id)
