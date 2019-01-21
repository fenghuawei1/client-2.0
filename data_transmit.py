
from PyQt5.QtCore import pyqtSignal, QObject, QThread

class Data_transmit(QThread):#继承Qthread线程类

    pressed = pyqtSignal()#设置信号槽

    def __init__(self,sockfd):#接收传入的socket

        super(Data_transmit,self).__init__()#重载QThread类
        self.client = sockfd
        self.pack = ''

#主进程将待发送的数据包发送给服务器

    def data_to_server(self,data_pack):
        self.text = data_pack
        self.client.send(self.text.encode())


#**********************子进程循环循环处理接收到的数据包******************

    def run(self):
        while True:
            recv_data = self.client.recv(1024)
            data = recv_data.decode().split('::')
            self.pack = data#接收到的数据
            self.pressed.emit()#关联给信号槽

