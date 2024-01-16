# coding:utf-8
import os
import sys
import subprocess
import psutil

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

# 创建APP
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)


def is_process_running(process_name):
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                return True
        return False

#启动CgTeamWork    
if is_process_running("CgTeamWork.exe"):
    from View.main_window import MainWindow
    w = MainWindow()
    w.show()
else:
    try:
        subprocess.Popen([r'C:\CgTeamWork_v7\bin\cgtw\CgTeamWork.exe'])
        from View.main_window import MainWindow
        w = MainWindow()
        w.show()
    except Exception as e:
        print(e)
        
        

app.exec_()