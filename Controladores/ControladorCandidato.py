from Modelos.Candidato import Candidato

class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        #print("Listar todos los candidatos")
        unCandidato = {
            "_id": "abc124",
            "cedula": "124",
            "nombre": "Luis Alberto",
            "apellido": "Garcia"
        }
        return [unCandidato]

    def create(self, infoCandidato):
        #print("Crear un candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self, id):
        #print("Mostrando un candidato con id ", id)
        elCandidato = {
            "_id": id,
            "cedula": "124",
            "nombre": "Luis Alberto",
            "apellido": "Garcia"
        }
        return elCandidato

    def update(self, id, infoCandidato):
        print("Actualizando candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Eliminando candidato con id ", id)
        return {"deleted_count": 1}