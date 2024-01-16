# coding:utf-8
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication

from qfluentwidgets import FluentWindow, ScrollArea, SplashScreen
from qfluentwidgets import FluentIcon as FIF

from View.timelog_interface import TimeLogInterface


class MainWindow(FluentWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("mainWindow")
        self.move(400,100)
        self.initWindow()
        
        
        #添加子界面
        self.timelog_interface = TimeLogInterface()
        
        #将子界面添加到导航栏
        self.initNavigation()
        self.splashScreen.finish()
        
    def initNavigation(self):
        # 导航栏
        self.addSubInterface(self.timelog_interface, FIF.HISTORY, '工时打卡')
    
    def initWindow(self):
        # self.resize(1024, 768)
        #self.setMinimumWidth(760)
        self.setWindowIcon(QIcon('app/resource/images/logo.png'))
        self.setWindowTitle('嘉伯乐动画')
        
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()
        
    
    