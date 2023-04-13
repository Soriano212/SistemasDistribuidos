import zmq, time

HOST, PORT = "10.10.10.105", "8080"

context = zmq.Context()
s.context.socket(zmq.PUB)
p = "tcp://"+HOST+":"+PORT
s.bind(p)

while True:
	time.sleep(5)
	s.send("TIME: "+time.asctime())

