from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        partidoActual = Partido(self.repositorioPartido.findById(id))
<<<<<<< HEAD
=======
        partidoActual.id = infoPartido["id"]
>>>>>>> 2529a974ab4711442d1358b9242c7cd401a6849b
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)
