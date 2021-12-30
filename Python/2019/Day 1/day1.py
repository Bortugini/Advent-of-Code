# _*_ coding: utf-8 _*_
'''
Created on
12/3 abrunden = 4 -2 = 2
100756 /3 abrunden = 33585 -2 =33583
@author: Thomas
'''
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(ROOT_DIR + "/fuel") as file:
    fuel = list(map(int, file.readlines()))
res = []
for i in fuel:
    res.append(int(i/3-2))
print(sum(res))