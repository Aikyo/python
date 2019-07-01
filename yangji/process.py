#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding:gbk
import os, re
import time
import psutil
import datetime
import sys

def MemoryInfo(PythonProcess,BrowserProcess,title):
    pattern = re.compile(r'([^\s]+)\s+(\d+)\s.*\s([^\s]+\sK)')
    py = 'tasklist /fi "imagename eq ' + PythonProcess + '"' + ' | findstr.exe ' + PythonProcess
    chrome = 'tasklist /fi "imagename eq ' + BrowserProcess + '"' + ' | findstr.exe ' + BrowserProcess
    py_result = os.popen(py).read()
    py_result_list = py_result.split("\n")

    chrome_result = os.popen(chrome).read()
    chrome_result_list = chrome_result.split("\n")


    t1 = datetime.datetime.now()
    text = open( title + '.txt', 'a')

    text.write("*" * 10 + " current time  {}  ".format(t1)  +'*' * 10 + "\n")
    text.write(" CPU利用率 {}%".format(psutil.cpu_percent()) + "\n")
    text.write(" Memory利用率 {}%".format(psutil.virtual_memory().percent) + "\n")
    text.write(" python_chrome 线程内存使用情况 \n")
    for srcLine in py_result_list:
        srcLine = "".join(srcLine.split('\n'))
        if len(srcLine) == 0:
            break
        m = pattern.search(srcLine)
        if m == None:
            continue

        if str(os.getpid()) == m.group(2):
            continue
        ori_mem = m.group(3).replace(',','')
        ori_mem = ori_mem.replace(' K','')
        ori_mem = ori_mem.replace(r'\sK','')
        print(type(ori_mem))
        memEach = int(ori_mem)
        t = 'ProcessName:' + m.group(1) + '\tPID:' + m.group(2) + '\tmemory size:%.2f' % (memEach * 1.0 / 1024) + ' M' + "\n"
        text.write(t)
    for srcLine in chrome_result_list:
        srcLine = "".join(srcLine.split('\n'))
        if len(srcLine) == 0:
            break
        m = pattern.search(srcLine)
        if m == None:
            continue
        if str(os.getpid()) == m.group(2):
            continue
        ori_mem = m.group(3).replace(',', '')
        ori_mem = ori_mem.replace(' K', '')
        ori_mem = ori_mem.replace(r'\sK', '')
        print(type(ori_mem))
        # memEach = string.atoi(ori_mem)
        memEach = int(ori_mem)
        t = 'ProcessName:' + m.group(1) + '\tPID:' + m.group(2) + '\tmemory size:%.2f' % (memEach * 1.0 / 1024) + ' M' + "\n"
        text.write(t)

    text.close()
    print("*" * 58)

if __name__ == '__main__':

    title = sys.argv[1]
    seconds = sys.argv[2]
    PythonProcess = 'python.exe'
    ChromeProcess = 'chrome.exe'
    text = open( title + '.txt', 'w')
    memory = psutil.virtual_memory()
    text.write("server_info: CPU个数:{},内存容量:{} M".format(psutil.cpu_count(),memory.total/1024/1024) + "\n")
    text.write("log per {} seconds".format(seconds) + "\n")
    text.close()
    while True:
        MemoryInfo(PythonProcess,ChromeProcess,title)
        time.sleep(int(seconds))