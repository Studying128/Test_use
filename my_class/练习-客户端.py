import socket
#1 客户端socket对象
cli_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2 链接服务端
cli_socket.connect(('127.0.0.1',5555))
# 循环发送信息并接受信息
while True:
    # # 3. 给服务端发送信息
    cli_in_str=input('客户端给服务端的信息:').encode(encoding='utf-8')
    cli_socket.send(cli_in_str)

    # 4.接受服务端信息并打印
    cli_out_str=cli_socket.recv(1024).decode(encoding='utf-8')
    print(f'服务器发送的信息:{cli_out_str}')

    # cli_socket.send(b'cli_in_str')

#6 关闭端口资源
cli_socket.close()
