import socket
from tool import GetDirectories


def Server(ip, port):
    basedir = "D:\\soft\\test\\a"
    dirs_files_list = [    ]
    dirs_files_list=GetDirectories.GetDirectories(basedir)
    #print(a)


Server("127.0.0.1", 8000)
