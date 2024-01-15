import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

class MyTrayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tray Application')
        self.setGeometry(100, 100, 400, 300)

        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('app/resource/images/logo.png'))

        # 创建系统托盘菜单
        tray_menu = QMenu(self)
        restore_action = QAction('Restore', self)
        minimize_action = QAction('Minimize', self)
        quit_action = QAction('Quit', self)

        restore_action.triggered.connect(self.showNormal)
        minimize_action.triggered.connect(self.hide)
        quit_action.triggered.connect(self.close)

        tray_menu.addAction(restore_action)
        tray_menu.addAction(minimize_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        # 显示系统托盘图标
        self.tray_icon.show()

    def closeEvent(self, event):
        # 隐藏窗口而不是关闭应用程序，以便在系统托盘中保留图标
        self.hide()
        event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyTrayApp()
    sys.exit(app.exec_())
