import socket
from tool import test


def Server(ip, port):
    basedir = "D:\\soft\\test"
    dirs_files_list = [    ]
    a={}
    dirs_files_list=test.GetDirectories(basedir,{})
    print("dirs:  :::",dirs_files_list)

    for i in dirs_files_list:
        print('i:  ', i)
        print("dirs_files_list[i]:   ", dirs_files_list[i])
    #print(a)


Server("127.0.0.1", 8000)
