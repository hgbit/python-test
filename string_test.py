#! /usr/bin/python
# -*- coding: UTF-8 -*-
# writen by guan.huang

num = 100
file = 'aa'

print '%d to hex is' % (num)

print '%s/%s' % (file, file)

if ('%s/%s' % (file, file) in 'aa/aa'):
    print 'success'
