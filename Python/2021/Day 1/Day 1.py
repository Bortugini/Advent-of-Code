# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
datas = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# datas = []

# methode to read data from a file
def read_file():
    global datas
    with open("/Advent of Code/2021\Day 1\data.txt", "r") as file:
        for line in file.read().split():
            datas.append(int(line))

# methode of solution one
def part_1():
    global datas
    count = 0
    for i in range(len(datas) - 1):
        data = datas[i]
        data1 = datas[i + 1]
        if data < data1:
            count += 1
    print(count)

# methode of solution 2
def part_2():
    global datas
    count = 0
    for i in range(len(datas) - 3):
        sum = datas[i] + datas[i + 1] + datas[i + 2]
        sum1 = datas[i + 1] + datas[i + 2] + datas[i + 3]
        if sum < sum1:
            count += 1
    print(count)


if __name__ == '__main__':
    # read_file()
    part_1()
    part_2()
