while True:
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    msg = input('请输入需要信息：')
    sock.sendto(msg.encode(), ('192.168.17.127', 10059))
