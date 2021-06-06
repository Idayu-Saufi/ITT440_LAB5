import socket

#create socket
s = socket.socket()

#choose port
Hostname = socket.gethostname()
ip_addr = socket.gethostbyname(Hostname)
print("Ip address Server is ", ip_addr)
Port = 9797

print ("\n Waiting for Client to connect...")

#bind to the port
s.bind(('',Port))
print("Binded to %s" %(Port))

#put the socket into listening mode
s.listen(5)
print("Socket is listening ")

while True:
	c, addr = s.accept()
	msg = "Connected to " + addr[0] + "\nHi, Thank You for Connnecting to our Server\n"
	c.send(msg.encode())

	filename = c.recv(1024).decode('utf-8')
	file = open(filename, 'wb')

	data = c.recv(99999)

	while data:
		file.write(data)
		data = c.recv(99999)

#close file when copy is completed
file.close()
print("\nCopy File is Completed ")

c.close()
print("\nConnection Closed\n")

