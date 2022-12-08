# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
import os
elfs = []
elf = []
calories = 0
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(ROOT_DIR + "/calories") as file:
    for line in file:
        if line in '\n':
            print("Leer")
            calories = sum(elf)
            elfs.append(calories)
        else:
            elf.append(int(line))

print(elfs)