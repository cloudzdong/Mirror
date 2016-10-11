#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Administrator'

import bs4
from bs4 import BeautifulSoup
import requests
import io
import sys
from urllib.request import urlopen
import  re
import time

# root_url = 'https://weather.com'
# index_url = root_url + '/weather/today/l/CHXX0064:1:CH'
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# def spider():
#     response = requests.get(index_url)
#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     return [a.ng-scope for a in soup.div]
#
# print(spider())
# html = urlopen('http://www.cnblogs.com/huangcong/archive/2013/03/25/2980102.html')
# print(html.read())



html = urlopen('http://jinan.tianqi.com/today/')
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# html1 = html.decode('gbk').encode('utf-8').decode('utf-8')
bsObJ = BeautifulSoup(html.read())
#bsObJ1 = BeautifulSoup(html.read())
High_Temp = bsObJ.findAll("font", {"color": "red"})    #直接通过tags标签，添加class属性来寻找定位
Low_Temp = bsObJ.findAll("font", {"color": "#006600"})
Details_Of_Temp = bsObJ.find("ul",{"class": "tbox1"} ).get_text()

# def Temp1(x, y1, y2, z):
#      a = urlopen(x)
#      b = BeautifulSoup(a.read())
#      Temp = b.findAll(y1, y2)
#      for  temp in Temp:
#           print(z, temp.get_text().encode('utf-8').decode('utf-8'))
#Imgs = bsObJ.findAll('img', {'src': re.compile("\.\.\/img\/gifts/img.*\.jpg")})
#Images = bsObJ1.findAll('img', {'src': re.compile("")})
# for Img in Imgs:
#     print(Img['src'])
print('当前位置: 山东济南')
print('当地时间:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
for Temp_High in  High_Temp:
     print('最高温度:',Temp_High.get_text().encode('utf-8').decode('utf-8'))

for Temp_Low in  Low_Temp:
     print('最低温度:',Temp_Low.get_text().encode('utf-8').decode('utf-8'))

for Temp_Of_Details in Details_Of_Temp:
     print(Temp_Of_Details.encode('utf-8').decode('utf-8'), end='')

#c = Temp1('http://jinan.tianqi.com/today/', "font", {"color": "red"}, '最高气温:')
s = Temp_Of_Details.encode('utf-8').decode('utf-8')
# s1 = []
# s1 = s
# f = open('test.txt' , 'w')
# f.write(s1)
# f.close()
print(repr(s))