import socket

#1 建立socket服务对象连接,采用IPV4 字节流方式
sever_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2 bind ip地址和端口号 以元组形式传参
sever_socket.bind(('127.0.0.1',5555))
#3 listen设置监听 1-128 5
sever_socket.listen(5)
#4 等待客户端
accept_socket,client_socket=sever_socket.accept()
#5 循环模拟聊天
while True:
    #7 接收数据
    recv_str_bytes=accept_socket.recv(1024)
    recv_str=recv_str_bytes.decode(encoding='utf-8')
    if len(recv_str)<=0:
        break
    else:
        print(f"客户端发的信息:{recv_str}")

    #6 发送数据
    send_str=input('要给客户端发送内容:').encode(encoding='utf-8')
    accept_socket.send(send_str)

    # accept_socket.send(b'send_str')



#关闭路径经
accept_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
accept_socket.close()
