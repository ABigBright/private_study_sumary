#!/usr/bin/python3.6

import socket,time

def tcpcli_init(ip,port):
	cli = socket.socket()
	cli.connect((ip,port))
	return cli
	
def tcpcli_send(cli):
	cli.send(b'abc')

def tcpcli_recv(cli):
	return cli.recv(100)

cli = tcpcli_init('localhost', 9999)
cnt = 0
while True:
	tcpcli_send(cli)
	time.sleep(1)
	print("from server [%d] : " %cnt, tcpcli_recv(cli))
	cnt += 1
cli.close()

