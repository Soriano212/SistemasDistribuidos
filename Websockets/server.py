import websockets
import asyncio
import json
import datetime
async def timer(websocket, path):
    # Lógica del servidor
    while True:
        # Espera a recibir un mensaje del cliente
        mensaje = await websocket.recv()
        print(f"Mensaje recibido: {mensaje}")

        # Envia un mensaje al cliente
        while(True):
            # Espera 5 segundos antes de enviar una respuesta
            await asyncio.sleep(5)
            time=str(datetime.datetime.now())
            respuesta = json.dumps(["Hola, de parte del servidor",time])
            await websocket.send(respuesta)

start_server = websockets.serve(timer, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()