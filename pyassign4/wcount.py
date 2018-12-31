#!/usr/bin/env python3

"""
wcount.py: count words from an Internet file.

__author__ = "Wang Zekun"
__pkuid__  = "1800011717"
__email__  = "wangzekun@pku.edu.cn"
"""

import sys
import urllib.request 
from urllib.request import urlopen


#-----------------------------------------------------------------------
#字数统计使用的函数
#-----------------------------------------------------------------------
def replace(strx,replist,reptar): 
    #替换函数，将strx包含的replist列表中每个字符串替换为目标字符串reptar
    for note in replist:
        strx = strx.replace(note,reptar)
    return strx

def removeNone(grp):
    #去除列表grp中空字符串的函数
    newgrp = []
    for obj in grp:
        if obj != '':
            newgrp.append(obj)
    return newgrp

def arrange(dictx,topn):
    #对于得到的单词计数进行统计，返回出现次数最多的topn个单词和它们的出现次数
    if topn > len(dictx):
        topn = len(dictx)
    anslis = []
    valuelist = list(dictx.values())
    valuelist.sort(reverse = True)
    for i in range(topn):
        if valuelist[i] != valuelist [i-1]:
            for words in list(dictx.keys()):
                if dictx[words] == valuelist[i]:
                    anslis.append((words,valuelist[i]))
    return anslis

def wcount(docstr,topn = 10):
    worddict = {}

    formatted = replace(docstr,['\r','\n','\\r\\n','\\xef','\\xbb','\\xbf','.',
                                "'",'[',']',':',',','*','_','#','&','--','!',
                                '?','"','@',';','\\','(',')','$','/'],' ').lower()
    #将url返回的字符串进行格式化（去除标点和转化小写）
    
    wordcol = removeNone(formatted.split(' ')) #分割字符串，并去除得到的列表的空字符串

    for word in wordcol[50:-100]: #统计每个单词的出现次数,去除首尾附加的网站信息等
        if word not in worddict:
            worddict[word] = 1
        elif word in worddict:
            worddict[word] += 1
        
    ans = arrange(worddict,topn)
    return ans



#-----------------------------------------------------------------------
#主函数
#-----------------------------------------------------------------------
def main():
    
    if len(sys.argv) == 1: #无URL时的输出
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    #
    try:
        doc = urlopen(sys.argv[1])
        
    except ValueError: #捕获错误输入
        print('Invalid URL input!')
        
    except urllib.request.HTTPError as e: #捕获http error
        print('Something wrong with the web.')
        print('ErrorType:',"'",e,"'")
        
    except urllib.request.URLError as e: #捕获url error
        print('Bad Internet connection or invalid URL.')
        print('ErrorType:',"'",e,"'")
        
    else:  #正常工作
        doc = urlopen(sys.argv[1])
        docstr0 = doc.read()
        doc.close()
        docstr = str(docstr0)
    
        if len(sys.argv) == 3: #统计给定值的前几名
            ans = wcount(docstr,int(sys.argv[2]))
        if len(sys.argv) == 2: #统计前十名（缺省）
            ans = wcount(docstr)
    
        for obj in ans: #输出结果，为了确保对齐，按照字符长度进行分类打印
            if len(obj[0])<=7:
                print(obj[0] + '\t'*2 + str(obj[1]))
            else:
                print(obj[0] + '\t' + str(obj[1]))
            
    
if __name__ == '__main__':
    main()

