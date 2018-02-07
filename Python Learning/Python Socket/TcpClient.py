#!/usr/bin/python3.6

import socket,time

def TcpCliInit(ip,port):
	cli = socket.socket()
	cli.connect((ip,port))
	return cli
	
def TcpCliSend(cli):
	cli.send(b'abc')

def TcpCliRecv(cli):
	return cli.recv(100)

cli = TcpCliInit('localhost', 9999)
connCnt = 0
while True:
	TcpCliSend(cli)
	time.sleep(1)
	print("From Server [%d] : " %connCnt, TcpCliRecv(cli))
	connCnt += 1
cli.close()

