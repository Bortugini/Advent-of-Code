# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
# inp = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
# solution 150
import os.path

inp = []


def read_file():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    global inp
    inp = []
    with open(ROOT_DIR + "\data.txt", "r") as file:
        for line in file.readlines():
            inp.append(line)


# solution of part 1
def part_1():
    global inp
    depth = 0
    horizontal = 0
    for i in inp:
        if "forward" in i:
            horizontal += int(i.split(" ")[1])
        if "down" in i:
            depth += int(i.split(" ")[1])
        if "up" in i:
            depth -= int(i.split(" ")[1])
    print(f"Resultat part 1 ist: {depth * horizontal}")


# solution of part 2
def part_2():
    global inp
    depth = 0
    horizontal = 0
    aim = 0
    for i in inp:
        if "forward" in i:
            horizontal += int(i.split(" ")[1])
            depth += int(i.split(" ")[1]) * aim
        if "down" in i:
            aim += int(i.split(" ")[1])
        if "up" in i:
            aim -= int(i.split(" ")[1])
    print(f"Tiefe ist: {depth}")
    print(f"Horizontal ist: {horizontal}")
    print(f"Resultat part 2 ist: {depth * horizontal}")


if __name__ == '__main__':
    read_file()
    part_1()
    part_2()
