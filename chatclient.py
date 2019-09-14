import sys
import socket

'''

Three arguments to be passed while running from client side
1) Script name. For example: chatclient.py
2) IP address of the server to be connected.
3) Port number, which the server is using for the communication.

'''
if len(sys.argv)!=3:
    print ("Correct order: script name, IP address, port number")
    exit()
host = str(sys.argv[1])
port = int(sys.argv[2])  

#Creating a TCP/IP socket at client side to recieve data
s = socket.socket()

#Connect socket to the server and port number 
s.connect((host,port))
string = raw_input("Me: ")
while string!='exit':
    s.send(string.encode())
    
    #Recieve message
    data=s.recv(2048) #2048 is the buffer size
    data=data.decode()
    print("from server: "+data)
    string=raw_input("Me: ")
s.close()
