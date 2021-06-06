import socket
import sys

#set server IP as first argument
if (len(sys.argv) > 1):
	Server_IP = sys.argv[1]
else:
	print("\nRun like \n python3 5.4_client.py < server ip address > \n\n")
	exit(1)

#create socket
s = socket.socket()

#choose port
Port = 9797

s.connect((Server_IP, Port))

filetosend = input('\nFile name to be stored in server:')
s.send(filetosend.encode())
file = open(filetosend, 'rb')

SendData = file.read(99999)

while SendData:
	print("\nResponse from server:", s.recv(1024).decode('utf-8'))

	s.send(SendData)
	SendData = file.read(99999)
	print(filetosend + " is completely copied to the server directory\n")

s.close()
