# -*- coding: cp936 -*-
import hashlib
import time
import os
import re
import urllib2,json
import random
def read(web):
    s=urllib2.urlopen(web).read()
    return s

def  getenglish(which):
    '''
       input a character , return a chinese word. 
    '''
    text=read('http://www.xiexingcun.com/cihai/'+which+'.htm')
    n = len(text)
    num = 1
    for i in range(0,len(text)-1):
        if(text[i] =='\n'):
            num = num+1;
    #print '一共',num,'行'
    num = num -43-19;
    num2 = random.randint(1, num)
    if(num2<1000 and num2>99):
        num2 = '0'+str(num2)
    elif(num2<100 and num2>9):
        num2 = '00'+str(num2)
    elif(num2<10):
        num2 = '000'+str(num2)
    else:
        num2 = str(num2)
    #print num2
    myre=re.compile(r'<title>.+</title>')
    text=read('http://www.xiexingcun.com/cihai/'+which+'/'+which+num2+'.htm')
    A=myre.findall(text)
    A = ''.join(A)
    A = A[7:-29]
    return ''.join(A)
# 获取 ted
def  getted():
    #myre=re.compile('\<dd class="mt15"\>.*country.*class.*span\>')
    myre=re.compile(r'"tTitle":"[\w\s:]+",')
    text=read('http://www.ted.com/')
    print text
    A=myre.findall(text)
    for x in range(len(A)):
        A[x]=A[x][10:-2]+'\n'
    return ''.join(A)

def get_random():
    words = 'abcdefghjklmnopqrstwxyz'
    while(1):
        num1 = random.randint(0, 22)
        hou_zhui = []
        hou_zhui.append(words[num1])
        A = getenglish(hou_zhui[0]);
        if(len(A)>=2):
            return A;
def main():
    words = 'abcdefghjklmnopqrstwxyz'
    while(1):
        raw_input("idea boost!!!");
        A = get_random();
        B = get_random();
        print A+"和"+B
main();
