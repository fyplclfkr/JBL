# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\works\JBL\app\View\UI\timelog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimeLog(object):
    def setupUi(self, TimeLog):
        TimeLog.setObjectName("TimeLog")
        TimeLog.resize(1024, 768)
        TimeLog.setMinimumSize(QtCore.QSize(860, 0))
        TimeLog.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(TimeLog)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(TimeLog)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(326, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.SubtitleLabel = SubtitleLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubtitleLabel.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel.setSizePolicy(sizePolicy)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.verticalLayout_10.addWidget(self.SubtitleLabel)
        self.verticalLayout.addWidget(self.frame_8)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.task_ListWidget = ListWidget(self.frame)
        self.task_ListWidget.setStyleSheet("ListView,\n"
"ListWidget {\n"
"    background: transparent;\n"
"    outline: none;\n"
"    border: none;\n"
"    /* font: 13px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    selection-background-color: transparent;\n"
"    alternate-background-color: transparent;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    background-color: rgb(249, 249, 249);\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"}\n"
"\n"
"ListView::item,\n"
"ListWidget::item {\n"
"    background: transparent;\n"
"    border: 0px;\n"
"    padding-left: 11px;\n"
"    padding-right: 11px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"ListView::indicator,\n"
"ListWidget::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 0.48);\n"
"    background-color: rgba(0, 0, 0, 0.022);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"ListView::indicator:hover,\n"
"ListWidget::indicator:hover {\n"
"    border: 1px solid rgba(0, 0, 0, 0.56);\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"}\n"
"\n"
"ListView::indicator:pressed,\n"
"ListWidget::indicator:pressed {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: rgba(0, 0, 0, 0.12);\n"
"}\n"
"\n"
"ListView::indicator:checke,\n"
"ListWidget::indicator:checked,\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    border: 1px solid #009faa;\n"
"    background-color: #009faa;\n"
"}\n"
"\n"
"ListView::indicator:checked,\n"
"ListWidget::indicator:checked {\n"
"    image: url(:/qfluentwidgets/images/check_box/Accept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    image: url(:/qfluentwidgets/images/check_box/PartialAccept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:checked:hove,\n"
"ListWidget::indicator:checked:hover,\n"
"ListView::indicator:indeterminate:hover,\n"
"ListWidget::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a7b3;\n"
"    background-color: #00a7b3;\n"
"}\n"
"\n"
"ListView::indicator:checked:presse,\n"
"ListWidget::indicator:checked:pressed,\n"
"ListView::indicator:indeterminate:pressed,\n"
"ListWidget::indicator:indeterminate:pressed {\n"
"    border: 1px solid #3eabb3;\n"
"    background-color: #3eabb3;\n"
"}\n"
"\n"
"ListView::indicator:disabled,\n"
"ListWidget::indicator:disabled {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"ListView::indicator:checked:disable,\n"
"ListWidget::indicator:checked:disabled,\n"
"ListView::indicator:indeterminate:disabled,\n"
"ListWidget::indicator:indeterminate:disabled {\n"
"    border: 1px solid rgb(199, 199, 199);\n"
"    background-color: rgb(199, 199, 199);\n"
"}")
        self.task_ListWidget.setObjectName("task_ListWidget")
        self.gridLayout.addWidget(self.task_ListWidget, 1, 1, 1, 1)
        self.project_ListWidget = ListWidget(self.frame)
        self.project_ListWidget.setStyleSheet("ListView,\n"
"ListWidget {\n"
"    background: transparent;\n"
"    outline: none;\n"
"    border: none;\n"
"    /* font: 13px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    selection-background-color: transparent;\n"
"    alternate-background-color: transparent;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    background-color: rgb(249, 249, 249);\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"\n"
"\n"
"}\n"
"\n"
"ListView::item,\n"
"ListWidget::item {\n"
"    background: transparent;\n"
"    border: 0px;\n"
"    padding-left: 11px;\n"
"    padding-right: 11px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"ListView::indicator,\n"
"ListWidget::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 0.48);\n"
"    background-color: rgba(0, 0, 0, 0.022);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"ListView::indicator:hover,\n"
"ListWidget::indicator:hover {\n"
"    border: 1px solid rgba(0, 0, 0, 0.56);\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"}\n"
"\n"
"ListView::indicator:pressed,\n"
"ListWidget::indicator:pressed {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: rgba(0, 0, 0, 0.12);\n"
"}\n"
"\n"
"ListView::indicator:checke,\n"
"ListWidget::indicator:checked,\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    border: 1px solid #009faa;\n"
"    background-color: #009faa;\n"
"}\n"
"\n"
"ListView::indicator:checked,\n"
"ListWidget::indicator:checked {\n"
"    image: url(:/qfluentwidgets/images/check_box/Accept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    image: url(:/qfluentwidgets/images/check_box/PartialAccept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:checked:hove,\n"
"ListWidget::indicator:checked:hover,\n"
"ListView::indicator:indeterminate:hover,\n"
"ListWidget::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a7b3;\n"
"    background-color: #00a7b3;\n"
"}\n"
"\n"
"ListView::indicator:checked:presse,\n"
"ListWidget::indicator:checked:pressed,\n"
"ListView::indicator:indeterminate:pressed,\n"
"ListWidget::indicator:indeterminate:pressed {\n"
"    border: 1px solid #3eabb3;\n"
"    background-color: #3eabb3;\n"
"}\n"
"\n"
"ListView::indicator:disabled,\n"
"ListWidget::indicator:disabled {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"ListView::indicator:checked:disable,\n"
"ListWidget::indicator:checked:disabled,\n"
"ListView::indicator:indeterminate:disabled,\n"
"ListWidget::indicator:indeterminate:disabled {\n"
"    border: 1px solid rgb(199, 199, 199);\n"
"    background-color: rgb(199, 199, 199);\n"
"}")
        self.project_ListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.project_ListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.project_ListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.project_ListWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.project_ListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.project_ListWidget.setObjectName("project_ListWidget")
        item = QtWidgets.QListWidgetItem()
        self.project_ListWidget.addItem(item)
        self.gridLayout.addWidget(self.project_ListWidget, 1, 0, 1, 1)
        self.BodyLabel = BodyLabel(self.frame)
        self.BodyLabel.setMinimumSize(QtCore.QSize(0, 28))
        self.BodyLabel.setMaximumSize(QtCore.QSize(16777215, 28))
        self.BodyLabel.setStyleSheet("background-color: rgba(51, 51, 51, 0.1);")
        self.BodyLabel.setProperty("pixelFontSize", 15)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridLayout.addWidget(self.BodyLabel, 0, 0, 1, 1)
        self.BodyLabel_2 = BodyLabel(self.frame)
        self.BodyLabel_2.setMinimumSize(QtCore.QSize(0, 28))
        self.BodyLabel_2.setMaximumSize(QtCore.QSize(16777215, 28))
        self.BodyLabel_2.setStyleSheet("background-color: rgba(51, 51, 51, 0.1);")
        self.BodyLabel_2.setProperty("pixelFontSize", 15)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.gridLayout.addWidget(self.BodyLabel_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(TimeLog)
        self.line.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(TimeLog)
        self.frame_2.setMinimumSize(QtCore.QSize(272, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(272, 16777215))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SubtitleLabel_2 = SubtitleLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubtitleLabel_2.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_2.setSizePolicy(sizePolicy)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.verticalLayout_4.addWidget(self.SubtitleLabel_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.info_projectname_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_projectname_label.setFont(font)
        self.info_projectname_label.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.info_projectname_label.setObjectName("info_projectname_label")
        self.horizontalLayout_2.addWidget(self.info_projectname_label)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.info_taskname_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_taskname_label.setFont(font)
        self.info_taskname_label.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.info_taskname_label.setObjectName("info_taskname_label")
        self.horizontalLayout_3.addWidget(self.info_taskname_label)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.info_taskstatu_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_taskstatu_label.setFont(font)
        self.info_taskstatu_label.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.info_taskstatu_label.setObjectName("info_taskstatu_label")
        self.horizontalLayout_4.addWidget(self.info_taskstatu_label)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.info_expectedtime_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_expectedtime_label.setFont(font)
        self.info_expectedtime_label.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.info_expectedtime_label.setObjectName("info_expectedtime_label")
        self.horizontalLayout_5.addWidget(self.info_expectedtime_label)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.info_usetime_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_usetime_label.setFont(font)
        self.info_usetime_label.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.info_usetime_label.setObjectName("info_usetime_label")
        self.horizontalLayout_6.addWidget(self.info_usetime_label)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_7.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_7.addWidget(self.label_23)
        self.info_residuetime_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_residuetime_label.setFont(font)
        self.info_residuetime_label.setStyleSheet("color:rgba(51, 51, 51, 0.5)")
        self.info_residuetime_label.setObjectName("info_residuetime_label")
        self.horizontalLayout_7.addWidget(self.info_residuetime_label)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.SubtitleLabel_3 = SubtitleLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubtitleLabel_3.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_3.setSizePolicy(sizePolicy)
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")
        self.verticalLayout_7.addWidget(self.SubtitleLabel_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.StrongBodyLabel = StrongBodyLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StrongBodyLabel.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel.setSizePolicy(sizePolicy)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.verticalLayout_5.addWidget(self.StrongBodyLabel)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PillPushButton = PillPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton.sizePolicy().hasHeightForWidth())
        self.PillPushButton.setSizePolicy(sizePolicy)
        self.PillPushButton.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton.setObjectName("PillPushButton")
        self.buttonGroup = QtWidgets.QButtonGroup(TimeLog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.PillPushButton)
        self.gridLayout_2.addWidget(self.PillPushButton, 0, 0, 1, 1)
        self.PillPushButton_2 = PillPushButton(self.frame_6)
        self.PillPushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton_2.sizePolicy().hasHeightForWidth())
        self.PillPushButton_2.setSizePolicy(sizePolicy)
        self.PillPushButton_2.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_2.setObjectName("PillPushButton_2")
        self.buttonGroup.addButton(self.PillPushButton_2)
        self.gridLayout_2.addWidget(self.PillPushButton_2, 0, 1, 1, 1)
        self.PillPushButton_3 = PillPushButton(self.frame_6)
        self.PillPushButton_3.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_3.setObjectName("PillPushButton_3")
        self.buttonGroup.addButton(self.PillPushButton_3)
        self.gridLayout_2.addWidget(self.PillPushButton_3, 1, 0, 1, 1)
        self.PillPushButton_4 = PillPushButton(self.frame_6)
        self.PillPushButton_4.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_4.setObjectName("PillPushButton_4")
        self.buttonGroup.addButton(self.PillPushButton_4)
        self.gridLayout_2.addWidget(self.PillPushButton_4, 1, 1, 1, 1)
        self.PillPushButton_5 = PillPushButton(self.frame_6)
        self.PillPushButton_5.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_5.setObjectName("PillPushButton_5")
        self.buttonGroup.addButton(self.PillPushButton_5)
        self.gridLayout_2.addWidget(self.PillPushButton_5, 2, 0, 1, 1)
        self.PillPushButton_6 = PillPushButton(self.frame_6)
        self.PillPushButton_6.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_6.setObjectName("PillPushButton_6")
        self.buttonGroup.addButton(self.PillPushButton_6)
        self.gridLayout_2.addWidget(self.PillPushButton_6, 2, 1, 1, 1)
        self.PillPushButton_7 = PillPushButton(self.frame_6)
        self.PillPushButton_7.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_7.setObjectName("PillPushButton_7")
        self.buttonGroup.addButton(self.PillPushButton_7)
        self.gridLayout_2.addWidget(self.PillPushButton_7, 3, 0, 1, 1)
        self.PillPushButton_8 = PillPushButton(self.frame_6)
        self.PillPushButton_8.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_8.setObjectName("PillPushButton_8")
        self.buttonGroup.addButton(self.PillPushButton_8)
        self.gridLayout_2.addWidget(self.PillPushButton_8, 3, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_2.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_2.setSizePolicy(sizePolicy)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.verticalLayout_6.addWidget(self.StrongBodyLabel_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PillPushButton_9 = PillPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton_9.sizePolicy().hasHeightForWidth())
        self.PillPushButton_9.setSizePolicy(sizePolicy)
        self.PillPushButton_9.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_9.setObjectName("PillPushButton_9")
        self.buttonGroup.addButton(self.PillPushButton_9)
        self.gridLayout_3.addWidget(self.PillPushButton_9, 0, 0, 1, 1)
        self.PillPushButton_10 = PillPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton_10.sizePolicy().hasHeightForWidth())
        self.PillPushButton_10.setSizePolicy(sizePolicy)
        self.PillPushButton_10.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_10.setObjectName("PillPushButton_10")
        self.buttonGroup.addButton(self.PillPushButton_10)
        self.gridLayout_3.addWidget(self.PillPushButton_10, 0, 1, 1, 1)
        self.PillPushButton_11 = PillPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton_11.sizePolicy().hasHeightForWidth())
        self.PillPushButton_11.setSizePolicy(sizePolicy)
        self.PillPushButton_11.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_11.setObjectName("PillPushButton_11")
        self.buttonGroup.addButton(self.PillPushButton_11)
        self.gridLayout_3.addWidget(self.PillPushButton_11, 1, 0, 1, 1)
        self.PillPushButton_12 = PillPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton_12.sizePolicy().hasHeightForWidth())
        self.PillPushButton_12.setSizePolicy(sizePolicy)
        self.PillPushButton_12.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_12.setObjectName("PillPushButton_12")
        self.buttonGroup.addButton(self.PillPushButton_12)
        self.gridLayout_3.addWidget(self.PillPushButton_12, 1, 1, 1, 1)
        self.PillPushButton_13 = PillPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton_13.sizePolicy().hasHeightForWidth())
        self.PillPushButton_13.setSizePolicy(sizePolicy)
        self.PillPushButton_13.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_13.setObjectName("PillPushButton_13")
        self.buttonGroup.addButton(self.PillPushButton_13)
        self.gridLayout_3.addWidget(self.PillPushButton_13, 2, 0, 1, 1)
        self.PillPushButton_14 = PillPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PillPushButton_14.sizePolicy().hasHeightForWidth())
        self.PillPushButton_14.setSizePolicy(sizePolicy)
        self.PillPushButton_14.setMinimumSize(QtCore.QSize(96, 29))
        self.PillPushButton_14.setObjectName("PillPushButton_14")
        self.buttonGroup.addButton(self.PillPushButton_14)
        self.gridLayout_3.addWidget(self.PillPushButton_14, 2, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.PrimaryPushButton = PrimaryPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrimaryPushButton.sizePolicy().hasHeightForWidth())
        self.PrimaryPushButton.setSizePolicy(sizePolicy)
        self.PrimaryPushButton.setMinimumSize(QtCore.QSize(158, 40))
        self.PrimaryPushButton.setIconSize(QtCore.QSize(16, 16))
        self.PrimaryPushButton.setProperty("hasIcon", False)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.horizontalLayout_8.addWidget(self.PrimaryPushButton)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.verticalLayout_8.addWidget(self.frame_6)
        self.verticalLayout_8.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.line_2 = QtWidgets.QFrame(TimeLog)
        self.line_2.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.frame_3 = QtWidgets.QFrame(TimeLog)
        self.frame_3.setMinimumSize(QtCore.QSize(304, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(304, 16777215))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setContentsMargins(-1, 9, 9, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SubtitleLabel_4 = SubtitleLabel(self.frame_7)
        self.SubtitleLabel_4.setObjectName("SubtitleLabel_4")
        self.verticalLayout_2.addWidget(self.SubtitleLabel_4)
        self.label = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/images/working.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_9.addWidget(self.frame_7)
        self.SegmentedWidget = SegmentedWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SegmentedWidget.sizePolicy().hasHeightForWidth())
        self.SegmentedWidget.setSizePolicy(sizePolicy)
        self.SegmentedWidget.setObjectName("SegmentedWidget")
        self.verticalLayout_9.addWidget(self.SegmentedWidget)
        self.verticalLayout_9.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.frame_3)

        self.retranslateUi(TimeLog)
        QtCore.QMetaObject.connectSlotsByName(TimeLog)

    def retranslateUi(self, TimeLog):
        _translate = QtCore.QCoreApplication.translate
        TimeLog.setWindowTitle(_translate("TimeLog", "Form"))
        self.SubtitleLabel.setText(_translate("TimeLog", "选择打卡任务"))
        self.project_ListWidget.setSortingEnabled(False)
        __sortingEnabled = self.project_ListWidget.isSortingEnabled()
        self.project_ListWidget.setSortingEnabled(False)
        item = self.project_ListWidget.item(0)
        item.setText(_translate("TimeLog", "新建项目"))
        self.project_ListWidget.setSortingEnabled(__sortingEnabled)
        self.BodyLabel.setText(_translate("TimeLog", "    项目列表"))
        self.BodyLabel_2.setText(_translate("TimeLog", "    任务列表"))
        self.SubtitleLabel_2.setText(_translate("TimeLog", "当前任务信息"))
        self.label_4.setText(_translate("TimeLog", "项目名称"))
        self.label_5.setText(_translate("TimeLog", "｜"))
        self.info_projectname_label.setText(_translate("TimeLog", " "))
        self.label_7.setText(_translate("TimeLog", "任务名称"))
        self.label_8.setText(_translate("TimeLog", "｜"))
        self.info_taskname_label.setText(_translate("TimeLog", " "))
        self.label_10.setText(_translate("TimeLog", "任务状态"))
        self.label_11.setText(_translate("TimeLog", "｜"))
        self.info_taskstatu_label.setText(_translate("TimeLog", " "))
        self.label_13.setText(_translate("TimeLog", "预计工时"))
        self.label_14.setText(_translate("TimeLog", "｜"))
        self.info_expectedtime_label.setText(_translate("TimeLog", " "))
        self.label_16.setText(_translate("TimeLog", "已用工时"))
        self.label_17.setText(_translate("TimeLog", "｜"))
        self.info_usetime_label.setText(_translate("TimeLog", " "))
        self.label_22.setText(_translate("TimeLog", "剩余工时"))
        self.label_23.setText(_translate("TimeLog", "｜"))
        self.info_residuetime_label.setText(_translate("TimeLog", " "))
        self.SubtitleLabel_3.setText(_translate("TimeLog", "请选择打卡时间"))
        self.StrongBodyLabel.setText(_translate("TimeLog", "工作时间"))
        self.PillPushButton.setText(_translate("TimeLog", "09:30-10:30"))
        self.PillPushButton_2.setText(_translate("TimeLog", "10:30-11:30"))
        self.PillPushButton_3.setText(_translate("TimeLog", "11:30-13:30"))
        self.PillPushButton_4.setText(_translate("TimeLog", "13:30-14:30"))
        self.PillPushButton_5.setText(_translate("TimeLog", "14:30-15:30"))
        self.PillPushButton_6.setText(_translate("TimeLog", "15:30-16:30"))
        self.PillPushButton_7.setText(_translate("TimeLog", "16:30-17:30"))
        self.PillPushButton_8.setText(_translate("TimeLog", "17:30-18:30"))
        self.StrongBodyLabel_2.setText(_translate("TimeLog", "加班时间"))
        self.PillPushButton_9.setText(_translate("TimeLog", "18:30-19:30"))
        self.PillPushButton_10.setText(_translate("TimeLog", "19:30-20:30"))
        self.PillPushButton_11.setText(_translate("TimeLog", "20:30-21:30"))
        self.PillPushButton_12.setText(_translate("TimeLog", "21:30-22:30"))
        self.PillPushButton_13.setText(_translate("TimeLog", "22:30-23:30"))
        self.PillPushButton_14.setText(_translate("TimeLog", "23:30-0:30"))
        self.PrimaryPushButton.setText(_translate("TimeLog", "确认打卡"))
        self.SubtitleLabel_4.setText(_translate("TimeLog", "打卡记录"))
from qfluentwidgets import BodyLabel, ListWidget, PillPushButton, PrimaryPushButton, SegmentedWidget, StrongBodyLabel, SubtitleLabel
from . import resource_rc
