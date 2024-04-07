""""
可以修改文件
"""

import socket
#1 地址族  ipv4   字节流   套界字对象
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#2 链接绑定,本地ip,设置服务器端口号
sever_socket.bind(('127.0.0.1',5555))#元组形式
#3 设置监听,1-128 一般设置为5
sever_socket.listen(5)
print('开始监听')

while True:
    #4 等待客户端信息链接,   .acept()方法会放回一个 客户端交互的socket的对象
     # 客户端ip地址信息
    accept_socket,client_socket = sever_socket.accept()
    #5 服务端给客户端发送信息
    in_str=input('输入服务端要给客户端信息:')
    in_str_bytes=in_str.encode(encoding='utf-8')
    accept_socket.send(b'welcome to study socket!')
    accept_socket.send(in_str_bytes)
    #6 服务端接受客户端信息并打印
    recv_data_bytes=accept_socket.recv(1024)
    recv_data=recv_data_bytes.decode(encoding='utf-8')
    print(f'recv_data={recv_data}')

    #7关闭服务端交互对象
    accept_socket.close()

    #8立刻放端口口
    #  1 当前socket对象 2 是否立即是否释放端口号
    sever_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)


