import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QStackedWidget, QLabel
import psutil
import subprocess

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)
        self.init_main_page()
        self.init_waiting_page()

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        self.check_process()  # 初始时检查软件是否运行

    def init_main_page(self):
        main_page = QWidget(self)
        btn_check = QPushButton('检查软件是否运行', main_page)
        btn_check.clicked.connect(self.check_process)
        self.stacked_widget.addWidget(main_page)

    def init_waiting_page(self):
        waiting_page = QWidget(self)
        layout = QVBoxLayout(waiting_page)
        layout.addWidget(QLabel('正在启动，请稍候...'))
        self.stacked_widget.addWidget(waiting_page)

    def check_process(self):
        process_name = 'CgTeamWork.exe'  # 替换成你要检查的软件进程名

        # 切换到等待页面
        self.stacked_widget.setCurrentIndex(1)

        # 检查软件是否正在运行
        if self.is_process_running(process_name):
            QMessageBox.information(self, '提示', f'{process_name} 已经在运行！')
            self.stacked_widget.setCurrentIndex(0)  # 切换回主页面
        else:
            # 如果软件未运行，启动它
            try:
                subprocess.Popen([r'C:\CgTeamWork_v7\bin\cgtw\CgTeamWork.exe'])  # 替换成你的软件路径
                QMessageBox.information(self, '提示', f'{process_name} 启动成功！')
                self.stacked_widget.setCurrentIndex(0)  # 切换回主页面
            except Exception as e:
                QMessageBox.warning(self, '警告', f'启动失败：{e}')
                self.stacked_widget.setCurrentIndex(0)  # 启动失败时也切换回主页面

    def is_process_running(self, process_name):
        # 使用psutil检查进程是否正在运行
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                return True
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.setGeometry(300, 300, 300, 200)
    ex.setWindowTitle('软件检测与启动')
    ex.show()
    sys.exit(app.exec_())