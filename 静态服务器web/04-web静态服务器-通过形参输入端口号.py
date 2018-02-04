import socket
import re
import sys







def main():
    if len(sys.argv) == 2:
        port_str = sys.argv[1]
        if port_str.isdigit():
            port = int(port_str)
        else:
            print('请输入正确的端口号')
            return
    else:
        print('请以 python3 xxx.py 8888方式运行服务器')
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 重复使用端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    server_socket.bind(('', 8888))
    #  设置监听,变为被动的套接字
    server_socket.listen(250)
    while True:
        # 接受连接accept
        new_socket, new_addr = server_socket.accept()
        # 接收数据
        recv_data = new_socket.recv(1024)
        # 判断是否有数据，然后进行解码
        if not recv_data:
            continue
        request = recv_data.decode()
        # print(request)
        request_lines = request.splitlines()
        print(request_lines)
        for i, line in enumerate(request_lines):
            print(i, line)
        # 正则表达式 解析发送过来的请求

        ret = re.match(r'([^/]*)([^ ]*)', request_lines[0])
        file_path = ret.group(2)

        if file_path == '/':
            file_path = '/index.html'
        print('================文件的路径', file_path)

        # 找到对应的文件，打开文件读取数据，返回客户端
        try:
            f = open(g_documents_root + file_path, 'rb')
        except Exception as ret:
            print('打开文件失败', ret)
            response_header = 'HTTP/1.1 404 Not Found\r\n'
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += '\r\n'
            response_body = 'sorry,请求页面失败'
            response = response_header + response_body
            new_socket.send(response.encode())

        else:
            content = f.read()

            # 返回一个固定的数据
            response_header = 'HTTP/1.1 200 OK\r\n'
            response_header += '\r\n'
            response_body = content
            # response = response_header + response_body,字符串和二进制无法运算

            new_socket.send(response_header.encode())
            new_socket.send(response_body)
            # new_socket.close()
        finally:
            new_socket.close()

if __name__ == '__main__':
    main()