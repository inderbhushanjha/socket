import socket
import sys

def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return True
    except socket.error as error:
        return False

if(create_socket):
    print("Socket Created Successfully")
else:
    print("Could not connect to the socket")