import os
import pickle
import socket
from tool import GetDictElement, GetDirectories
from tool.SendMessage import SendMessage
import shutil

def createBlankDirs(dir, basedir):
    print("0001#"+dir)
    os.mkdir(basedir + "\\" + dir)
    msg = SendMessage("127.0.0.1", 8000, "0001#" + dir)
    remotefiles = pickle.loads(msg)
    print(remotefiles)
    # os.mkdir(basedir+"//"+dir)


def tes(dir):
    msg = SendMessage("127.0.0.1", 8000, "0001#"+dir)
    remotefiles = pickle.loads(msg)
    print(remotefiles)
    #os.mkdir(basedir+"//"+dir)



def Client(ip, port, local_config_dir):
    #0000初始化
    msg = SendMessage(ip, port, "0000")
    remotedirs = pickle.loads(msg)
    # 清空目录
    shutil.rmtree(local_config_dir)
    os.mkdir(local_config_dir)
    localdirs = GetDirectories.GetDirectories(local_config_dir, {})

    #print("remotedirs:  ", remotedirs, "localdirs:  ", localdirs)
    if isinstance(remotedirs, dict):
        #print(remotedirs)
        #新建空目录
        GetDictElement.GetDirsDictElement(remotedirs, createBlankDirs, local_config_dir)#("lambda x:print  ",  x))

        # for k in remotedirs.keys():
        #     if isinstance(remotedirs[k], dict):
        #         print(remotedirs[k])

    #print(type(a))
    #print("a:::", a)
    # print(msg.decode('utf-8'))
Client("127.0.0.1",8000,"d:\\test")