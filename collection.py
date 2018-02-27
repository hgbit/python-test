#!/usr/bin/python
# -*- coding: UTF-8 -*-

mylist = [1, 2, 3, 4]
print mylist[2]

dict1 = {1:"a", 2:"b"}
dict2 = {1:"a", 2:"b", 2:"b"}

print cmp(dict1, dict2)
print dict1.items()
print dict2.items()
dict2.pop(1)
print dict2.items()