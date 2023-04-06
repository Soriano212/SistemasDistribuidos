from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("10.10.10.82", "8080"))
s.send("Hello, world!")
data = s.recv(1024)

print(data)
s.close()