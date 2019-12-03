#!/usr/bin/venv python
# -*- coding: utf-8 -*-
#https://blog.csdn.net/baidu_39372836/article/details/90240851

import pymysql
import xlwt


class Mysql(object):
    def __init__(self, database, user, password, host="localhost", port=3306, charset="utf8"):
        self.conn = pymysql.connect(host=host, port=port, database=database, user=user, password=password,
                                    charset=charset,autocommit = True)
        self.cs1 = self.conn.cursor()

    def get_table(self):
        self.cs1.execute("show tables;")
        tables_name = self.cs1.fetchall()
        return [i[0] for i in tables_name]

    def get_data(self, table_name):
        self.cs1.execute("select * from {}".format(table_name))
        data = self.cs1.fetchall()
        # 获取表格的字段
        table_field = [i[0] for i in self.cs1.description]
        # 拼接表格字段和数据
        data = list(data)
        data.insert(0, tuple(table_field))
        return data, table_field

    def __del__(self):
        print("删除mysql链接")


class Excel(object):
    def __init__(self, excel_name):
        self.excel_name = excel_name
        # self.app = xw.App(visible=True, add_book=False)
        # self.wb = self.app.books.add()
        self.wb = xlwt.Workbook()

    def write_excel(self, data, fields, sheet_name):
        sheet = self.wb.add_sheet(sheet_name,cell_overwrite_ok=True)

        row = 1
        col = 0
        for row in range(1,len(data)+1):
            for col in range(0,len(fields)):
                sheet.write(row-1,col,u'%s'%data[row-1][col])

    def save_excel(self):
        path = "/home/sgl/db_HW/DB/" + self.excel_name +".xlsx"
        self.wb.save(path)


if __name__ == '__main__':
    mysql = Mysql(database="pet", user="root", password="owen")
    table_names = mysql.get_table()
    m_excel = Excel(excel_name="animal-table")
    for table_name in table_names:
        table_data,fields = mysql.get_data(table_name=table_name)
        m_excel.write_excel(table_data, fields, table_name)
    m_excel.save_excel()
