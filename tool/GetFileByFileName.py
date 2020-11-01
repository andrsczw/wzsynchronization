import pickle
import socket

def GetFile(rip, rport, msg, localbasedir):
    """
    :param rip:  远程ip
    :param rport:  远程端口
    :param filename:  文件名称
    """
    # 初始化

    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rip, rport))
    if len(msg) != 0:
        # print("dsssfsf")

        filename = localbasedir + "\\" + msg.split("#")[1][1:]
        filename = filename.replace("*","\\")
        print(msg, localbasedir, filename)
        s.send(msg.encode('utf-8'))

        total_data = b''
        num = 0
        while True:
            data = s.recv(1024)
            total_data = total_data + data
            num = len(data)
            while len(data) > 0:
                data = s.recv(1024*1024)
                num = len(data) + num
                total_data = total_data + data
                #print("num=  ",num,"data=  ", data)
                #print("num=  ",num,"len(data)=  ", len(data))
            print("同步文件", filename)
            with open(filename, 'wb') as f:
                f.write(total_data)
                print("同步文件成功!  ", filename)
            return
        s.close()
