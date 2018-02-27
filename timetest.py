#! /usr/bin/python
# -*- coding: UTF-8 -*-

import time, datetime

ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print "本地时间为 :", localtime
print localtime[2]

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print time.strftime("%Y%m%d-%H%M%S", time.localtime())

now = datetime.datetime.now()

print(now.strftime('%Y%m%d-%H%M%S'))

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' aaa'

