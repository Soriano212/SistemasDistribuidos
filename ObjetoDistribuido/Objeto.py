import Pyro4
import socket
import asyncio

### Objeto remoto
@Pyro4.expose
class Persona:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
    
    @staticmethod
    def crear_persona(nombre, cedula):
        return Persona(nombre, cedula)
    
    def verificar_cedula(self):
        
        if len(self.cedula) == 10:
            return "Cedula válida." 
        
        return "Cédula no válida."
    
    def to_string(self):

        return f"Nombre: {self.nombre}\nCédula: {self.cedula}"


### Servidor Socket
async def servidor_socket(uri: Pyro4.URI):
    
    # Creación del socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 5005)
    server_socket.bind(server_address)
    server_socket.listen(1)

    try:
        print("Servidor listo. Esperando conexión del cliente...")
        
        # Aceptar la conexión del cliente
        client_socket, client_address = server_socket.accept()
        print("Conexión establecida con el cliente:", client_address)

        # Enviar el URI del objeto Persona
        client_socket.sendall(str(uri).encode())
        
        print("URI enviado al cliente. Cerrando socket...")

        # Cerrar la conexión del socket
        client_socket.close()
        
        print("Socket cerrado...")
        
        
    except Exception as e:
        print("Error al enviar el URI:", e)
    except KeyboardInterrupt:
        print("El servidor se cerró.")

    finally:
        # Cierre del socket del servidor
        server_socket.close()

### Pyro4 Loop asincrono
async def pyro_loop(daemon):
    daemon.requestLoop()

### Main asincrono
async def main():
    # Configuración del servidor Pyro4
    daemon = Pyro4.Daemon()
    uri = daemon.register(Persona)
    
    print("URI del objeto Persona:", uri)
    
    servidor_socket_task = asyncio.create_task(servidor_socket(uri))
    
    # Inicia el loop de Pyro4 en segundo plano
    print("Iniciando el servidor Pyro4...")
    pyro_loop_task = asyncio.create_task(pyro_loop(daemon))
    
    # Esperar a que el loop de Pyro4 termine
    await asyncio.gather(servidor_socket_task, pyro_loop_task)

### Main
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("El programa se cerró.")


