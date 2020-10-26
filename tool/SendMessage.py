import pickle
import socket

def SendMessage(rip, rport, msg):
    """
    :param rip:  远程ip
    :param rport:  远程端口
    :param msg:  发送消息
    """
    #创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rip, rport))
    if len(msg) != 0:
        #print("dsssfsf")
        s.send(msg.encode('utf-8'))
        msg = s.recv(1024)
        a = pickle.loads(msg)
        print(type(a))
        print("a:::",a)
        #print(msg.decode('utf-8'))
        s.close()
