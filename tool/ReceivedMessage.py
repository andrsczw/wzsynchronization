import socket
def ReceivedMessage(ip, port):
    s = socket.socket()
    s.bind(ip, port)
    s.listen()
    while True:
        #每当接收到客户端socket的请求时，该方法就返回对应的socket和远程地址
        c, addr = s.accept()
        print(c)
        print('连接地址：', addr)
        c.send('您好，您收到了服务器的回复'.encode('utf-8'))
        c.close()