#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import re
import base64
import bs4
from bs4 import BeautifulSoup
from time import *

start_time = time()
#----------------------------------------------------------------
#配置headers，建立连接
user = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Referer': 'http://lexue.bit.edu.cn/',
    
    #-------------------------通过cookie登陆校园网------------------------
    'Cookie': '', #这里复制自己的cookie    
    #-------------------------通过cookie登陆校园网------------------------
    
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
    }
#通过抓包获取全部headers

url = 'http://lexue.bit.edu.cn/calendar/view.php'              
#乐学通知地址

response = requests.get(url,headers = user)
flag = response.status_code
#记录状态码
print("Status code:{}\n".format(flag))      
#显示状态码

html = response.text                             
#用文本显示访问网页得到的内容

soup = BeautifulSoup(html,'html.parser')
#用BeautifulSoup进行封装，使用html解析器

[script.extract() for script in soup.findAll('script')]
[style.extract() for style in soup.findAll('style')]
#把soup里面的scrip和style清理掉


content = soup.find_all(name='div',attrs={"class":"eventlist"},)
#找到全部通知信息
# print(content)

ddl_name = []
ddl_clas = []
ddl_time = []
ddl_desc = []
#ddl名称、课程归属、截止时间、描述

for x_cont in content:
    total = x_cont.find_all(name='h3',attrs={"class":["referer","name"]})
#收集ddl名称
for name in total:
    x_name = name.get_text()
    # print(x_name)
    ddl_name.append(x_name)


for x_cont in content:
    total = x_cont.find_all(name='div',attrs={"class":"course"})
#收集ddl课程归属
for clas in total:
    x_clas = clas.get_text()
    # print(x_clas)
    ddl_clas.append(x_clas)


for x_cont in content:
    total = x_cont.find_all(name='span',attrs={"class":"date"})
#收集ddl时间
for ttime in total:
    x_time = ttime.get_text()
    # print(x_time)
    ddl_time.append(x_time)


for x_cont in content:
    total = x_cont.find_all(name='div',attrs={"class":"description"})
#收集ddl内容
for desc in total:
    x_desc = desc.get_text()
    # print(x_desc)
    ddl_desc.append(x_desc)


def check(x,y,z,t):
    if x==y and y==z and z==t:
        return True
    else:
        return False
#检查bug，检查各项数目是否相等


name_num = len(ddl_name)
time_num = len(ddl_time)
desc_num = len(ddl_desc)
clas_num = len(ddl_clas)

flag = check(name_num,time_num,desc_num,clas_num)
# print(flag)

if flag:
    # for i in range(name_num):
    #     print("事项：{name}\n课程：{clas_name}\n截止日期：\n{time}\n描述：{desc}\n\n".format(name=ddl_name[i],clas_name=ddl_clas[i],time=ddl_time[i],desc=ddl_desc[i]))
    f = open("./ddl.md",'w')
    f.write("#近期ddl\n")
    for i in range(name_num):
            f.write("事项：{name}\n课程：{clas_name}\n截止日期：\n{time}\n描述：{desc}\n\n".format(name=ddl_name[i],clas_name=ddl_clas[i],time=ddl_time[i],desc=ddl_desc[i]))
    f.close()
else:
    print("Something went wrong!!!")


end_time = time()
print("\nrunning time: {:.7}s".format(end_time-start_time))
#统计运行时间