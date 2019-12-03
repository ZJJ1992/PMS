# PMS（Pet Management System）
The Pet Management System (PMS) is a pet information query, statistic, and pet transaction system for pet store holders.

## STEPS 
1. git download:
```
git clone https://github.com/ZJJ1992/PMS.git
```
2. create Mysql database:
```
python DBsql.py
```
3. run:
```
python run.py
```

## Prerequisite：
1. python3.5 above
2. PyQt5
3. Mysql
4. pymysql
5. xlrd and xlwt ( for excel to SQL and SQL to excel)

## Statistic
In Statistic frame, some important sum, average data can be shown by pressing "obtain".

## Image
In Image frame, you can check the pet picture or upload a file to preview.

## Transaction
In Transaction frame, you can keep the sell and add record.

## Query
In Query frame, through "load", you can load all pets attributes to the combobox; after the chosen of every attribute in the combobox, press "Preview", the pet image can be seen in the Pet Image frame.


## note
1.  ui to python cmd
```
/usr/bin/python3 -m PyQt5.uic.pyuic DB.ui -o Ui_DB.py
/usr/bin/python3 -m PyQt5.uic.pyuic login.ui -o Ui_login.py
```
2. add qrc file
   ```
   pyrcc5 add.qrc -o add_rc.py
   ```
3. pack to exe
   ```
   pyinstaller -F -w -D run.py
   ```

## important reference
1. [使用pymysql简单创建mysql数据库](https://blog.csdn.net/cnmnui/article/details/99324619)
2. [Python教程 | 五种常见的数据存储方式](http://blog.itpub.net/31561225/viewspace-2633478/)
3. [Python交互数据库（Mysql | Mongodb | Redis）](https://www.jianshu.com/p/8be1a04e6534)
4. [SQL 基础教程](https://www.w3school.com.cn/sql/sql_orderby.asp)
5. [ 基于python+mysql浅谈redis缓存设计与数据库关联数据处理](https://www.cnblogs.com/shouke/p/10157756.html)
6. [Redis和MySQL的4种结合方案](https://blog.csdn.net/hemeinvyiqiluoben/article/details/82563470)
7. [Mysql存储引擎介绍、查看及常用存储引擎讲解](https://www.2cto.com/database/201801/715203.html)
8. [python 使用 pymysql 数据库操作基本使用](https://www.jianshu.com/p/25f759413402)
9. [使用pymysql查询数据库，将结果保存为列表并获取指定元素下标](https://blog.csdn.net/cm731231988/article/details/80261269)
10. [redis和mysql的结合示例](https://www.jianshu.com/p/184c4c7a6572)
11. [python操作redis数据库](https://www.jianshu.com/p/c8b46f8c302d)
12. [Python小练习_将数据库中表数据存到redis里](https://www.cnblogs.com/jessica-test/p/9004774.html)
