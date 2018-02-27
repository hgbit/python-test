#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
# db = MySQLdb.connect(host="172.16.20.103",port=3306,user="JRJ_mystock_test",passwd="zQHRGbWLqFptMxaMC3gN",db="mystock",charset="utf8")
db = MySQLdb.connect(host="172.16.20.103",port=3308,user="user_wangyl",passwd="4dYv^ph%f",db="stock",charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()