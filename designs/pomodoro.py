# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pomodoro.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(800, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.le_interruption = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_interruption.setObjectName("le_interruption")
        self.gridLayout.addWidget(self.le_interruption, 1, 1, 1, 1)
        self.pb_remaining = QtWidgets.QProgressBar(self.groupBox_2)
        self.pb_remaining.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: #3add36;\n"
"     width: 1px;\n"
" }\n"
"\n"
" QProgressBar {\n"
"     border: 1px solid grey;\n"
"     border-radius: 0px;\n"
"     text-align: center;\n"
" }")
        self.pb_remaining.setProperty("value", 24)
        self.pb_remaining.setObjectName("pb_remaining")
        self.gridLayout.addWidget(self.pb_remaining, 1, 0, 1, 1)
        self.lbl_status = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_status.setObjectName("lbl_status")
        self.gridLayout.addWidget(self.lbl_status, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(800, 80))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sb_number_of_poms = QtWidgets.QSpinBox(self.groupBox)
        self.sb_number_of_poms.setObjectName("sb_number_of_poms")
        self.gridLayout_3.addWidget(self.sb_number_of_poms, 0, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.cb_task = QtWidgets.QComboBox(self.groupBox)
        self.cb_task.setObjectName("cb_task")
        self.gridLayout_3.addWidget(self.cb_task, 0, 4, 1, 1)
        self.btn_go = QtWidgets.QPushButton(self.groupBox)
        self.btn_go.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_go.setObjectName("btn_go")
        self.gridLayout_3.addWidget(self.btn_go, 0, 7, 1, 1)
        self.cb_project = QtWidgets.QComboBox(self.groupBox)
        self.cb_project.setObjectName("cb_project")
        self.gridLayout_3.addWidget(self.cb_project, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 5, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(800, 110))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_add_project = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_add_project.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_add_project.setObjectName("btn_add_project")
        self.gridLayout_2.addWidget(self.btn_add_project, 0, 1, 1, 1)
        self.le_enter_project = QtWidgets.QLineEdit(self.groupBox_5)
        self.le_enter_project.setObjectName("le_enter_project")
        self.gridLayout_2.addWidget(self.le_enter_project, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 2, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cb_project_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.cb_project_2.setObjectName("cb_project_2")
        self.gridLayout_5.addWidget(self.cb_project_2, 0, 0, 1, 1)
        self.le_enter_task_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_enter_task_2.setObjectName("le_enter_task_2")
        self.gridLayout_5.addWidget(self.le_enter_task_2, 0, 1, 1, 1)
        self.btn_add_task = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_add_task.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_add_task.setObjectName("btn_add_task")
        self.gridLayout_5.addWidget(self.btn_add_task, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 0, 1, 2, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_add_project.clicked.connect(self.le_enter_task_2.setFocus)
        self.le_enter_task_2.returnPressed.connect(self.btn_add_task.click)
        self.le_enter_project.returnPressed.connect(self.btn_add_project.click)
        self.btn_add_task.clicked.connect(self.sb_number_of_poms.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cb_project, self.cb_task)
        MainWindow.setTabOrder(self.cb_task, self.sb_number_of_poms)
        MainWindow.setTabOrder(self.sb_number_of_poms, self.btn_go)
        MainWindow.setTabOrder(self.btn_go, self.le_enter_project)
        MainWindow.setTabOrder(self.le_enter_project, self.btn_add_project)
        MainWindow.setTabOrder(self.btn_add_project, self.cb_project_2)
        MainWindow.setTabOrder(self.cb_project_2, self.le_enter_task_2)
        MainWindow.setTabOrder(self.le_enter_task_2, self.btn_add_task)
        MainWindow.setTabOrder(self.btn_add_task, self.le_interruption)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Current Task"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>seperate with comma</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "interruptions"))
        self.lbl_status.setText(_translate("MainWindow", "work"))
        self.groupBox.setTitle(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Project"))
        self.btn_go.setText(_translate("MainWindow", "go"))
        self.label_2.setText(_translate("MainWindow", "Task"))
        self.groupBox_3.setTitle(_translate("MainWindow", "New"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Project"))
        self.btn_add_project.setText(_translate("MainWindow", "add"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Task"))
        self.btn_add_task.setText(_translate("MainWindow", "add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
