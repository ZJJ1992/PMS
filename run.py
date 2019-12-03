#!/usr/bin/venv/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow,QDialog, QMessageBox,QStatusBar
from DBwindow import DBMainWindow
from loginWindow import LGDialog
import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = LGDialog()
    if  dialog.exec_()==QDialog.Accepted:
        name = dialog.get_id()
        the_window = DBMainWindow()
        the_window.set_id(name)
        the_window.show()
        sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # ui = DBMainWindow()
    # ui.show()

    # sys.exit(app.exec_())
