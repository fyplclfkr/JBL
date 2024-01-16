from PyQt5.QtCore import QThread, pyqtSignal

class InitTimeButtonsThread(QThread):
    initTimeButtonsFinished = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        self.initTimeButtonsFinished.emit()