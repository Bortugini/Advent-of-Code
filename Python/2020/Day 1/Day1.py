# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(ROOT_DIR + "/numbers") as file:
    numbers = list(map(int, file.readlines()))

numbers = [1721, 979, 366, 299, 675, 1456]

for x in numbers:
    for y in numbers:
        if x + y == 2020:
            print(x * y)
            break
    else:
        continue
    break

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x+y+z == 2020:
                print(x*y*z)
                break
        else:
            continue
        break
    else:
        continue
    break