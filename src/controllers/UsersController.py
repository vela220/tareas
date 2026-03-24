from src.models.UserModel import UsuarioModel
from src.models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, email, password):
        try:
            #Validar datos con el schema
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, password=password)
            sucess = self.model.registrar(nuevo_usuario)
            return sucess, "Usuario creado correctamente"
        except ValidationError as e:
            #Retoma el priemr error de validacion encontrado
            return False, e.errors()[0]['msg']
        