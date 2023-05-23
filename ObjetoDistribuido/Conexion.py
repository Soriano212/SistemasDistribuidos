import Pyro4
import socket

# Creación del socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 5005)  # Dirección y puerto del servidor
client_socket.connect(server_address)

try:
    print("Esperando recibir uri.")
    
    # Recibir el URI del objeto de Pyro4 desde el servidor
    uri_str = client_socket.recv(1024).decode()
    uri = Pyro4.URI(uri_str)
    
    print("URI del objeto Persona:", uri)
    print("Conectando al objeto remoto...")

    # Conectar al objeto remoto
    persona = Pyro4.Proxy(uri)

    # Crea un objeto Persona con nombre "Alberto" y cédula "0150440378"
    nombre = "Alberto"
    cedula = "1234567890"
    mi_persona = persona.__class__(nombre, cedula)

    # Ejecuta los métodos del objeto remoto
    print(mi_persona.to_string())
    print("La cédula es válida" if mi_persona.verificar_cedula() else "La cédula no es válida")

except KeyboardInterrupt as e:
    print("Error al recibir o conectar al URI:", e)
finally:
    # Cerrar la conexión del cliente
    client_socket.close()
