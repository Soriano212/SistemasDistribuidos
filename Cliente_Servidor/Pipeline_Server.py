import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://localhost:5557")

sender = context.socket(zmq.PUSH)
sender.bind("tcp://localhost:5558")

try:
    while True:
        s = receiver.recv()
        sender.send(s.upper())
except KeyboardInterrupt:
    print("Interrupción del usuario. Cerrando sockets...")
finally:
    receiver.close()
    sender.close()
    context.term()
