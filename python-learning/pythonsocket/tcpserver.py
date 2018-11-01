#!/usr/bin/python3.6

import socket, time

ser = socket.socket()

def tcpser_init(ip, port):
	ser = socket.socket()
	ser.bind((ip,port))
	ser.listen()
	# print(ser)
	return ser.accept()

def tcpser_recv(cli):
	return cli.recv(100)

def tcpser_send(cli):
	cli.send(b'xyz')

# print(ser)
cli, cliaddr = tcpser_init('localhost', 9999)
cnt = 0
while True:
	time.sleep(1)	
	print("from client [%d] : %s" %(cnt, cliaddr[0]), tcpser_recv(cli))
	cnt += 1
	tcpser_send(cli)
ser.close()

