""""
客户端给服务端上传文件

"""
import socket

# 1 创建socket对象
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 绑定ip,端口号
sever_socket.bind(('127.0.0.1', 6666))
# 3 设置监听
sever_socket.listen(5)
# 4 开启监听,等待客户端建立连接
accept_socket,client_socket=sever_socket.accept()
# 5 接受客户端发送的文件(内容)

with open('./data/yzl.jpg','wb') as dest_f:
    #  思路一  一次读取完文件,一次写完
    # #5.1 一次性从客户端读取所有的文件内容
    # rev_data_bytes=accept_socket.recv(1024_000_000)
    # # 5.2  具体往目的地文件写入数据的动作
    # dest_f.write(rev_data_bytes)

    # 思路2 一次读1024个字节
    while True:
        rev_data_bytes=accept_socket.recv(1024)
        if len(rev_data_bytes)<=0:
            break
        dest_f.write(rev_data_bytes)
# 7 释放资源
accept_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
# accept_socket.close()