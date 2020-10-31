import os
import pickle
import socket
import time

from tool import GetDictElement, GetDirectories
from tool.GetFileByFileName import GetFile
from tool.SendMessage import SendMessage
import shutil

def createBlankDirs(dir, basedir):
    #print("0001#"+dir)
    if not os.path.exists(basedir + "\\" + dir):
        os.mkdir(basedir + "\\" + dir)

    # os.mkdir(basedir+"//"+dir)


def tes(ip, port, local_config_dir, remotefiles):
    #获取远程目录
    msg = SendMessage(ip, port, "0000")
    remotedirs = pickle.loads(msg)
    localdirs = GetDirectories.GetDirectories(local_config_dir, {})
    remotefiles = []
    if isinstance(remotedirs, dict):
        # print(remotedirs)
        # 新建空目录
        GetDictElement.GetDirsDictElement(remotedirs, createBlankDirs, local_config_dir)  # ("lambda x:print  ",  x))

        msg = SendMessage("127.0.0.1", 8000, "0001#")
        msg = pickle.loads(msg)

        remotefiles.extend(msg)

        print("remotefiles:  ", remotefiles, "  len=", len(remotefiles))


        for v in remotefiles:
            # msg = SendMessage("127.0.0.1", 8000, "0002#" + v.replace("\\", "**"))

            # print("v_to_un_*:  ",v)
            # print("v_to_un_*:  ",v)
            filepath = local_config_dir + "\\" + v.replace("\\", "*")
            if not os.path.isfile(filepath):
                print(filepath)
                GetFile('127.0.0.1', 8000, "0002#" + v.replace("\\", "*"), local_config_dir)
        # remotefiles = list(set(remotefiles))
        # print("list(set(remotefiles))    ", remotefiles,"  len=",len(remotefiles))

        # 获取文件

        # for k in remotedirs.keys():
        #     if isinstance(remotedirs[k], dict):
        #         print(remotedirs[k])

    # print(type(a))
    # print("a:::", a)
    # print(msg.decode('utf-8'))



def Client(ip, port, local_config_dir):
    print("初始化")
    ## 0000初始化
    #获取远程目录
    msg = SendMessage(ip, port, "0000")
    remotedirs = pickle.loads(msg)
    # 清空目录
    shutil.rmtree(local_config_dir)
    os.mkdir(local_config_dir)
    localdirs = GetDirectories.GetDirectories(local_config_dir, {})
    remotefiles = []
    if isinstance(remotedirs, dict):
        # print(remotedirs)
        # 新建空目录
        GetDictElement.GetDirsDictElement(remotedirs, createBlankDirs, local_config_dir)  # ("lambda x:print  ",  x))

        msg = SendMessage("127.0.0.1", 8000, "0001#")
        msg = pickle.loads(msg)

        remotefiles.extend(msg)

        print("remotefiles:  ", remotefiles, "  len=", len(remotefiles))
        for v in remotefiles:
            # msg = SendMessage("127.0.0.1", 8000, "0002#" + v.replace("\\", "**"))

            # print("v_to_un_*:  ",v)
            # print("v_to_un_*:  ",v)
            GetFile('127.0.0.1', 8000, "0002#" + v.replace("\\", "*"), local_config_dir)
    print("初始化完成！")
    time.sleep(20)
    # 远程文件存放路径
    #remotefiles = []
    ##初始化完成

    print("remotedirs:  ", remotedirs, "  localdirs:  ", localdirs)
    while True:
        msg = SendMessage(ip, port, "0000")
        remotedirs = pickle.loads(msg)
        start = time.time()
        print("同步开始！ ", start)
        tes(ip, port, local_config_dir, remotedirs)


        end = time.time()
        print("同步结束!", end)

        time.sleep(20)


Client("127.0.0.1", 8000, "d:\\test")