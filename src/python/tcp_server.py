#coding:utf-8

import socket
import time
import sys

HOST_IP = "182.61.61.133"
HOST_PORT = 17799
host_addr = ("", HOST_PORT)

def tcp_server():
    print("Starting socket: TCP server")
    #1.create socket object:socket=socket.socket(family,type)
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )

    #2.bind socket to addr:socket.bind(address)
    socket_tcp.bind(host_addr)
    #3.listen connection request:socket.listen(backlog)
    socket_tcp.listen(5)
    #4.waite for client:connection,address=socket.accept()
    socket_con, (client_ip, client_port) = socket_tcp.accept()
    print("Connection accepted from %s." %(client_ip.encode()))
    socket_con.send("Welcome to TCP server!")

    while True:
        try:
            data=socket_con.recv(512)
            if len(data)>0:
                print("Received:%s"%data)
                socket_con.send(data)
                time.sleep(1)
                continue
        except Exception:
            socket_tcp.close()
            sys.exit(1)