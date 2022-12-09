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
    lines = file.readlines()

for i in range(len(lines)):
    if lines[i] in '\n' or i == len(lines) - 1:
        if i == len(lines) - 1:
            elf.append(int(lines[i]))
        calories = sum(elf)
        elf.clear()
        elfs.append(calories)
    else:
        elf.append(int(lines[i]))


print("Part 1 " + str(max(elfs)))
print("Part 2 " + str(sum(sorted(elfs)[-3:])))