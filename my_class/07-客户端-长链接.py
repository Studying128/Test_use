""""
    1 创建客户端socket对象 指定 地址族,传输方式
    2 链接服务端,指定链接服务器ip地址, 端口号
    3 接受服务端发送的信息
    4 给服务端发送信息
    5 释放资源
"""

import socket
# 1 创建客户端socket对象 指定 地址族,传输方式
cli_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 链接服务端,指定链接服务器ip地址, 端口号
cli_socket.connect(('127.0.0.1', 5555))
# cli_socket.connect(('192.168.24.115', 5555))

while True:

# 4 给服务端发送信息
    sed_str=input('要给服务器的信息:').encode(encoding='utf-8')
    cli_socket.send(sed_str)

    if sed_str=='886'.encode(encoding='utf-8'):
        break

# 5 释放资源
cli_socket.close()
