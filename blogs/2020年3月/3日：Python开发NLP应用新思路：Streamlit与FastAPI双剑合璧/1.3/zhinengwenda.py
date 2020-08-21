#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
from lxml import etree
import jieba
import re
import sys,time
import os

'''
其中:
- requests库用来向搜索引擎搜索答案;
- lxml用来获取答案;
- jieba库用来提取问题以及做出问题分析
- re是处理语言的正则匹配库;
- sys以及time库用来调试输出效果
- os模块用来写入文件以搭建模式选择。
'''

# 实现逐字输出的效果
def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r") # /r 光标回到行首
    sys.stdout.flush() #把缓冲区全部输出
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

# 真正搭建的部分
# 首先我们要加载停用词，去除掉语言中无意义的词，比如“了”，“啊”等等
stop = [line.strip() for line in open('stopwords.txt',encoding='utf-8').readlines() ]

# 开始执行的判断输出一下，以及使用者的输入：
print("小智：您好，请问您需要问什么呢(对话（快，慢），可控制输出速度)")
input_word=input("我：")

#默认为慢速
print(input_word)
if input_word == "快":
        f = open("1.txt", "w")
        f.write("0")
        f.close()
elif input_word =='慢':
        f = open("1.txt", "w")
        f.write("1")
        f.close()

# 下面用Jieba分词，去除掉无用的停用词：
sd=jieba.cut(input_word,cut_all=False)
final=''
for seg in sd:
    #去停用词
        print(seg)
        if seg not in stop :
            final +=seg
 process=final

# 此时process是仅仅最简单语言的处理结果，为了适应更多语言习惯，
# 使用正则表达式匹配另一种语言习惯，一个“问”时的处理：
#匹配问后面全部内容
pat=re.compile(r'(.*?)问(.*)')
#一个“问”时的处理
try:
        rel=pat.findall(final)
        process=rel[0][1]
except:
        pass

# 另外再添加语言习惯，两个“问”的处理：
#两个问时的处理
try:
        rel=pat.findall(final)
        rel0=rel[0][1]
        print(rel0)
        rel1=pat.findall(rel0)
        process=rel1[0][1]
except:
        pass

# 这样输出的效果就可以适应多种语言习惯，为了区分问答句和模式选择句加入判断语句：
print("问题："+process)
if process=='':
        print("小智：OK")

# 在else中使用搜索引擎获取答案，首先使用请求头，百度百科网址：
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/63.0.3239.132 Safari/537.36'}

url=requests.get("https://baike.baidu.com/search/word?word="+process,headers=header)

# 为了防止中文乱码，编码使用原网页编码
        url.raise_for_status()
        url.encoding = url.apparent_encoding

# 下面使用匹配获取内容：
bject=etree.HTML(url.text)
        print(object)
#正则匹配搜索出来答案的所有网址
#获取词条
head =object.xpath('/html/head//meta[@name="description"]/@content')
#详细内容
para=object.xpath('/html/body//div[@class="para"]/text()')

# 然后为了判断提问者提出的问题是否可行，以及模式匹配的选择，加入判断：
result='小智：'
        for i in para:
            result+=i
        if result=='小智：':
            print("小智：对不起，我不知道")
        else:
            f = open("1.txt", "r")
            s=f.read()
            if s=="1":
                print_one_by_one(result)
            else:
                print(result)

# 然后循环执行问答系统即可：
while(True):
    if os.path.exists('1.txt'):
        chuli()
    else:
        f = open("1.txt", "w")
        f.write("1")
        f.close()
        chuli()


