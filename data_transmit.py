
from PyQt5.QtCore import pyqtSignal, QObject, QThread

class Data_transmit(QThread):#继承Qthread线程类

    pressed=pyqtSignal()#设置信号槽

    def __init__(self,sockfd):#接收传入的socket

        super(Data_transmit,self).__init__()#重载QThread类
        self.client=sockfd
        self.msg=''

    def run(self):#子线程用来循环处理接收到的数据包
        while True:
            recv_data=self.client.recv(1024)
            data=recv_data.decode().split('::')
            self.msg=data#接收到的数据
            self.pressed.emit()#关联给信号槽

    def data_to_server(self,data_pack):#将待发送的数据包发送给服务器
        self.text=data_pack
        self.client.send(self.text.encode())