# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow - untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Inequal = QtWidgets.QPushButton(self.centralwidget)
        self.Inequal.setObjectName("Inequal")
        self.horizontalLayout.addWidget(self.Inequal)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setObjectName("Save")
        self.horizontalLayout.addWidget(self.Save)
        self.Equal = QtWidgets.QPushButton(self.centralwidget)
        self.Equal.setObjectName("Equal")
        self.horizontalLayout.addWidget(self.Equal)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 28))
        self.menubar.setObjectName("menubar")
        self.program_setting = QtWidgets.QMenu(self.menubar)
        self.program_setting.setObjectName("program_setting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tips = QtWidgets.QAction(MainWindow)
        self.tips.setObjectName("tips")
        self.program_setting.addAction(self.tips)
        self.menubar.addAction(self.program_setting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????????????"))
        self.Inequal.setText(_translate("MainWindow", "?????????"))
        self.Save.setText(_translate("MainWindow", "??????"))
        self.Equal.setText(_translate("MainWindow", "??????"))
        self.program_setting.setTitle(_translate("MainWindow", "??????"))
        self.tips.setText(_translate("MainWindow", "????????????"))
from PyQt5 import QtWebEngineWidgets
