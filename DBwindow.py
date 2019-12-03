#!/usr/bin/venv python
# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
#project path
# import re
# from PROJECTPATH import *
import time,os
# pyqt5 class
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QFileDialog,QMainWindow, QMessageBox,QLineEdit,QRadioButton,QStatusBar,QComboBox
from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator,QPixmap,QImage,QPainter
from Ui_DB import Ui_MainWindow
from Pet import PET
# from ur_gui_ros_node import guiNode

# define class
# from gui_ros_node import *
# import cv2


class DBMainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(DBMainWindow, self).__init__(parent)
        self.setupUi(self)

        # self.setFixedSize(1440,950)
        self.init_show()

        self.petDB = PET()
        self.accDB = PET()
        self.accDB.set_owner("account")
        

    def set_id(self, id):
        self.id = id
        self.petDB.set_owner(id)
        # print(type(self.id))
        # print(self.id)
        str = "Store Holder:  " + self.id + ' ! Welcome to your Pet Management System'
        self.setWindowTitle(  str )
        self.show_money(self.id)

    def init_show(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('./resource/dog.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.img_post_btn.setEnabled(False)
        self.img_pre_btn.setEnabled(False)
        self.trans_sell_check_btn.setEnabled(False) 
        # self.setWindowOpacity(0.9)
    
    # def paintEvent(self,event):
    #         #初始化绘图工具
    #     qp=QPainter()
    #     #开始在窗口绘制
    #     qp.begin(self)  
    #     #自定义画点方法
    #     qp.fillRect([0,0,1091,741],QColor(255, 255, 0, 200))
    #     #结束在窗口的绘制
    #     qp.end()

        
    # def set_label_pic(self, label, img):
    #     try:
    #         h, w = img.shape[:2]
    #         img = QImage(img,
    #                      w, h, QImage.Format_RGB888)
    #         img = QPixmap.fromImage(img)
    #         label.setPixmap(img)
    #         label.setScaledContents(True)
    #     except:
    #         print("no img for qtgui")

    @pyqtSlot()
    def on_sta_help_btn_clicked(self):
        str =  'In Statistic frame, some important sum, average data can be shown by pressing "obtain".'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_qu_help_btn_clicked(self):
        str = 'In Query frame, through "load", you can load all pets attributes to the combobox; after the chosen of every attribute in the combobox, press "Preview", the pet image can be seen in the Pet Image frame. Also press "query", and choose the union query conditions, you can get the union query result from the database.'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_img_upload_btn_clicked(self):
        # directory = QtWidgets.QFileDialog.getOpenFileName(self,
        #                                                   "getOpenFileName", "./",
        #                                                   "All Files (*)")
        label = self.pet_img_label
        imgName, imgType = QFileDialog.getOpenFileName(self, "open image", "", "*jpeg;;All Files(*);;*.jpg;;*.png")
        jpg = QtGui.QPixmap(imgName).scaled(label.width(), label.height())
        label.setPixmap(jpg)

    @pyqtSlot()
    def on_trans_help_btn_clicked(self):
        str = 'In Transaction frame, you can keep the sell and add record.'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_img_help_btn_clicked(self):
        str='In Image frame, you can check the pet picture or upload a file to preview.'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_img_clear_btn_clicked(self):
        label = self.pet_img_label
        label.setPixmap(QPixmap(""))    


    @pyqtSlot()
    def on_qu_pushButton_clicked(self):
        # namBox = self.qu_name_comboBox
        # catBox = self.qu_category_comboBox
        # ageBox = self.qu_age_comboBox
        # genBox = self.qu_gender_comboBox
        # colBox = self.qu_color_comboBox
        # priceBox = self.qu_price_comboBox
        attr_list = self.petDB.attr_list[:6]
        # print(attr_list)
        # attr_list = self.petDB.db.read_attr_list_from_table()
        # res_num = 0
        for attr in attr_list:
        # name = "name"
            l = self.petDB.load_rows_from_db(attr)
            # res_num = len(l)
            l_str = [str(i) for i in l]
            comBoxName = "qu_"+attr+"_comboBox"
            # print(comBoxName)
            comBox = self.findChild(QComboBox, comBoxName)
            comBox.clear()
            comBox.addItems(l_str)
        name_list =  self.petDB.load_rows_from_db("name")
        print(name_list)
        self.petDB.set_chosen_pet_name_list(name_list)
        self.set_query_result_number(self.petDB.chosen_num)
        self.delete_duplicate()
        # print(self.qu_name_comboBox.currentIndex())
        self.img_post_btn.setEnabled(True)
        self.img_pre_btn.setEnabled(False)
            # self.add_item_list_to_comBox(comBox,l)
            # print(l)
    
    def set_query_result_number(self, num):
        self.qu_res_num_label.setText( str(num) )

    @pyqtSlot()
    def on_qu_query_btn_clicked(self):
        choice_dict = {}        
        attr_list = self.petDB.attr_list[:6]
        flag = 0
        for attr in attr_list:
            # res = []
            radioBtnName = "qu_"+attr+"_radioButton"
            radioBtn = self.findChild(QRadioButton, radioBtnName)
            # choice_dict[attr] = radioBtn.isChecked()
            if radioBtn.isChecked():
                res = []
                flag = 1
                comBoxName = "qu_"+attr+"_comboBox"
                comBox = self.findChild(QComboBox, comBoxName)
                val = comBox.currentText()
                if attr == "age" or attr == "price":
                    signcomBoxName = "qu_equal_"+attr+"_comboBox"
                    sign_comBox = self.findChild(QComboBox, signcomBoxName)
                    sign = sign_comBox.currentText()
                    res = [sign, val]
                else:
                    res = [val]
                choice_dict[attr] = res
        # print(choice_dict)
        if flag == 1:
            res_list,choice = self.petDB.load_choice_dict_query(choice_dict)
            self.petDB.add_query_times()
            # print(res_list)
            q_times = self.petDB.query_times
            status = "The " + str(q_times) + "th query is: " + choice +"\n"
            # res_num = len(res_list)
            # name_list =  self.petDB.set_chosen_pet_name_list(res_list)
            self.petDB.set_chosen_pet_name_list(res_list)
            self.set_query_result_number( self.petDB.chosen_num )
            if len(res_list) > 0:                
                i = 0
                status = status + " Result is: "
                for attr in attr_list:
                    l_str = []
                    for res in res_list:
                        l_str.append(str(res[i]))
                    comBoxName = "qu_"+attr+"_comboBox"
                    comBox = self.findChild(QComboBox, comBoxName)
                    # print(comBoxName)
                    # print(l_str)
                    comBox.clear()
                    comBox.addItems(l_str)
                    i = i + 1
                for res in res_list:
                    status = status + res[0] + ", "
                status = status[:-2]
                self.delete_duplicate()
                
                showname = res_list[0][0]
                # print(showname)
                self.view_of_name_comboBox(showname)
            else:
                status = status + "NO result!"
                self.img_name_lineEdit.setText("")
                label = self.pet_img_label
                label.setPixmap(QPixmap("")) 
            self.set_his_textEdit(status)
            # self.img_name_lineEdit.setText(self.qu_name_comboBox.currentText())
        elif flag == 0:
            
            self.warning_msgbox("please select at least one query choice!")
            self.img_name_lineEdit.setText("")
            label = self.pet_img_label
            label.setPixmap(QPixmap(""))  
        # return choice_dict
        # pass

    @pyqtSlot()
    def on_qu_preview_btn_clicked(self):
        name = self.qu_name_comboBox.currentText()
        self.view_of_name_comboBox(name)

    def view_of_name_comboBox(self,name):        
        path = self.petDB.img_path
        imgName = path + name + ".jpg"
        # print(imgName)
        self.view_img_in_label(imgName)
        self.img_name_lineEdit.setText(name)


    def view_img_in_label(self, imgName):
        self.set_imgName(imgName)
        try:
            imgName = self.imgName
            label = self.pet_img_label
            print(imgName)
            jpg = QtGui.QPixmap(imgName).scaled(label.width(), label.height())
            label.setPixmap(jpg)
        except:
            msg = "No picture can be found with your choice!"
            self.warning_msgbox(msg)
        # self.trans_img_lineEdit.setText(imgName)

    def delete_duplicate(self):
        for attr in self.petDB.attr_list:
            comBoxName = "qu_"+attr+"_comboBox"
            comBox = self.findChild(QComboBox, comBoxName)
            # print(comBoxName)
            # print(l_str)
            AllItems = [comBox.itemText(i) for i in range(comBox.count())]
            # print(AllItems)
            clear_items = list(set(AllItems))
            clear_items.sort(key=AllItems.index) # duplicate
            # print(clear_items)
            comBox.clear()
            comBox.addItems(clear_items)

    @pyqtSlot()
    def on_img_pre_btn_clicked(self):
        path = self.petDB.img_path
        chosen_list = self.petDB.chosen_pet_name_list
        now_index = self.petDB.currentIndex
        if now_index < 1:
            self.img_pre_btn.setEnabled(False)
        else:
            new_index = now_index - 1
            # name = self.qu_name_comboBox.itemText(new_index)
            name = self.qu_name_comboBox.itemText(new_index)
            imgName = path + name + ".jpg"
            self.view_img_in_label(imgName)
            # self.reorder_comBox_items(new_index)
            self.img_name_lineEdit.setText(name)
            self.delete_duplicate()
            self.petDB.set_currentIndex(new_index)
            self.img_post_btn.setEnabled(True)

    @pyqtSlot()
    def on_img_post_btn_clicked(self):
        path = self.petDB.img_path
        chosen_list = self.petDB.chosen_pet_name_list
        now_index = self.petDB.currentIndex
        count = self.qu_name_comboBox.count()
        if now_index > count-2:
            self.img_post_btn.setEnabled(False)
        else:
            new_index = now_index + 1
            name = self.qu_name_comboBox.itemText(new_index)
            imgName = path + name + ".jpg"
            self.view_img_in_label(imgName)
            # self.reorder_comBox_items(new_index)
            self.img_name_lineEdit.setText(name)
            self.delete_duplicate()
            self.petDB.set_currentIndex(new_index)
            self.img_pre_btn.setEnabled(True)

    def reorder_comBox_items(self, new_index):
        # now_index = self.petDB.currentIndex
        name = self.qu_name_comboBox.itemText(new_index)
        # print(new_index)
        # print(name)
        l = self.petDB.load_cols_from_db("name",name)
        # print(l)
        j = 0
        for attr in self.petDB.attr_list:
            comBoxName = "qu_"+attr+"_comboBox"
            # print(comBoxName)
            comBox = self.findChild(QComboBox, comBoxName)
            # print(l[j])
            s = str(l[j])
            # print(s)
            AllItems = [comBox.itemText(i) for i in range(comBox.count())]
            id = AllItems.index(s)
            # print(id)
            comBox.setCurrentText(s)
            j = j + 1            
        
        # l = self.petDB.load_cols_from_db("name",name)

        # chosen_list = self.petDB.chosen_pet_name_list
        # for name in chosen_list:
        #     # name = "name"
        #     l = self.petDB.load_cols_from_db("name",name)
        #     # res_num = len(l)
        #     l_str = [str(i) for i in l]
        #     comBoxName = "qu_"+attr+"_comboBox"
        #     # print(comBoxName)
        #     comBox = self.findChild(QComboBox, comBoxName)
        #     comBox.clear()
        #     comBox.addItems(l_str)

    # def reorder_comBox_items(self):
    #     AllItems = [QComboBoxName.itemText(i) for i in range(QComboBoxName.count())]

    
    def set_his_textEdit(self, status):
        self.his_textEdit.append("@"+status)

    @pyqtSlot()
    def on_sta_obtain_btn_clicked(self):
        total_dog_no = self.petDB.get_total_val("category", "dog")
        total_cat_no = self.petDB.get_total_val("category", "cat")
        total_price = self.petDB.sum_price("price")
        eldest_pet = self.petDB.mum_val('age','max')
        self.total_dog_no_lineEdit.setText(str(total_dog_no))
        self.total_cat_no_lineEdit.setText(str(total_cat_no))
        self.total_price_lineEdit.setText(str(total_price))
        self.eldest_pet_lineEdit.setText(eldest_pet[0])
        self.eldest_age_lineEdit.setText(str(eldest_pet[2]))
        self.eldest_price_lineEdit.setText(str(eldest_pet[5]))
        # pass

    @pyqtSlot()
    def on_trans_del_load_btn_clicked(self):
        l = self.petDB.load_rows_from_db("name")
        comBox = self.trans_del_pet_name_comboBox
        comBox.clear()
        comBox.addItems(l)   #
        comBox2 = self.trans_sell_pet_name_comboBox
        comBox2.clear()
        comBox2.addItems(l)   #
        l2 = self.accDB.load_rows_from_db("id")
        l2.remove(self.id)
        comBox3 = self.trans_sell_buyer_comboBox
        comBox3.clear()
        comBox3.addItems(l2)   #
        self.trans_sell_check_btn.setEnabled(True) 

    @pyqtSlot()
    def on_trans_del_ok_btn_clicked(self):
        val = self.trans_del_pet_name_comboBox.currentText()
        if val=="":
            self.warning_msgbox("please press load button and choose a pet to delete!")
            return 
        if self.choose_msgbox("Are you sure to delete"):
            
            self.petDB.del_val("name",val)
            status = "Successfully Delete pet" + val
            self.set_his_textEdit(status)
            fname = self.petDB.img_path + val +".jpg"
            cmd = "mv " + fname + " " + self.petDB.db_path  
            # print(cmd)
            os.system(cmd)
        else:
            return
    
    @pyqtSlot()
    def on_trans_add_help_btn_clicked(self):
        str =  'In Transaction frame of Add, you can load any animal picture in your computer through "load image", and fill its attributes in the blank line, press "Add", then you can add a new pet record to your database.'
        self.intro_plainTextEdit.setPlainText(str)
    
    @pyqtSlot()
    def on_trans_sell_help_btn_clicked(self):
        str =  'In Transaction frame of Sell, press "load" in the Delete Frame, you can get the pet name and buyer information from database; then after choose the pet and insert the final price, you can sell out the pet and in buyer database, a new record can be found in his databse.'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_trans_sell_check_btn_clicked(self):
        name = self.trans_sell_pet_name_comboBox.currentText()
        l = self.petDB.load_cols_from_db("name",name)
        self.trans_sell_price_lineEdit.setText(str(l[5]))
        self.trans_sell_category_lineEdit.setText(l[1])

    def show_money(self, owner):
        money = self.petDB.get_owner_money(owner)
        self.show_money_label.setText(str(money))

    @pyqtSlot()
    def on_trans_sell_ok_btn_clicked(self):
        # trans_sell_ok_btn
        price = self.trans_sell_final_price_lineEdit.text()
        buyer = self.trans_sell_buyer_comboBox.currentText()
        # print(price)
        if buyer == "":
            self.warning_msgbox("please choose a buyer!")
            return

        if price:
            name = self.trans_sell_pet_name_comboBox.currentText()
            l = self.petDB.load_cols_from_db("name",name) 
            l = list(l)
            l[5] = price
            
            status = "Pet: %s, Buyer: %s, final price: %s. " \
                %(name, buyer, price)
            if self.choose_msgbox(status + "\n Sure finished?"):

                self.petDB.del_val("name",name)
                status = "Successfully Sell pet" + name + "!"
                self.set_his_textEdit(status)
                fname = self.petDB.img_path + name +".jpg"
                cmd = "mv " + fname + " " + self.petDB.db_path 
                os.system(cmd)
                # add new record in buyer db
                self.petDB.add_item_to_buyer( l, buyer)
                status2 = "Successfully "+ buyer + " gets the pet "+ name + "!"
                self.set_his_textEdit(status2)
                fname = self.petDB.db_path + name +".jpg"
                cmd = "mv " + fname + " " + self.petDB.img_path 
                os.system(cmd)
                seller =self.id
                self.petDB.set_money_to_transaction(price, buyer, seller)

                money = int(self.petDB.get_owner_money(seller)) + int(price)
                self.show_money_label.setText(str(money))
                self.petDB.set_owner_money(seller,str(money))

                money_buyer = int(self.petDB.get_owner_money(buyer)) - int(price)
                self.petDB.set_owner_money(buyer,str(money_buyer))
            # print(cmd)
            # os.system(cmd)
                # pass============
            else:
                return          
            # pass
        else:
            self.warning_msgbox("please insert the final transaction price!")
            return

    # @pyqtSlot()
    # def on_trans_sell_load_btn_clicked(self):
    #     l = self.accDB.load_rows_from_db("id")
    #     try:
    #         l.remove(self.id)
    #     except:
    #         pass
    #     self.trans_sell_buyer_comboBox.clear()
    #     self.trans_sell_buyer_comboBox.addItems(l)

    #     pet_list = self.petDB.load_rows_from_db("name")
    #     self.trans_sell_pet_name_comboBox.clear()
    #     self.trans_sell_pet_name_comboBox.addItems(pet_list)

    @pyqtSlot()
    def on_trans_load_img_btn_clicked(self):
        # fname = ''
        # fname = self.trans_img_lineEdit.text()
        # record = [fname, ]
        ## open image
        label = self.pet_img_label
        imgName, imgType = QFileDialog.getOpenFileName(self, "open image", "", "*jpeg;;All Files(*);;*.jpg;;*.png") 
        # print(imgName)
        self.set_imgName(imgName)
        self.trans_img_lineEdit.setText(imgName)
        pet_name = imgName.split("/")[-1].split(".")[0]
        # print(fname)
        # print(fname.split("/")[-1])
        # print(pet_name)
        self.trans_name_lineEdit.setText(pet_name)

    def set_imgName(self, img):
        self.imgName = img
    
    @pyqtSlot()
    def on_trans_add_ok_btn_clicked(self):
        fname = self.trans_img_lineEdit.text()
        pet_name = fname.split("/")[-1].split(".")[0]
        in_name = self.trans_name_lineEdit.text()
        bool_name = (pet_name == in_name)
        if bool_name:
            l = []
            for attr in self.petDB.attr_list:
                lEditName = "trans_"+attr+"_lineEdit"
                lEdit = self.findChild(QLineEdit, lEditName)
                val = lEdit.text()
                l.append(val)
            # in_category = self.trans_name_lineEdit.text()
            # in_age = self.trans_age_lineEdit.text()
            # in_color = self.trans_color_lineEdit.text()
            # in_gender = self.trans_gender_lineEdit.text()
            # in_price =self.trans_price_lineEdit.text()
            # holder_marker = ",".join(["%s"]*len(self.petDB.attr_list))
            status = "Add new member (%s) to your database."\
                %(",".join(l))
            if self.choose_msgbox(status+"\nSure about that?"):
                self.set_his_textEdit(status)
                # l = [in_name,in_category,in_age,in_color,in_gender,in_price]
                self.petDB.add_item(l)
                cmd = "mv " +  fname + " " + self.petDB.img_path
                os.system(cmd)
                self.warning_msgbox("successfully add a new pet! \n please query and preview him with name: " + in_name)
            else:
                return 
        else:
            ch = self.choose_msgbox("You input another name for the new pet\n Sure to change its file name?")
            if ch :
                pre = '/'.join(fname.split("/")[:-1])
                new_name = pre +"/"+ in_name + '.jpg'
                cmd = "mv " +  fname + " " + new_name
                print(cmd)
                os.system(cmd)
                self.warning_msgbox("filename has been changed to " + in_name + '.jpg' +"!")
                self.trans_img_lineEdit.setText(new_name)
            else:
                self.warning_msgbox("please change the input name in the name edit place.")

    @pyqtSlot()
    def on_trans_clear_btn_clicked(self):
        self.trans_name_lineEdit.setText("")
        self.trans_category_lineEdit.setText("")
        self.trans_age_lineEdit.setText("")
        self.trans_gender_lineEdit.setText("")
        self.trans_color_lineEdit.setText("")
        self.trans_price_lineEdit.setText("")

    @pyqtSlot()
    def on_trans_preview_btn_clicked(self):
        try:
            imgName = self.imgName
            label = self.pet_img_label
            jpg = QtGui.QPixmap(imgName).scaled(label.width(), label.height())
            label.setPixmap(jpg)
        except:
            msg = "please press the load img button to choose an image file!"
            self.warning_msgbox(msg)

    # @pyqtSlot()
    # def on_trans_ok_btn_clicked(self):
    #     tmp_list = []
    #     name = self.trans_name_lineEdit.text()
    #     category = self.trans_category_lineEdit.text()
    #     age = self.trans_age_lineEdit.setText.text()
    #     gender = self.trans_gender_lineEdit.setText.text()
    #     color = self.trans_color_lineEdit.setText.text()
    #     price = self.trans_price_lineEdit.setText.text()
    #     tmp_list.append(name,category,age,gender,color,price)
    #     self.petDB.add_pet_to_db(tmp_list)

    
    def warning_msgbox(self,msg):
        msg = QMessageBox.information(self,
                                "Remind",
                                msg,
                                QMessageBox.Yes)
        if (msg == QMessageBox.Yes):
            return
        else:
            return False
    
    def choose_msgbox(self,msg):
        msg = QMessageBox.information(self,
                                "Remind",
                                msg,
                                QMessageBox.Yes | QMessageBox.No)
        if (msg == QMessageBox.Yes):
            return True
        else:
            return False