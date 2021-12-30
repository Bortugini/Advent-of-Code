# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''

with open("D:/Programirung/Pycharm/Python/Advent of Code/2020/Day 3/map") as file:
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