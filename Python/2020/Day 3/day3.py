# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(ROOT_DIR + "/map") as file:
    lines = file.readlines()
count = 0
index = 0
for i in lines:
    print(index, len(i) - 1)
    if index >= len(i)-1:
        if index == len(i)-1:

            if i[index] == "#":
                count += 1
            index = 2
            continue
        else:
            index = len(i)-1 - (index-3)
            continue
    if i[index] == "#":
        count += 1
    index += 3

print(count)