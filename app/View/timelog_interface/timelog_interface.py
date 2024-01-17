# coding:utf-8
import sys
import time

from datetime import date, timedelta

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem , QAbstractScrollArea

from ..UI.timelog import Ui_TimeLog

from Core.cgtwapi import get_project, get_my_task, get_daily_timelog

from common.thread.get_projects_thread import GetProjectsThread
from common.thread.get_tasks_thread import GetTasksThread
from common.thread.get_daily_timelog_thread import GetDailyTimelogThread

_today = date.today()
_yesterday = _today - timedelta(days=1)
_before_yesterday = _today - timedelta(days=2)
_today = _today.strftime('%Y-%m-%d')
_yesterday.strftime('%Y-%m-%d')
_before_yesterday.strftime('%Y-%m-%d')

class TimeLogInterface(QWidget, Ui_TimeLog):

    def __init__(self):
        super().__init__()
        start_time = time.time()  # 记录窗口加载开始时间

        
        self.setupUi(self)
        
        
        self.get_project_thread = GetProjectsThread()
        self.get_project_thread.getProjectFinished.connect(self.initProject)
        self.get_project_thread.start()
        
        self.project_ListWidget.itemClicked.connect(self.get_tasks_thread)
        self.task_ListWidget.itemClicked.connect(self.setTaskInfo)
        
        self.get_timelog_thread()
        
        end_time = time.time()  # 记录窗口加载结束时间
        # 输出加载时间
        print(f'Window loaded in {end_time - start_time:.4f} seconds')

    def initProject(self, project_list):
        self.project_ListWidget.clear()
        for project in project_list:
            # print(project['project.full_name'])
            list_item = QListWidgetItem(project['project.full_name'])
            list_item.setData(Qt.UserRole, project)
            self.project_ListWidget.addItem(list_item)
            
    def initTask(self, task_list):
        self.task_ListWidget.clear()
        # print(task_list)
        for task in task_list:
            entity_key = 'asset.entity' if 'asset.entity' in task else 'shot.entity'
            entity_value = task.get(entity_key, '')
            list_item = QListWidgetItem(entity_value)
            list_item.setData(Qt.UserRole, task)
            self.task_ListWidget.addItem(list_item)
            
    def setTaskInfo(self):
        self.info_projectname_label.setText(self.project_ListWidget.currentItem().text())
        self.info_taskname_label.setText(self.task_ListWidget.currentItem().data(Qt.UserRole)['task.url'])
        self.info_taskstatu_label.setText(self.task_ListWidget.currentItem().data(Qt.UserRole)['task.status'])
        self.info_expectedtime_label.setText(self.task_ListWidget.currentItem().data(Qt.UserRole)['task.expected_time'])
        self.info_usetime_label.setText(self.task_ListWidget.currentItem().data(Qt.UserRole)['task.total_use_time'])
        self.info_residuetime_label.setText('')
        
    def initTimeButton(self,timelog_list):
        for timelog in timelog_list:
            for button in self.buttonGroup.buttons():
                if timelog['tag'] == button.text():
                    button.setEnabled(False)
        
        
        
    def get_tasks_thread(self):
        db = self.project_ListWidget.currentItem().data(Qt.UserRole)['project.database']
        self.get_tasks_thread = GetTasksThread(db)
        self.get_tasks_thread.getTaskFinished.connect(self.initTask)
        self.get_tasks_thread.start()
        
    def get_timelog_thread(self):
        _data = '2024-01-15'
        self.get_timelog_thread = GetDailyTimelogThread(_data)
        self.get_timelog_thread.getTimelogFinished.connect(self.initTimeButton)
        self.get_timelog_thread.start()

    def set_timelog(self):
        pass
    
    def init_submitted_timelog(self):
        self.SegmentedWidget
        pass

        
    
    
            
            