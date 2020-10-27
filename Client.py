import pickle
import socket
from tool import  GetDictElement
from tool.SendMessage import SendMessage


def Client(ip, port, local_config_dir):
    #0000初始化
    msg = SendMessage(ip, port, "0000")
    remotedirs = pickle.loads(msg)
    if isinstance(remotedirs, dict):
        print(remotedirs)
        GetDictElement.GetDirsDictElement(remotedirs, lambda dic: print(len(dic)))
        # for k in remotedirs.keys():
        #     if isinstance(remotedirs[k], dict):
        #         print(remotedirs[k])

    #print(type(a))
    #print("a:::", a)
    # print(msg.decode('utf-8'))
Client("127.0.0.1",8000,"d://test")