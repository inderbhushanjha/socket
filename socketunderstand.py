import socket
import sys

if(len(sys.argv)<3):
    print("Try using host name and port number\nOperation: \{filename\} \{host name\} \{port number\}")
    sys.exit(0)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("failed creation socket")
    print("Reason: "+str(error))
    sys.exit(4)
print("socket created successful")

targethost = sys.argv[1]
port = sys.argv[2]

try:
    sock.connect((targethost,int(port)))
    print("socket connected to :"+targethost+":"+str(port))
    sock.shutdown(1)
except socket.error as error:
    print("failed to connect to host")
    print("Reason: "+str(error))
    