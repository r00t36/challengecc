import sys
import socket

'''

Two arguments to be passed while running from server side
1) Script name. For example: chatserver.py
2) Port number, at which the communication is to be established. Range should be 1024 to 65535.

'''
if len(sys.argv)!=2:
    print ("Correct order: script name, port number")
    exit()

host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])  

#Creating a TCP/IP socket at server side
s = socket.socket()

#Binding the socket with hostname and port number
s.bind((host,port))

#Specifying maximum number of connections
s.listen(1)

#Storing c (connection object) and addr (address of client)
c,addr=s.accept()

print("client connected")
while True:
    data=c.recv(2048)
    if not data:
        break
    print("from client: "+str(data.decode()))
    data=raw_input("enter response: ")
    
    #send data to client in binary format
    c.send(data.encode())
c.close()
