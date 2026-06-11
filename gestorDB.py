from datetime import datetime
from werkzeug.security import generate_password_hash
from modelo import db, Organizador, Evaluador, Trabajo, Asignacion

class GestorDB:
    def crearDB(self):
        db.create_all()

    def loginOrganizador(self, correo, clave):
        pass

    def loginEvaluador(self, correo, clave):
        pass

    def crearTrabajo(self):
        pass

    def getTrabajoPorId(self):
        pass

    def getTrabajoAutor(self, id_trabajo, email):
        pass

    def getTrabajosPendientes(self):
        pass

    def getEvaluadoresArea(self, area):
        pass
    
    def getCantidadAsignaciones(self, id_evaluador):
        pass

    def crearAsignacion(self, trabajo_id, evaluador_id):
        pass

    def getTrabajosEvaluador(self, id_evaluador):
        pass

    def getEvaluacionesRealizadas(self, id_evaluador):
        pass