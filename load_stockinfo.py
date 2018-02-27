#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# writen by guan.huang

import datetime
import gzip
import os
import urllib
import urllib2

STOCK_INFO_URL = 'http://127.0.0.1:8080/_inner/stockinfo'
ALARM_URL = 'http://wx.jrj.com.cn/api/weixin.jsp?action=send_msg&users=guan.huang|weibo.qin&content='
# FILE_PATH = '/data/build/zxhq-data/zxhq/sapi/download'
FILE_PATH = '/Users/guan.huang/Desktop/test'
FILE_NAME = 'stockinfo_v2.json.gz'


# 报警
def send_error_msg(msg):
    urllib2.urlopen(ALARM_URL + urllib.quote('拉取行情文件异常：' + msg))


# 备份文件
def backup_files():
    des_name = '%s-%s' % (FILE_NAME, datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
    if os.path.exists(FILE_NAME):
        os.rename(FILE_NAME, des_name)


# 删除过期文件
def delete_bak_files():
    # 设定2天前的文件为过期
    delta = datetime.timedelta(days=2)

    for dir_path, dir_names, file_names in os.walk(FILE_PATH):
        for file_name in file_names:
            # 获取文件创建时间
            ctime = datetime.datetime.fromtimestamp(os.path.getctime(file_name))
            # 若创建于delta天前,删除
            if FILE_NAME in file_name and ctime < (datetime.datetime.now() - delta):
                print 'delete file:' + file_name
                os.remove(file_name)


try:

    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' 拉取行情文件开始！'

    os.chdir(FILE_PATH)

    req = urllib2.urlopen(STOCK_INFO_URL, timeout=100)
    content = req.read()
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' 拉取行情文件条数=' + str(len(content))
    if len(content) < 1000:
        send_error_msg('result is empty, exit!')
        exit()

    backup_files()

    f = gzip.open(FILE_NAME, 'wb')
    f.write(content)
    f.close()

    delete_bak_files()

    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' 拉取行情文件成功！'

except Exception as e:
    print e
    send_error_msg(str(e))
