#!/usr/bin/python3.6

import socket, time

ser = socket.socket()

def tcpserver_init(ip, port):
	ser = socket.socket()
	ser.bind((ip,port))
	ser.listen()
	# print(ser)
	return ser.accept()

def tcpserver_recv(cli):
	return cli.recv(100)

def tcpserver_send(cli):
	cli.send(b'xyz')

# print(ser)
cli, cliaddr = tcpserver_init('localhost', 9999)
cnt = 0
while True:
	time.sleep(1)	
	print("from client [%d] : %s" %(cnt, cliaddr[0]), tcpserver_recv(cli))
	cnt += 1
	tcpserver_send(cli)
ser.close()

