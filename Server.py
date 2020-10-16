import socket
from tool import GetDirectories


def Server(ip, port):
    basedir = "D:\\soft\\test\\a"
    dirs_files_list = [    ]
    a={}
    dirs_files_list=GetDirectories.GetDirectories(basedir)
    print(dirs_files_list)
    #print(a)


Server("127.0.0.1", 8000)
