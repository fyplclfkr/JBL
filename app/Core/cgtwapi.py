# coding:utf-8
import sys
from datetime import datetime
# sys.path.append(r'c:/CgTeamWork_v7/bin/base')
import cgtw2

t_tw = cgtw2.tw()
username = t_tw.login.account()
userid = t_tw.login.account_id()


def get_project():
    """获取所有启用的项目"""
    field_sign_list = ['project.entity','project.full_name', 'project.id', 'project.database']
    filter_list = [['project.status', '=', 'Active']]
    id_list = t_tw.project.get_id(filter_list, limit="5000", start_num="")
    project_list = t_tw.project.get(id_list, field_sign_list, limit="5000", order_sign_list=[])
    return project_list


# print(get_project())

def get_my_task(db):
    """获取我的任务列表"""
    _module = ['asset','shot']
    _task_list = []
    for module in _module:
        if module == 'asset':
            field_sign_list = ['asset.entity', 'task.account', 'task.artist']
            filter_list = [['task.account', '=', username]]
            id_list = t_tw.task.get_id(
                db, module, filter_list, limit="5000", start_num="")
            task_list = t_tw.task.get(
                db, module, id_list, field_sign_list, limit="5000", order_sign_list=[])
            _task_list.extend(task_list)
        elif module == 'shot':
            field_sign_list = ['shot.entity', 'task.account', 'task.artist']
            filter_list = [['task.account', '=', username]]
            id_list = t_tw.task.get_id(db, module, filter_list, limit="5000", start_num="")
            task_list = t_tw.task.get(db, module, id_list, field_sign_list, limit="5000", order_sign_list=[])
            _task_list.extend(task_list)
    return _task_list


def get_daily_timelog(_date):
    """获取当前cgtw登录用户某天的工时,日期格式为:2024-01-09"""
    _time_log = []
    _project = get_project()
    for i in _project:
        db = i['project.database']
        field_list = ['date', 'tag', 'artist', 'project', 'link_entity']
        # field_list = t_tw.timelog.fields()
        # field_list.extend(['tag'])
        filter_list = [['account_id', '=', userid], ['date', '=', _date]]
        id_list = t_tw.timelog.get_id(db, filter_list, limit="5000")
        _time_log.extend(t_tw.timelog.get(
            db, id_list, field_list, limit="5000", order_list=[]))
    return _time_log
