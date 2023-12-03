import os
import random
import numpy as np
from numpy import *

txtfilepath = r"../labels" #原始txt文件所存文件夹，文件夹可以有一个或多个txt文件
savefilepath = r"../labels_new" #更改后txt文件存放的文件夹
total_txt = os.listdir(txtfilepath) # 返回指定的文件夹包含的文件或文件夹的名字的列表
num = len(total_txt)
list = range(num) #创建从0到num的整数列表
files = os.listdir(savefilepath)

for file in total_txt:
    filepath = os.path.join(txtfilepath, file)
    savepath = os.path.join(savefilepath, file)
    b = []
    with open(filepath, 'r', encoding='utf8') as f:
        print(f)
        while True:
            _ = f.readline()
            print(_)

            if _:
                b.append(_.split(' '))
            else:
                break

        for i in range(len(b)):
            print(b[i])
            if b[i][0] == '0':
                b[i][0] = '1'
            elif b[i][0] == '1':
                b[i][0] = '0'
    with open(savepath, 'w+', encoding='utf8') as f:
        for i in b:
            f.writelines(' '.join(i))

