#！/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Administrator'

from bs4 import BeautifulSoup
from urllib.request import urlopen


# html = urlopen('http://jinan.tianqi.com/')
# bsObj = BeautifulSoup(html.read())
#
# Days_6 = bsObj.find('div', {'class': 'everytqshow'}, {'id': 'detail'}).get_text()
#
# print('山东济南天气预报一周，如下：')
# for  Details_Days_6 in Days_6:
#     print(Details_Days_6, end='')

html1 = urlopen('http://www.weather.com.cn/weather/101120101.shtml')
bsObj1 = BeautifulSoup(html1.read())
Days_7 = bsObj1.find("ul", {"class": "t clearfix"}).get_text()

for  Details_Days_7 in Days_7:
    print(Details_Days_7.encode('utf-8').decode('utf-8'), end='')
    # s = Details_Days_7.encode('utf-8').decode('utf-8')
    # s1 = s.strip()
    # for tt in s1:
    #     print(tt)
f1 = Details_Days_7.encode('utf-8').decode('utf-8')
# f2 = 'a aaa     aaa   aa'
# for f3 in f2:
#     print(f3 , end='')
#     f3 = f3.strip()
# f = open('test.txt' , 'w')
# f.write(f3)
# f.close()
print(repr(f1))