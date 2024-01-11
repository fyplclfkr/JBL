# coding:utf-8
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from View.main_window import MainWindow

# 创建APP
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

# 创建主窗体
w = MainWindow()
w.show()

app.exec_()