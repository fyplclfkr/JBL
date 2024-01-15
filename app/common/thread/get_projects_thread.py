# coding: utf-8

from PyQt5.QtCore import QThread, pyqtSignal

from Core.cgtwapi import get_project


class GetProjectsThread(QThread):
    getProjectFinished = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
        
    def run(self):
        project_list = get_project()
        self.getProjectFinished.emit(project_list)
