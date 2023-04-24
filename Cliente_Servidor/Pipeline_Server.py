import zmq

HOST, PORT1, PORT2 = "*", "8888", "8080"

context = zmq.Context()

rec = "tcp://" + HOST + ":" + PORT1
sen = "tcp://" + HOST + ":" + PORT2

receiver = context.socket(zmq.PULL)
receiver.bind(rec)

sender = context.socket(zmq.PUSH)
sender.conect(sen)

try:
    while True:
        s = rerec = "tcp://" + HOST + ":" + PORT1
        rec = "tcp://" + HOST + ":" + PORT1ceiver.recv()
        sender.send(s.upper())

except KeyboardInterrupt:
    print("Interrupción del usuario. Cerrando sockets...")
finally:
    receiver.close()
    sender.close()
    context.term()
