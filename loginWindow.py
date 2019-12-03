#!/usr/bin/venv python
# -*- coding: utf-8 -*-

"""
login in implementing MainWindow.
"""

import time
# pyqt5 class
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QMessageBox,QStatusBar
from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator,QPixmap,QImage
# from Ui_URgui import Ui_MainWindow
# from ur_gui_ros_node import guiNode
from Ui_login import Ui_Dialog
from DBwindow import DBMainWindow
from Pet import PET

id_pwd_dict = {"store": "admin",
                "alice":"alice",
                "jack":"jack",
                "zjj":"zjj" }

class LGDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        super(LGDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Pet Management Login')
        # self.setFixedSize(1440,950)
        self.init_show()
        self.id = ""
        self.accDB = PET()
        self.accDB.set_owner("account")

    def init_show(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('./resource/dog.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    @pyqtSlot()
    def on_pushButton_clear_clicked(self):
        self.lineEdit_account.clear()
        self.lineEdit_password.clear()

    @pyqtSlot()
    def on_pushButton_enter_clicked(self):
        account_flag = 0
        pwd_flag = 0
        id = self.lineEdit_account.text()
        pwd = self.lineEdit_password.text()
        res = self.accDB.load_cols_from_db("id",id)
        if res:
            account_flag = 1
            if res[1] == pwd:
                pwd_flag = 1
        # else:

        # bool_id = id_pwd_dict.has_key(id)
        # bool_pwd = ( id_pwd_dict.get(id) == pwd )
        # print(bool_id,bool_pwd)
        # if bool_id:
        #     account_flag = 1
        # if bool_pwd:
        #     pwd_flag = 1

        all_flag = pwd_flag + account_flag
    
        # print(all_flag)
        if all_flag == 2:
            self.set_id(id)
            self.accept()
            # return True
        else:
            self.warning_msgbox()
            return

    def warning_msgbox(self):
        msg = QMessageBox.information(self,
                            "Remind",
                            "Please input right ID and PASSWORD!",
                            QMessageBox.Yes)
        if (msg == QMessageBox.Yes):
            return
        else:
            return