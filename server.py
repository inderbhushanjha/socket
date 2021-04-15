import socket
import sys


serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversock.bind(("127.0.0.1",5993))

serversock.listen(5) #here 5 is backlog and means 5 connections are waiting if server is busy if the 6th socket will try to connect then server will refusr the connection


while True:
    print("Server is waiting...")
    clientsock , addr = serversock.accept() #this is accept method
    print("client connected from: "+str(addr))
    while True:
        data = clientsock.recv(1024)
        if not data or data.decode("utf-8") == "END":
            break
        print("Client: %s"%data.decode("utf-8"))
        try:
            clientsock.send(bytes("Request recieved","utf-8"))
        except:
            print("Exited by the user")
    clientsock.close()
