"""
长链接方式

"""
import socket

# 1. 创建服务器端Socket对象, 指定: 地址族, 传输方式.
# 参1: 地址族, Address Family, 即: 指定何种方式解析IP, 这里的 AF_INET代表 Ipv4
# 参2: 传输方式, 这里是: 字节流.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定ip地址 和 端口号.
server_socket.bind(('127.0.0.1', 5555))     # 元组形式: (字符串形式的ip地址, int类型的端口号)
# server_socket.bind(('192.168.24.148', 5555))     # 元组形式: (字符串形式的ip地址, int类型的端口号)
# 3. 设置监听. 范围: 1 ~ 128, 一般设置为: 5
server_socket.listen(5)
print('服务器端, 开始监听了...')

# 4. 等待客户端申请建立连接, 如果有, 则创建1个新的socket对象负责和该客户端交互.
# 参1: 负责和该客户端交互的 socket对象.
# 参2: 客户端的ip地址信息.
accept_socket, client_info = server_socket.accept()
# print(f'监听到客户端信息: {client_info}')

# 5. 给客户端写一句话.      二进制字符串形式.
# in_str=input('服务器端->客户端信息:').encode(encoding='utf-8')
# accept_socket.send(in_str)
# accept_socket.send(b'Welcome to study socket!')
while True:
    # 6. 接收客户端的回执信息.
    recv_data_bytes = accept_socket.recv(1024)
    recv_data = recv_data_bytes.decode(encoding='utf-8')
    print(f'服务器端收到回执信息: {recv_data}')
    #规定:886 发送的就关闭
    if recv_data == '886':
        break

accept_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
# 7. 释放资源.
accept_socket.close()
#端口号立刻关闭

