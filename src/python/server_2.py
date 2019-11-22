#coding:utf-8

'''
建立一个python server，监听指定端口，
如果该端口被远程连接访问，则获取远程连接，然后接收数据，
并且做出相应反馈。
'''

#import necessary package
import socket
import time
import sys

HOST_IP = "172.18.250.47"
HOST_PORT = 17799
host_addr = (HOST_IP, HOST_PORT)
'''
print("Starting socket: TCP...")
#1.create socket object:socket=socket.socket(family,type)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
#2.bind socket to addr:socket.bind(address)
socket_tcp.bind(host_addr)
#3.listen connection request:socket.listen(backlog)
socket_tcp.listen(1)
#4.waite for client:connection,address=socket.accept()
socket_con, (client_ip, client_port) = socket_tcp.accept()
print("Connection accepted from %s." %client_ip)
socket_con.send("Welcome to RPi TCP server!")

print("Receiving package...")
while True:
    try:
        data=socket_con.recv(512)
        if len(data)>0:
            print("Received:%s"%data)
            if data=='1':
                GPIO.output(11,GPIO.HIGH)
            elif data=='0':
                GPIO.output(11,GPIO.LOW)
            socket_con.send(data)
            time.sleep(1)
            continue
    except Exception:
        socket_tcp.close()
        sys.exit(1)
'''
		
try: 
	print "Server is starting"
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(host_addr)  #配置soket，绑定IP地址和端口号
	sock.listen(5) #设置最大允许连接数，各连接和server的通信遵循FIFO原则
	print "Server is listenting port %s, with max connection 5" %HOST_PORT
	while True:  #循环轮询socket状态，等待访问
		connection,address = sock.accept()
		try:
			connection.settimeout(1000)
			#获得一个连接，然后开始循环处理这个连接发送的信息
			'''
			如果server要同时处理多个连接，则下面的语句块应该用多线程来处理，

			否则server就始终在下面这个while语句块里被第一个连接所占用，

			无法去扫描其他新连接了，但多线程会影响代码结构，所以记得在连接数大于1时

			下面的语句要改为多线程即可。
			'''
			while True:
				buf = connection.recv(512)
				print buf
				connection.send(buf)
				'''
				print "Get value" +buf
				if buf == '1':
					print "send welcome"
					connection.send('welcome to server!')
				elif buf!='0':
					connection.send('XXX'.encode())
					print "send refuse"
				else:
					print "close"
					break  #退出连接监听循环
				'''
		except socket.timeout:  #如果建立连接后，该连接在设定的时间内无数据发来，则time out
			print 'time out'
		print "closing one connection" #当一个连接监听循环退出后，连接可以关掉
		connection.close()  
		
except Exception:
 	print "Can't server,try it latter!"
	sys.exit(1)

           
