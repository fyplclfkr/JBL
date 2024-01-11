# coding:utf-8

import sys
sys.path.append('./')

import cgtw2
t_tw = cgtw2.tw()

from app.Core import cgtwapi


"""获取项目信息"""
# print(cgtwapi.get_project())
# [{'project.entity': 'AQT_Anniversary', 'project.full_name': '暗区突围-一周年', 'project.id': 'DF9B11DC-8CAF-4B89-8992-678562B28DAF', 'project.database': 'proj_aqt_anniversary', 'id': 'DF9B11DC-8CAF-4B89-8992-678562B28DAF'}, 
#  {'project.entity': 'Project_Z', 'project.full_name': 'Project_Z', 'project.id': '6BCE39CF-4323-4103-BCB3-6F33B3124766', 'project.database': 'proj_project_z', 'id': '6BCE39CF-4323-4103-BCB3-6F33B3124766'}, 
#  {'project.entity': 'AQT_TRN', 'project.full_name': '暗区TRN', 'project.id': 'FFD7F738-8EC5-4555-9BC7-5C17B3D84B0A', 'project.database': 'proj_aqt_trn', 'id': 'FFD7F738-8EC5-4555-9BC7-5C17B3D84B0A'}, 
#  {'project.entity': 'test3', 'project.full_name': 'test3', 'project.id': '11036D88-01EB-4712-937A-4A5679ECFB3A', 'project.database': 'proj_test3', 'id': '11036D88-01EB-4712-937A-4A5679ECFB3A'},
#  {'project.entity': 'SV', 'project.full_name': 'SVGame_360-凌空对决', 'project.id': 'F8C9397F-CA4E-4D54-8052-052208E03933', 'project.database': 'proj_sv', 'id': 'F8C9397F-CA4E-4D54-8052-052208E03933'}, 
#  {'project.entity': 'TEST', 'project.full_name': 'TEST', 'project.id': '748E64B9-BD82-4FC1-B651-B2B82400BD5A', 'project.database': 'proj_test', 'id': '748E64B9-BD82-4FC1-B651-B2B82400BD5A'}, 
#  {'project.entity': 'AQT_Borrero', 'project.full_name': '暗区博雷罗', 'project.id': '77CEF7A1-FB34-4E9F-BEDE-74CB995C371E', 'project.database': 'proj_aqt_borrero', 'id': '77CEF7A1-FB34-4E9F-BEDE-74CB995C371E'}, 
#  {'project.entity': 'TEST2', 'project.full_name': 'TEST2', 'project.id': '980DB891-73DD-4205-A396-A4E0782C4E96', 'project.database': 'proj_test2', 'id': '980DB891-73DD-4205-A396-A4E0782C4E96'}]

"""获取任务信息"""
# print(cgtwapi.get_my_task(db='proj_test'))
# [{'asset.entity': 'Borrero', 'task.account': 'yuping.fan', 'task.artist': '范毓平', 'id': '4902F7B4-52F8-F6D5-ADA0-314CD416F99E'}, 
#  {'shot.entity': 'Sc01', 'task.account': 'yuping.fan', 'task.artist': '范毓平', 'id': '5E3AB1CD-F678-48B7-E7F1-1D6294B6822A'}]

"""获取工时信息"""
# print(cgtwapi.get_daily_timelog('2024-01-09'))
# [{'date': '2024-01-09', 'tag': '16:30-17:30', 'artist': '范毓平', 'project': 'TEST', 'link_entity': 'Sc01/Layout', '#id': 'AA3F3253-C436-C585-F0A2-2F9FF2C0A651'}, 
#  {'date': '2024-01-09', 'tag': '14:30-15:30', 'artist': '范毓平', 'project': 'TEST', 'link_entity': 'Sc01/Layout', '#id': '7257EC80-715F-6890-5D58-99D858215D3A'}]