#! /usr/bin/python
# -*- coding: UTF-8 -*-
# writen by guan.huang
import urllib, urllib2, gzip, os, time

import os, datetime

PATH = '/Users/guan.huang/Desktop/test'

delta = datetime.timedelta(days=0)  # 设定365天前的文件为过期
now = datetime.datetime.now()  # 获取当前时间

for dir_path, dir_names, file_names in os.walk(PATH):
    for file_name in file_names:
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(dir_path, file_name)))  # 获取文件创建时间
        if 'stockinfo_v2.json.gz-20180108-1406' in file_name and ctime < (now - delta):  # 若创建于delta天前
            print file_name
            os.remove(os.path.join(dir_path, file_name))
