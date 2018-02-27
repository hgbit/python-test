#! /usr/bin/python
# -*- coding: UTF-8 -*-
# writen by guan.huang
import urlparse, urllib, urllib2, gzip, os, time

ALARM_URL = 'http://wx.jrj.com.cn/api/weixin.jsp?action=send_msg&users=guan.huang&content='

msg = '报警'
# values = {'action': 'send_msg', 'users':'guan.huang|weibo.qin', 'content': msg}
print (urllib.quote(msg))
# urllib2.urlopen(ALARM_URL, urllib.urlencode(msg))
