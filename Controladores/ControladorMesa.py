from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        #print("Listar todos las mesas")
        unaMesa = {
            "numero": "22",
            "cantidad_inscritos": "124"
        }
        return [unaMesa]

    def create(self, infoMesa):
        print("Crear una mesa")
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def show(self, numero):
        print("Mostrando una mesa con numero ", numero)
        elMesa = {
            "numero": "22",
            "cantidad_inscritos": "124"
        }
        return elMesa
    def update(self, numero, infoMesa):
        print("Actualizando mesa con numero ", numero)
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def delete(self, id):
        print("Elimiando mesa con id ", id)
        return {"deleted_count": 1}
