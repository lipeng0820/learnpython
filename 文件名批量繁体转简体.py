# -*- coding: utf-8 -*-

#使用钱需要安装 pip install zhconv

from operator import length_hint
import zhconv
import os
FilePath = input("请粘贴入文件夹路径：") + "/"

#获取该目录下所有文件，存入列表中
FileList = os.listdir(FilePath)

n = 0

for i in FileList:

    #跳过隐藏文件
    Scaner = i[0:2]
    if Scaner == "._":
        print("已跳过隐藏文件")
        n+=1
        continue


    else:
        #定义旧文件名（此为路径+文件名）
        TrName = FilePath + os.sep + FileList[n]   # os.sep添加系统分隔符

        #测文件名长度
        #文件名带路径的长度为:
        TrName_Length = len(TrName)
        #文件名长度
        FileNane_Length = len(i)
        Show_NewName = TrName[TrName_Length-FileNane_Length : TrName_Length+1]

        #繁中转换
        SimName = zhconv.convert(TrName,'zh-hans')

        #设置新文件名
        SimNewName = FilePath + os.sep + SimName

        os.chdir(FilePath)
        os.renames(TrName,SimName)   #用os模块中的rename方法对文件改名
        
        print("已将文件名由繁体:" + i ,"转换为简体=>",Show_NewName)
        n+=1
        
print("转换已结束")
    
    