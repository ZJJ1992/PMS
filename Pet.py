#!/usr/bin/venv python
# -*- coding: utf-8 -*-
'''
pet attributes and statistic methods
one pet
Lily: 
{
    age: 10,
    name: Lily,
    color: yellow,
    #height: 0.5m,
    #weight: 20kg,
    class: dog,
    gender: male,
    price: 10
}
name class age color gender price

'''
from DBsql import DB
import time

class PET():

    def __init__(self):
        # can not re-define construct method
        self.all_pet_dict = {}
        chosen_pet_name_list = []
        # self.owner = owner
        self.db = DB()
        # self.img_dict= {"zjj":}
        self.query_times = 0  
        self.dir =  "/home/sgl/db_HW/"
        self.db_path = self.dir+"DB/"
        self.img_path =  self.db_path + "pic/"        
        # self.chosen_index = 0

    def add_query_times(self):
        self.query_times = self.query_times + 1
    
    def get_owner_money(self, owner):
        tb_name = self.db.dbname + ".account"
        res = self.db.load_columns("id",owner,tb_name)
        return res[2]

    def set_owner_money(self, owner, money):
        tb_name = self.db.dbname + ".account"
        # delete the line
        # l = self.db.load_columns("id",owner,tb_name)
        # l = list(l)
        # l[2] = str(money)
        self.db.update_data("money", str(money), "id", owner, tb_name)
        # add one new line
        # pass

    def set_chosen_pet_name_list(self,res_list):
        self.chosen_num = len(res_list)
        self.chosen_pet_name_list = self.choose_key_list_from_query_list(res_list,'name')
        self.currentIndex = 0

    def set_currentIndex(self,id):
        self.currentIndex = id

    def choose_key_list_from_query_list(self, res_list, key):
        key_list = []
        key_num = self.attr_list.index(key)
        if len(res_list) > 0:
            for i in range(0,len(res_list)):
                key_list.append(res_list[i][key_num])
        return key_list

    def set_owner(self, owner):
        self.owner = owner
        self.money = 0
        
        self.tb_name = self.db.dbname + '.' + self.owner
        # print(self.tb_name,self.db.dbname)
        self.attr_list = self.db.read_attr_list_from_table(self.owner, self.db.dbname)

    def add_pet_to_db(self, add_list):
        data_list = [add_list]
        attr_list = self.attr_list
        tb_name = self.tb_name
        self.db.add_columns(self.owner, data_list, attr_list)
    
    def load_rows_from_db(self, columnName):
        tb_name = self.tb_name
        res_list = self.db.load_rows(columnName,tb_name)
        # print(res_list)
        return res_list
        # pass
    
    def load_cols_from_db(self, key, val):
        tb_name = self.tb_name
        # print(tb_name)
        # print(key)
        # print(val)
        res_list = self.db.load_columns(key,val,tb_name)
        return res_list
    
    def load_img_file(self, img):
        fname = img+'.jpg'
    
    def load_choice_dict_query(self, choice_dict):
        tb_name = self.tb_name
        res_list,choice = self.db.load_choice(tb_name, choice_dict)
        return res_list,choice

    def get_total_val(self, key, val):
        tb_name = self.tb_name
        return self.db.count_total_num(key, val, tb_name)  

    def sum_price(self, key):
        tb_name = self.tb_name
        return self.db.sum_total_price(key,  tb_name)   

    def mum_val(self,key,mum):
        tb_name = self.tb_name  
        return self.db.select_mum(key,mum,tb_name) 

    def del_val(self, key, val):
        tb_name = self.tb_name
        return self.db.del_columns(tb_name, [(key,val)])

    def add_item(self, l):
        tb_name = self.tb_name
        self.db.add_columns(tb_name, [l],self.attr_list )

    def add_item_to_buyer(self, l, buyer ):
        tb_name = self.db.dbname + "."+buyer
        self.db.add_columns(tb_name, [l],self.attr_list )

    def set_money_to_transaction(self, price, buyer, seller):
        tb_name = self.db.dbname + ".transaction" 
        attr_list = ["buyer",	"seller"	,"price"	,"time"]
        now = time.localtime()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S",now)
        data_list = [ [ buyer, seller, price, time_str] ]
        self.db.add_columns(tb_name, data_list, attr_list)
    # def get_total_val(self, key):
    #     pet_dict = self.all_pet_dict
    #     sum = 0
    #     # num = 0
    #     # ave = 0
    #     for pet in pet_dict:
    #         sum = sum + pet[key]
    #         # num = num + 1
    #     return sum
    
    def get_ave_val(self, key):
        pet_dict = self.all_pet_dict
        sum = 0
        num = 0
        ave = 0
        for pet in pet_dict:
            sum = sum + pet[key]
            num = num + 1
        ave = sum * 1.0 / num
        return ave

    def get_all_val(self, key):
        pet_dict = self.all_pet_dict
        key_list = []
        # sum = 0
        # num = 0
        # ave = 0
        for pet in pet_dict:
            key_list.append(pet[key])
            # sum = sum + pet[key]
            # num = num + 1
        # ave = sum * 1.0 / num
        return key_list
