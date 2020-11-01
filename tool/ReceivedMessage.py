import pickle
import socket
import os
import time

from tool import GetDirectories
from tool.GetFileNameByDirName import GetFileNameByDirName


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
        command = data.decode('utf-8')
        basedir = "D:\\soft\\test"
        if command == "0000":

            dirs_files_list = {}

            dirs_files_list = GetDirectories.GetDirectories(basedir, {})
            print("dirs:  :::", dirs_files_list)
            c.send(pickle.dumps(dirs_files_list))
        elif command.split("#")[0] == "0001":

            dir = basedir + "\\" + command.split("#")[1][1:]
            dir = dir.replace('*', '\\')
            files_list = GetFileNameByDirName(dir,basedir)
            print("files_list:  ", files_list, dir)

            c.send(pickle.dumps(files_list))
        elif command.split("#")[0] == "0002":
            dir = basedir + "\\" + command.split("#")[1][1:]
            dir = dir.replace('*', '\\')
            print("1111111111"+dir)
            f = open(dir,'rb')
            c.sendall(f.read())


        elif command.split("#")[0] == "0003":
            file = basedir + "\\" + command.split("#")[1][1:]
            file = dir.replace('*', '\\')
            c.send(str(os.path.getmtime(file)).encode('utf-8'))
        #print("c.recv(1024):   ", data.decode('utf-8'))

        #c.send('您好，您收到了服务器的回复'.encode('utf-8'))
        c.close()