import socket

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_socket.connect(('127.0.0.1', 6666))
# cli_socket.connect(('192.168.24.148', 6666))

with open('D:/Ai_test_dictory/01.jpg','rb') as src_f:
    # #方式1 一次读所有,
    # data_bytes=src_f.read()
    # cli_socket.send(data_bytes)

    #方式二
    while True:
        data_bytes = src_f.read(1024)
        cli_socket.send(data_bytes)
        if len(data_bytes) <= 0:
            break
cli_socket.close()