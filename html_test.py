#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# writen by guan.huang

from bs4 import BeautifulSoup
import urllib

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

url = "http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book"
page = urllib.urlopen(url)

# soup = BeautifulSoup(html, 'lxml')
soup = BeautifulSoup(page, 'lxml')

print soup.prettify()

print '----------------------------'


book_div = soup.find(attrs={"id":"book"})
book_a = book_div.findAll(attrs={"class":"title"})
for book in book_a:
    print book.string
    print book.attrs['href']

url1 = 'https://book.douban.com/subject/27131538/?from=tag'
soup1 = BeautifulSoup(urllib.urlopen(url1), 'lxml')
mydiv = soup1.find(attrs={"id":"db-rec-section"})
mya = mydiv.findAll('dd')
for mmmm in mya:
    print mmmm.a.string.lstrip().strip()
