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
# 3 接受服务端发送的信息
recv_data_bytes= cli_socket.recv(1024)
recv_data=recv_data_bytes.decode(encoding='utf8')
print(f'服务端发送{recv_data}')
# 4 给服务端发送信息
sed_str='over'.encode(encoding='utf-8')
cli_socket.send(sed_str)

# 5 释放资源
cli_socket.close()
