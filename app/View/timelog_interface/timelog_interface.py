# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from ..UI.timelog import Ui_TimeLog


class TimeLogInterface(QWidget, Ui_TimeLog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)