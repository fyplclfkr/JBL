# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem

from ..UI.timelog import Ui_TimeLog

from Core.cgtwapi import *

PROJECTS = get_project()

class TimeLogInterface(QWidget, Ui_TimeLog):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.initProject()
        
        self.project_ListWidget.itemClicked.connect(self.initTask)
        self.task_ListWidget.itemClicked.connect(lambda: print(self.task_ListWidget.currentItem().data(1)))

    def initProject(self):
        for project in PROJECTS:
            list_item = QListWidgetItem(project['project.full_name'])
            list_item.setData(1, project)
            self.project_ListWidget.addItem(list_item)
            
    def initTask(self):
        self.task_ListWidget.clear()
        
        db = self.project_ListWidget.currentItem().data(1)['project.database']
        tasks= get_my_task(db)
        print(tasks)
        for task in tasks:
            entity_key = 'asset.entity' if 'asset.entity' in task else 'shot.entity'
            entity_value = task.get(entity_key, '')
            list_item = QListWidgetItem(entity_value)
            list_item.setData(1, task)
            self.task_ListWidget.addItem(list_item)
    
            
            