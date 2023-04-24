import zmq

HOST, PORT = "10.10.10.105", "8080"

context=zmq.Context()
s=context.socket(zmq.SUB)
p="tcp://"+HOST+":"+PORT
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")

for i in range(5):
	time=s.recv()
	print(time)
