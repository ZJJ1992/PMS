#!/usr/bin/venv python
# -*- coding: utf-8 -*-
'''
excle to sql database
'''
# refer : https://blog.csdn.net/qq_42708830/article/details/92762302
# and https://blog.csdn.net/weixin_41580638/article/details/86550318

import xlrd
import pymysql

# Open the workbook and define the worksheet


class DB(object):
    def __init__(self, dbname='pet'):
        # self.db_info = DATABASES_INFO
        # self.init_db(fname)
        self.host='localhost'
        self.port=3306
        self.user='root'
        self.password='owen'
        # self.database = fname,
        self.charset ='utf8mb4' 
        self.dbname = dbname
        # self.conn = pymysql.connect(host, user, passwd, charset=CHARSET)
        # self.cursor = self.conn.cursor()    
  
    def build_conn(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            # database=self.database,
            charset=self.charset
        )
        # get a cursor
        self.cursor = self.conn.cursor()
        # return self.conn, self.cursor

    def close_mysql(self):
        # 关闭游标
        self.cursor.close()
        # 提交
        self.conn.commit()
        # 关闭数据库连接
        self.conn.close()

    def read_xls(self, fname="./DB/animal-table.xlsx"):
        book = xlrd.open_workbook(fname) # excel  filename        
        # sheet1 = book.sheet_by_name("zjj") # sheet name in xls file
        # sheet2 = book.sheet_by_name("alice")
        # print(book.sheet_names())
        sheet_list = book.sheet_names()
        # print()
        return book, sheet_list

  ### main ####
    def excleTosqlDB(self):
        self.build_conn()
        book, sheet_list = self.read_xls()
        db_name = self.dbname
        self.create_DB(db_name)
        for sheet in sheet_list:
            self.create_table(sheet,db_name)
            attr_list = self.read_attributes_from_sheet(sheet,book)
            data_list = self.read_data_from_sheet(sheet, book)
            self.insert_columns(sheet, attr_list,data_list)

        self.close_mysql()
    
    def read_from_sheet(self, sheetname, book):
        sheet = book.sheet_by_name(sheetname)
        print(sheet.cell(0, 0).value)
    
    def read_attributes_from_sheet(self, sheetname, book):
        sheet = book.sheet_by_name(sheetname)
        # print(sheet.cell(0, 0).value)
        # print(sheet.ncols)
        attr_list=[]
        for i in range(0, sheet.ncols):
            attr_list.append(sheet.cell(0,i).value)
        # print(attr_list)
        # insert_attr = "zjj" + "("+','.join(attr_list)+")"
        # print(insert_attr)
        return attr_list
    
    def read_data_from_sheet(self, sheetname, book):
        sheet = book.sheet_by_name(sheetname)

        data_list=[]
        for j in range(1, sheet.nrows):
            tmp_list = []
            for i in range(0, sheet.ncols):
                tmp_list.append(sheet.cell(j,i).value)
            data_list.append(tuple(tmp_list))

        return data_list

    def create_DB(self, db_name):
        # drop database RUNOOB;
        self.cursor.execute('show databases;')
        try:
            cmd = "DROP DATABASE IF EXISTS  %s;" %(db_name)
            print(cmd)
            self.cursor.execute(cmd)
        except Exception as e:
            print("error:{e}")
        try:
            cmd = "CREATE DATABASE IF NOT EXISTS %s;" %(db_name)
            # cmd = f"CREATE DATABASE IF NOT EXISTS '{db_name}';"
            print(cmd)
            self.cursor.execute(cmd)
        except Exception as e:
            print("error:{e}")
            self.conn.rollback()
            return 
        print("DB created ok...")
    
    def create_table(self, tb_name, db_name):
        # refer:https://blog.csdn.net/cnmnui/article/details/99324619
        # my_table = f'CREATE TABLE {tb_info["tb_name"]}(' \
        #             f'id INT NOT NULL AUTO_INCREMENT,' \
        #             f'PRIMARY KEY (id)' \
        #             f')CHARSET="utf8mb4"'
        cmd = "use %s;" %(db_name)
        self.cursor.execute( cmd )
        self.cursor.execute('SHOW tables;')
        # cmd = "DROP TABLE IF EXISTS  %s;" 
        exist = self.cursor.execute("show tables like '%s'" % tb_name)
        if exist:
            self.cursor.execute("DROP TABLE IF EXISTS %s" % tb_name)
        print("ok cmd table")
        # try:
        #     cmd = "DROP TABLE IF EXISTS  %s;" 
        #     # print(cmd)
        #     self.cursor.execute(cmd, tb_name)
        #     print("ok cmd table")
        # except Exception as e:
        #     print("error:{e}")
        if tb_name == "account":
            my_table = " CREATE TABLE IF NOT EXISTS %s(\
                id varchar(10) primary key not null,\
                pwd varchar(10) not null,\
                money INT not null);" %(tb_name)
        elif tb_name == "transaction":
            my_table = " CREATE TABLE IF NOT EXISTS %s(\
                time varchar(30) primary key not null,\
                buyer varchar(10) not null,\
                seller varchar(10) not null,\
                price INT not null);" %(tb_name)            
        else:
            my_table = "CREATE TABLE IF NOT EXISTS %s( \
                name varchar(10) primary key not null, \
                category varchar(10) not null, \
                age INT not null, \
                color varchar(10) not null, \
                gender varchar(10) not null, \
                price INT not null);" \
                    %(tb_name)
        print("add table "+tb_name)
        # print(my_table)
        self.cursor.execute(my_table)
        # try:
        #     my_table = "CREATE TABLE IF NOT EXISTS %s( \
        #                 name varchar(10) primary key not null, \
        #                 category varchar(10), \
        #                 age varchar(10), \
        #                 color varchar(10), \
        #                 gender varchar(10), \
        #                 price INT, \
        #                 )CHARSET='utf8mb4';" \
        #                     %(tb_name)
        #     print("add table "+tb_name)
        #     self.cursor.execute(my_table)
        # except Exception as e:
        #     print("error:{e}")
        #     self.conn.rollback()
        #     return 
        print("table " + tb_name +" created ok...")

    def insert_columns(self, tb_name, attr_list, data_list):
        print("begin to insert columns")
        # attribute_list = 
        attr_str = tb_name + " ("+','.join(attr_list)+")"
        # data_str =
        print(len(data_list))
        holder_marker = ",".join(["%s"]*len(attr_list))
        for data in data_list: 
            # data_str = ','.join([str(j) for j in data])
            data = [str(j) for j in data]
            print(data)
            # query = "INSERT INTO %s VALUES (%s,%s,%s,%s,%s,%s);" %(attr_str, data) 
            query = "INSERT INTO " + attr_str + " VALUES ("+ holder_marker +");"
                # 执行sql语句
            # values = data_list
            print(query)
            self.cursor.execute(query, data)

    def del_columns(self, tb_name, attr_list):
        '''
        tb_name = "pet.zjj"
        attr_list = [("name","Thomas")]  # c.append(zip(a,b))
        '''
        self.build_conn()

        for attr in attr_list:
            # print(attr)
            # cmd = "delete from " + tb_name + " where " + attr[0] + "=%s;"
            # # cmd = " delete from userinfo where user=%s; "
            # print(cmd)
            # self.cursor.execute(cmd, attr[1])
            try:
                cmd = "delete from " + tb_name + " where " + attr[0] + "=%s;"
                # cmd = " delete from userinfo where user=%s; "
                print(cmd)
                self.cursor.execute(cmd, attr[1])
            except:
                print("error delete columns"+ attr )

        self.close_mysql()

    def add_columns(self, tb_name, data_list,attr_list):
        '''
        tb_name = "pet.zjj"
        attr_list = ["name", "category", "age", "color", "gender", "price"]
        data_list = [["Thomas", "dog", 2.0 , "white", "female", 7 ]]
        '''
        # attr_list = ["name", "category", "age", "color", "gender", "price"]
        self.build_conn()
        self.insert_columns(tb_name,attr_list,data_list)
        self.close_mysql()

    # def add_columns_transaction(self, tb_name, data_list,attr_list):
    #     '''
    #     tb_name = "pet.zjj"
    #     attr_list = ["name", "category", "age", "color", "gender", "price"]
    #     data_list = [["Thomas", "dog", 2.0 , "white", "female", 7 ]]
    #     '''
    #     attr_list = ["name", "category", "age", "color", "gender", "price"]
    #     self.build_conn()
    #     self.insert_columns(tb_name,attr_list,data_list)
    #     self.close_mysql()

    def read_attr_list_from_table(self, tb_name_raw, db_name):
        cmd = "select column_name from information_schema.columns where table_schema='%s' and table_name='%s';" %(db_name,tb_name_raw)
        res = self.query_sql(cmd)
        res = [ i[0] for i in list(res) ]
        # print(res)
        self.set_attr_list(res)
        return res    
    
    def set_attr_list(self, list):
        self.attr_list = list

    def load_rows(self, columnName, tb_name):
        query = "select %s from %s" %(columnName, tb_name)
        res = self.query_sql(query)
        res = [ i[0] for i in list(res) ]
        # print(res)
        return res
    
    def load_columns(self, key, val, tb_name):
        query = "select * from %s where %s='%s';" %(tb_name,key,val)
        res = self.query_sql(query)
        # print(self.cursor.description)
        if res:
            res = res[0]
        else:
            res = []
        return res
    
    def update_data(self, update_key, val, id, val_id, tb_name):
        query = "update %s SET %s='%s' where %s = '%s';"\
            %(tb_name, update_key, val, id, val_id)
        res = self.query_sql(query)
    
    def load_choice(self, tb_name, choice_dict):
        '''
        choice_dict={
            name: Thomas,  
            category: dog, # cat
            age: [>, 5], #eq, l, s, le, se, 
            price: [>, 4], #eq, l, s, le, se, 
            gender: male # female
        }
        '''
        res_list = []

        choice = ""
        for attr, res in choice_dict.iteritems():
            l = len(res)
            if l == 2:
                choice = choice + attr + res[0] + res[1] + " and "
            elif l == 1:
                choice = choice + attr + "= '" + res[0] + "' and "
        choice = choice[:-4]
        query = "select * from " + tb_name + " where %s ;" %(choice)
        # print(query)
        res = self.query_sql(query)
        res_list = list(res)
        # print(res_list)
        return res_list, choice

    def query_sql(self, query):
        self.build_conn()
        str = self.cursor.execute(query)
        res = self.cursor.fetchall()
        self.close_mysql()
        return res
    
    def count_total_num(self, key, val, tb_name):
        query = " select count(%s) from %s where %s='%s';"\
            %(key, tb_name, key, val)
        res = self.query_sql(query)
        return res[0][0]
    
    def sum_total_price(self, key, tb_name):
        query = " select sum(%s) from %s ;"\
            %(key, tb_name)
        res = self.query_sql(query)
        return res[0][0]
    
    def select_mum(self, key, mum, tb_name):
        # mum = max or min
        query = " select * from %s where %s =( \
             select %s(%s) from %s );"\
                %(tb_name, key, mum, key, tb_name)
        print(query)
        res = self.query_sql(query)
        print(res)
        if res:
            res = list(res[0])
        else:
            res = []
        return res
    
    def __del__(self):
        print("删除mysql链接")

    def test(self,query):
        res = self.query_sql(query)
        # print(self.cursor.description)
        # print(res)
        if res:
            print(type(res))
            print(list(res))

if __name__ == '__main__':
    db = DB()
    db.excleTosqlDB()

    # tb_name = "pet.zjj"
    # attr_list = [("name","Thomas")]  # c.append(zip(a,b))
    # db.del_columns(tb_name, attr_list)

    # tb_name = "pet.zjj"
    # attr_list = ["name", "category", "age", "color", "gender", "price"]
    # data_list = [["Thomas", "dog", 2.0 , "white", "female", 7 ]]
    # db.add_columns(tb_name,data_list,attr_list)
    # db.test_mysql("select column_name from information_schema.columns where table_schema='pet' and table_name='zjj'")
    # db.read_attr_list_from_table('zjj','pet')
    # db.load_rows('name','pet.zjj')
    # db.test("select * from pet.zjj where age>2;")
    # db.test("select count(category) from pet.zjj where category='dog';")
    # db.test("select min(age) from pet.zjj;")
    # db.select_mum('price','max', 'pet.zjj')


