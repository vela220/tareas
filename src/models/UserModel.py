import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        #Encontrar contraseña
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)

        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                    "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)",
                    (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
                )
            conn.commit()
            return True
        except Exception as e:
                    print(f"Error: {e}")
                    return False
        finally:
                        conn.close()

    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user
        return None
    
    def iniciar_sesion(self, usuario_data):
        conn = None
        cursor = None
    try:
            # establecer conexion
            conn = self.db.get_connection()
            cursor =conn.cursor(dictionary=True) #dictionary=True facilita leer por nombre de clumna
            
            #definir la consulta
            #IMPORNTANE: Usamos placeholders(%s) para evitar inyeccion SQL
            query = "SELECT * FROM usuario WHERE email = %s"
            values = (usuario_data.email,)
            
            #ejecutar y obetener resultado
            cursor.execute(query, values)
            usuario_encontrado = cursor.fetchone()
            
            #logica de retorno
            if usuario_encontrado:
                #verificar la ontraseña usando bcrypt
                if bcrypt.checkpw(usuario_data.contraseña.encode('utf-8'), usuario_encontrado['contraseña'].encode('utf-8')):
                    return True #credenciales validas
                else:
                    return false #no se encontro el usuario o la clave no coincide
                