""""
 socket:
   概念:套接字的意思,网络编程核心
   即:通信段都有自己socket对象,子昂另个Socket之间通过
            字节流(TCP) 或数据包(udp) 形式进行传输
     1 导包
     2 创建Socket对象 指定 地址族, 传输方式
     3 打印socket对象


"""

import socket
#地址族  传输方式
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(cli_socket)