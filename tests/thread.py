import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget
from PyQt5.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    finished_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        # 模拟获取数据的耗时操作
        import time
        time.sleep(5)

        # 模拟获取的数据
        data = ["Item 1", "Item 2", "Item 3"]
        self.finished_signal.emit(data)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # 创建并启动线程
        self.thread = WorkerThread()
        self.thread.finished_signal.connect(self.on_thread_finished)
        self.thread.start()

        self.setLayout(layout)
        self.setWindowTitle("线程获取数据示例")

    def on_thread_finished(self, data):
        # 在线程完成时更新 QListWidget
        self.list_widget.clear()
        self.list_widget.addItems(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
