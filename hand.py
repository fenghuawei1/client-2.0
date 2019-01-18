
from PyQt5.QtWidgets import  QMainWindow
import socket
from data_transmit import Data_transmit


#此类用于处理UI界面
class Hand:

    def __init__(self):

        #初始化socket,服务器连接和线程

        self.address = (())
        self.client = socket.socket()
        self.client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.connState = False#配置服务器连接状态为关闭
        self.threadState = False#配置线程开启状态为关闭

        self.th = Data_transmit(self.client) #实例化数据传输模块，传入socket参数


#**************************第一部分：配置各种界面*****************************

    
        
        self.LoginWindow = QMainWindow()#配置登录窗口
        pass

        self.main_window = QMainWindow()#配置主界面窗口
        pass

        self.hall_window = QMainWindow()#配置大厅窗口
        pass

    

#***********************第二部分：获取客户端信息，发送给服务器********************


    def get_single_chat_data(self):#获取单聊输入数据
        pass
        
    def get_multi_chat_data(self):#获取群聊输入数据
        pass


    #发送给服务器
    
    def send_to_server(self):

        if self.tryConnServer():#尝试连接上服务器
            pass

    def tryConnServer(self):#连接服务器
        if not self.connectServer():
            pass

    def connectServer(self):#此函数连接服务器
        pass

    def open_thread(self):#此函数启动子线程循环接收数据
        pass

    
#******************第三部分：接收从子线程传回的数据，并解析******************


    def parseData(self):#接收数据，分发给解析函数
        pass

    
    #以下函数解析收到的数据


    def show_login(self):#显示登录框
        pass

    def exit_login(self):#退出登录框
        pass

    def show_main(self):#显示主界面
        pass

    def exit_main(self):#退出主界面
        pass



    
