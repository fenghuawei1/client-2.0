
from PyQt5.QtWidgets import  QMainWindow
import socket
from data_transmit import Data_transmit


#此类用于处理UI界面
class Hand:

    def __init__(self):

        self.LoginWindow = QMainWindow()#配置登录窗口
        pass#此处初始化并配置登录UI界面

        self.main_window = QMainWindow()#配置主界面窗口
        pass

        self.hall_window = QMainWindow()#配置大厅窗口
        pass

    
        ...
        此处配置其他窗口
        ...

        #以下初始化socket,服务器连接和线程
        self.address = (())
        self.client = socket.socket()
        self.client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.connState = False#配置服务器连接状态为关闭
        self.threadState = False#配置线程开启状态为关闭

        self.th = Data_transmit(self.client) #实例化数据传输模块，传入socket参数



    def open_thread(self):#此函数启动子线程循环接收数据
        pass

    def parseData(self):#此函数接收并解析子线程从服务器传回的数据
        pass


    #以下为处理界面操作函数


    def show_login(self):#显示登录框
        pass

    def exit_login(self):#退出登录框
        pass

    def show_main(self):#显示主界面
        pass

    def exit_main(self):#退出主界面
        pass

    ...
    其他界面操作
    ...

    def look(self):
        pass

    def get_single_chat_data(self):#获取单聊输入数据
        pass
        
    def get_multi_chat_data(self):#获取群聊输入数据
        pass
    
    def send_to_server(self):#打包消息发送给服务器

        if self.tryConnServer():#尝试连接上服务器
            pass

    def tryConnServer(self):#连接服务器
        if not self.connectServer():
            pass

    def connectServer(self):#此函数连接服务器
        pass

    


    
