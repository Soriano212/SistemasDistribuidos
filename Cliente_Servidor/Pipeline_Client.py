import zmq
import time

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5557")

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5558")

for i in range(10):
    msg = f"Mensaje {i}"
    sender.send(msg.encode())
    result = receiver.recv()
    print(f"Mensaje enviado: {msg}, Resultado: {result.decode()}")
    time.sleep(1)