#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import re
import sys
import base64
from bs4 import BeautifulSoup
from time import *

start_time = time()
#需要手动在cookie.txt里面输入cookie
f_cookie = open('./cookie.txt','r',encoding='utf-8')
cookie = f_cookie.readline()
cookie = cookie.strip('\n')
f_cookie.close()

#配置headers，建立连接
user = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Referer': 'http://lexue.bit.edu.cn/',
    'Cookie': cookie, 
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    }
#通过抓包获取全部headers

url = 'http://lexue.bit.edu.cn/calendar/view.php'              
#乐学通知地址

ddl_name = []
ddl_clas = []
ddl_time = []
ddl_desc = []
#ddl名称、课程归属、截止时间、描述

def spider(url):
    response = requests.get(url,headers = user)
    flag = response.status_code
    # 记录状态码
    # print("Status code:{}\n".format(flag))      

    if flag!=200:
        print("Error code:{}".format(flag))
        sys.exit(0)

    html = response.text                             
    # 用文本显示访问网页得到的内容
    sss = "统一身份认证"
    if sss in html:
        print("登录失败，请输入正确的cookie")
        sys.exit(0)
    soup = BeautifulSoup(html,'html.parser')
    #用BeautifulSoup进行封装，使用html解析器

    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    # 把soup里面的scrip和style清理掉

    content = soup.find_all(name='div',attrs={"class":"eventlist my-1"},)
    #找到全部通知信息
    return content

def handle(content):
    total = []
    for x_cont in content:
        total = x_cont.find_all(name='h3',attrs={"class":"name d-inline-block"})
    #收集ddl名称
    for name in total:
        x_name = name.get_text()
        # print(x_name)
        ddl_name.append(x_name)


    for x_cont in content:
        total = x_cont.find_all(name='div',attrs={"class":"col-xs-11"})

    cnt = 0
    for item in total:
        item_cont = item.get_text()
        if cnt % 4 == 0:
            ddl_time.append(item_cont)
        if cnt % 4 == 2:
            ddl_desc.append(item_cont)
        if cnt % 4 == 3:
            ddl_clas.append(item_cont)
        cnt = cnt + 1

def check(x,y,z,t):
    if x==y and y==z and z==t:
        return True
    else:
        return False
#检查bug，检查各项数目是否相等

def output():
    name_num = len(ddl_name)
    time_num = len(ddl_time)
    desc_num = len(ddl_desc)
    clas_num = len(ddl_clas)
    flag = check(name_num,time_num,desc_num,clas_num)
    # print(flag)
    length = name_num
    if flag:
        for i in range(length):
            print("事项：{name}\n课程：{clas_name}\n截止日期：{time}\n描述：{desc}\n\n".format(name=ddl_name[i],clas_name=ddl_clas[i],time=ddl_time[i],desc=ddl_desc[i]))
        f = open("./ddl.md",'w', encoding='utf-8')
        f.write("# 近期ddl\n")
        for i in range(length):
                f.write("事项：{name}\n课程：{clas_name}\n截止日期：{time}\n描述：{desc}\n\n---\n".format(name=ddl_name[i],clas_name=ddl_clas[i],time=ddl_time[i],desc=ddl_desc[i]))
        f.close()
        print("ddl.md 已生成")
    else:
        print("Something went wrong!!!")
        sys.exit(0)


end_time = time()
print("\nrunning time: {:.7}s".format(end_time-start_time))
#统计运行时间

if __name__ == "__main__":
    handle(spider(url))
    output()