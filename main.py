
import sys
from PyQt5.QtWidgets import QApplication
from hand import Hand

def main():

    app = QApplication(sys.argv)#配置程序

    ui_hand=Hand()#实例化UI对象

    ui_hand.show_login()#显示UI登录窗口

    sys.exit(app.exec_())#开启程序


if __name__ == "__main__":
    main()
