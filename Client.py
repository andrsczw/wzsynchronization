import pickle
import socket
from tool import test, GetDictElement
from tool.SendMessage import SendMessage


def Client(ip, port, local_config_dir):
    #0000初始化
    msg = SendMessage(ip, port, "0000")
    remotedirs = pickle.loads(msg)
    if isinstance(remotedirs, dict):
        GetDictElement.GetDirsDictElement(remotedirs, lambda dic: print(dic))
        # for k in remotedirs.keys():
        #     if isinstance(remotedirs[k], dict):
        #         print(remotedirs[k])

    #print(type(a))
    #print("a:::", a)
    # print(msg.decode('utf-8'))
Client("127.0.0.1",8000,"d://test")