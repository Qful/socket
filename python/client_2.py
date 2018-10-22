#coding:utf-8
import socket
import time
import sys

SERVER_IP = "120.79.63.76"
SERVER_PORT = 8888
print 'Starting socket: TCP...'
server_addr = (SERVER_IP, SERVER_PORT)

try:  
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(server_addr)
	flag = '1'
	while True:
		time.sleep(3)
		print 'send to server with value: '+ flag
		sock.send(flag)
		print sock.recv(1024)
		flag = (flag=='1') and '2' or '1' #change to another type of value each time
	sock.close()
except Exception:
	print 'Can't connect to server,try it latter!'
	sock.close()
	sock=None
	sys.exit(1)