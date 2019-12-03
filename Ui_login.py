# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 231)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 110, 231, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_id = QtWidgets.QLabel(self.layoutWidget)
        self.label_id.setObjectName("label_id")
        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)
        self.lineEdit_account = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.gridLayout.addWidget(self.lineEdit_account, 0, 1, 1, 2)
        self.label_pwd = QtWidgets.QLabel(self.layoutWidget)
        self.label_pwd.setObjectName("label_pwd")
        self.gridLayout.addWidget(self.label_pwd, 1, 0, 1, 2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 261, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 60, 231, 41))
        self.label_4.setObjectName("label_4")
        self.pushButton_clear = QtWidgets.QPushButton(Dialog)
        self.pushButton_clear.setGeometry(QtCore.QRect(90, 180, 101, 25))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_enter = QtWidgets.QPushButton(Dialog)
        self.pushButton_enter.setGeometry(QtCore.QRect(210, 180, 101, 25))
        self.pushButton_enter.setObjectName("pushButton_enter")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_id.setText(_translate("Dialog", "ID:"))
        self.lineEdit_account.setText(_translate("Dialog", "zjj"))
        self.lineEdit_account.setPlaceholderText(_translate("Dialog", "zjj"))
        self.label_pwd.setText(_translate("Dialog", "Password:"))
        self.lineEdit_password.setText(_translate("Dialog", "zjj"))
        self.label_3.setText(_translate("Dialog", "Welcome to pet management system!"))
        self.label_4.setText(_translate("Dialog", "plese input your id and password."))
        self.pushButton_clear.setText(_translate("Dialog", "Clear"))
        self.pushButton_enter.setText(_translate("Dialog", "OK"))


