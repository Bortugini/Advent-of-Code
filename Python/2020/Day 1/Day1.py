# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''

with open("D:/Programirung/Pycharm/Python/Advent of Code/2020/Day 1/numbers") as file:
    numbers = list(map(int, file.readlines()))

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x+y+z == 2020:
                print(x*y*z)