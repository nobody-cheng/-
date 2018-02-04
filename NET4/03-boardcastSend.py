from socket import *

sock = socket(AF_INET, SOCK_DGRAM)

sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

sock.sendto('1:123456789:itcast-python:localhost:32:hello'.encode(), ('192.168.17.255', 2425))
