# lexue_ddl
#### 概述

本项目是一个十分简陋的爬虫示例，设计初衷只是想避免翻阅北理乐学的通知，结果做完之后遇到了站点重构......那就只好也重构一下爬虫了（x）......然后顺手做了一个词云

* version:1.3
* author：xiabee
* 主要功能：`BIT乐学`通知事项的爬取、词云制作
* 依赖：`requests,re,base64,bs4,time`等
* 登陆方法：cookie登陆



#### 目录结构

```
├── cookie.txt
├── ddl.md
├── main.py
├── README.md
├── requirements.txt
└── wordcloud
    ├── cloud.py
    ├── love.jpg
    ├── __pycache__
    │   ├── wordcloud.cpython-38.pyc
    │   └── wordcloud.cpython-39.pyc
    └── ttf
        ├── STCAIYUN.TTF
        ├── STXINGKA.TTF
        └── STZHONGS.TTF

3 directories, 12 files
```





#### 与上一版比较

* 北理乐学于`2020.5`做了一次大更新，故此脚本也替换了相关键值对的搜索
* 添加了错误信息处理，判断脚本是否登录
* 添加了`requirements.txt`，便于一键式导入依赖
* 添加了`词云`功能



#### 使用方法：

* 将自己登录乐学的cookie复制粘贴进`cookie.txt`中

* 在项目文件夹内打开终端，键入以下命令安装依赖：

  ```
  pip install -r requirements.txt
  ```

* 直接运行`main.py`或命令行运行`main.py`

  ```
  python3 main.py
  ```

* 程序将生成个`ddl.md`，大致内容如下：

  ```
  # 近期ddl
  
  事项：实验三报告和源码提交 已到期
  课程：操作系统课程设计-2020（3-6）
  截止日期：明天, 00:00
  描述：文件请用班号-学号-姓名-实验三，如07111803-1120170650-王同学-实验三打包 实验报告和实验源码
  
  ---
  
  事项：成老师班第五章作业提交链接。 已到期
  课程：计算机组成原理-2020
  截止日期：12月7日 星期一, 00:00
  描述：第五章作业5-4，5-10， 5-13，5-14，5-16，5-17，5-18截止12月7日 0:00
  
  ---
  ......
  ```

* 词云使用方法：

  * 进入`./wordcloud`文件夹

  * 直接运行或命令行运行`cloud.py`

  * ```
    cd wordcloud
    python3 cloud.py
    ```

#### 附录：寻找cookie：

* ①登陆乐学 

* ②在网页中按F12进入开发者模式 

* ③进入`Network`选项 

* ④找到`index.php`

* ⑤找到"`Request Headers`" 

* ⑥找到"`Cookie`"键值对 

* ⑦将其值复制填入到`cookie.txt`中

* 乐学`cookie`只能保持一周，一周过后需要更新`cookie`...

  密码登陆功能暂时没做，如果有时间的话（划掉）继续更新