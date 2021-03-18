import socket

from tool.ReceivedMessage import ReceivedMessage


def Server(ip, port):
    ReceivedMessage(ip, port)


Server("127.0.0.1", 8000)
