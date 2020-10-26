import pickle
import socket
import os

from tool import test


def ReceivedMessage(ip, port):
    """
    建立接受服务器
    :param ip:
    :param port:
    """
    s = socket.socket()
    s.bind((ip, port))
    s.listen()
    print("开始监听")
    while True:
        #每当接收到客户端socket的请求时，该方法就返回对应的socket和远程地址
        c, addr = s.accept()
        print("准备接收")
        print(c)
        print('连接地址：', addr)
        data = c.recv(1024)
        print(data)
        if data.decode('utf-8') == "0000":
            basedir = "D:\\soft\\test"
            dirs_files_list = []
            a = {}
            dirs_files_list = test.GetDirectories(basedir, {})
            print("dirs:  :::", dirs_files_list)
            c.send(pickle.dumps(dirs_files_list))

        print("c.recv(1024):   ", data.decode('utf-8'))

        #c.send('您好，您收到了服务器的回复'.encode('utf-8'))
        c.close()