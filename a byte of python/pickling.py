#!/usr/bin/python
#coding=utf-8
# Filename: pickling.py 
import pickle
# the name of the file where we will store the object 
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = open(shoplistfile, 'wb') 
pickle.dump(shoplist, f) # 转储对象到文件 
f.close()

del shoplist # 销毁 shoplist 变量
# 从文件找回对象
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # 从文件加载对象 
print(storedlist)