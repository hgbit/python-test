#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
# db = MySQLdb.connect(host="172.16.20.103",port=3306,user="JRJ_mystock_test",passwd="zQHRGbWLqFptMxaMC3gN",db="mystock",charset="utf8")
db = MySQLdb.connect(host="172.16.20.103", port=3308, user="user_wangyl", passwd="4dYv^ph%f", db="stock",
                     charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM stock.zxhq_signal_info"
# try:
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    # 打印结果
    print "fname=%s" % \
          (fname)
# except:
#    print "Error: unable to fecth data"

# 关闭数据库连接
db.close()
