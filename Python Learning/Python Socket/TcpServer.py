#!/usr/bin/python3.6

import socket, time

serverSocket = socket.socket()

def TcpServerInit(ip, port):
	serverSocket = socket.socket()
	serverSocket.bind((ip,port))
	serverSocket.listen()
	# print(serverSocket)
	return serverSocket.accept()

def TcpServerRecv(cliSocket):
	return cliSocket.recv(100)

def TcpServerSend(cliSocket):
	cliSocket.send(b'xyz')

# print(serverSocket)
cliSocket, cliAddr = TcpServerInit('localhost', 9999)
connCnt = 0
while True:
	time.sleep(1)	
	print("From Client [%d] : %s" %(connCnt, cliAddr[0]), TcpServerRecv(cliSocket))
	connCnt += 1
	TcpServerSend(cliSocket)
serverSocket.close()

