HOST = '10.10.10.100'
PORT = 8080

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

s.send(b'Hola Servidor')
while True:
	data = s.recv(1024)
	if
