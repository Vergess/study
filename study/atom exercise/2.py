#!/usr/bin/python
# -*- coding: UTF-8 -*-

#将字母转换为4*n的矩阵
def ord1(a):
    l = int(len(a)/4)
    x = [i for i in range(0,l)]
    for i in range(0,l):
        x[i]=[]
        for j in range(0,4):
            x[i].append(ord(a[i*4+j])-97)
    return x

#将4*1矩阵转化为文字
def chr1(a):
    for i in range(0,4):
        print(chr(a[i]))

#对数字矩阵进行加密转换
import numpy as np
a=np.array([[3,13,21,9],[15,10,6,25],[10,17,4,8],[1,23,7,2]])
b=np.array([[1,21,8,17]])
b=b.T
x=ord1('pleasesendmethebookmycreditcardnoissixonetwoonethreeeightsixzeroonesixeightfourninesevenzerotwoa')
for i in range(0,24):
    y=np.array([x[i]])
    print((a*y.T+b)%26)
    #t=y.tolist()
