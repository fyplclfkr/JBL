# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem , QAbstractScrollArea

from ..UI.timelog import Ui_TimeLog

from Core.cgtwapi import get_project, get_my_task
from common.thread.get_projects_thread import GetProjectsThread
from common.thread.get_tasks_thread import GetTasksThread


PROJECTS = get_project()

class TimeLogInterface(QWidget, Ui_TimeLog):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.get_project_thread = GetProjectsThread()
        self.get_project_thread.getProjectFinished.connect(self.initProject)
        self.get_project_thread.start()
        
        self.project_ListWidget.itemClicked.connect(self.get_tasks_thread)
        self.task_ListWidget.itemClicked.connect(lambda: print(self.task_ListWidget.currentItem().data(Qt.UserRole)))

    def initProject(self, project_list):
        self.project_ListWidget.clear()
        for project in project_list:
            print(project['project.full_name'])
            list_item = QListWidgetItem(project['project.full_name'])
            list_item.setData(Qt.UserRole, project)
            self.project_ListWidget.addItem(list_item)
            
    def initTask(self, task_list):
        self.task_ListWidget.clear()
        print(task_list)
        for task in task_list:
            entity_key = 'asset.entity' if 'asset.entity' in task else 'shot.entity'
            entity_value = task.get(entity_key, '')
            list_item = QListWidgetItem(entity_value)
            list_item.setData(Qt.UserRole, task)
            self.task_ListWidget.addItem(list_item)
            
    def initTaskInfo(self):
        pass
    
    def get_tasks_thread(self):
        db = self.project_ListWidget.currentItem().data(Qt.UserRole)['project.database']
        self.get_tasks_thread = GetTasksThread(db)
        self.get_tasks_thread.getTaskFinished.connect(self.initTask)
        self.get_tasks_thread.start()
        
    
    
            
            