# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''


# method to load data from a file
import os


def load_file():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    inp = []
    with open(ROOT_DIR + "\input.txt", "r") as file:
        for i in file.readlines():
            inp.append(i.replace(f"\n", ""))
    return inp


def sort_and_split(raw_inp):
    raw_inp = split(raw_inp)
    inp = []
    for i in raw_inp:
        i = sorted(i)
        inp.append("".join(i))
    return inp


def split(raw_inp):
    inp = []
    for a in raw_inp:
        a = a.split("|")
        a = a[1].split(" ")
        for b in a:
            if not b in "":
                inp.append(b)
    return inp


def detect_segment(li_inp):
    count = 0
    for inp in li_inp:
        if len(inp) == 2 or len(inp) == 3 or len(inp) == 4 or len(inp) == 7:
            count += 1
    return count


if __name__ == '__main__':
    raw_inp = load_file()
    inp = sort_and_split(raw_inp)
    print(detect_segment(inp))

