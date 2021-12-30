# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(ROOT_DIR + "/list") as file:
    li = file.readlines()

valid = 0
valid_two = 0
reg_ex = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
for i in li:
    match = re.search(reg_ex, i)
    min = int(match.group(1))
    max = int(match.group(2))
    char = match.group(3)
    pw = match.group(4)
    con = pw.count(char)
    if con >= min and con <= max:
        valid += 1
    #two
    if pw[max-1] == char and not pw[min-1] == char:
        valid_two +=1
    elif pw[min-1] == char and not pw[max-1] == char:
        valid_two +=1

print(valid)
print(valid_two)