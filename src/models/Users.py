import bcrypt
from .database import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        #Encontrar cpntraseña
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario)