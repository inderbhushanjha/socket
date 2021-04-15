import socket
import sys

clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
data = "Hey server"
try:
    clientsock.connect(("127.0.0.1",5993))
    print("Connected successfully")
except socket.error as error:
    print("connection failed\nReason: "+str(error))
try:
    while True:
        clientsock.send(data.encode("utf-8"))
        dat = clientsock.recv(1024)
        print("server: "+str(dat))
        data = input("You: ")
except KeyboardInterrupt:
    print("Exited by the user")

clientsock.close()



