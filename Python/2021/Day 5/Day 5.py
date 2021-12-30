# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
# inp = "0,9 -> 5,9" \
#       "8,0 -> 0,8" \
#       "9,4 -> 3,4" \
#       "2,2 -> 2,1" \
#       "7,0 -> 7,4" \
#       "6,4 -> 2,0" \
#       "0,9 -> 2,9" \
#       "3,4 -> 1,4" \
#       "0,0 -> 8,8" \
#       "5,5 -> 8,2"
#
# map_2d = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
map_2d = []
coordinates = []


def read_file():
    global coordinates
    inp = ""
    with open("/Advent of Code/2021\Day 5\input.txt", "r") as file:
        for line in file.readlines():
            inp += line
    coordinates = []  # column, row , column, row
    num = ()
    for line in inp.split("\n"):
        line = line.split("->")
        line = line[0].split(","), line[1].split(",")
        num = (int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1]))
        # filter all x and y coordinates
        if num[0] == num[2] or num[1] == num[3]:
            coordinates.append(num)
            num = ()


def create_map():
    global map_2d, coordinates
    greatest_x = 0
    greatest_y = 0
    # filter the greatest x and y
    for i in coordinates:
        for j in range(4):
            if j == 0 or j == 2:
                if i[j] > greatest_x:
                    greatest_x = i[j]
            else:
                if i[j] > greatest_y:
                    greatest_y = i[j]
    row = greatest_y + 1
    col = greatest_x + 1
    map_2d = [[0] * col for i in range(row)]


# part 1
def fill_map():
    for cor in coordinates:
        if cor[1] == cor[3]:
            if cor[0] > cor[2]:
                temp = cor[0]
                temp1 = cor[2]
                cor = list(cor)
                cor[0] = temp1
                cor[2] = temp
                cor = tuple(cor)
            for x in range(cor[0], cor[2] + 1):
                map_2d[cor[1]][x] += 1
        else:
            if cor[1] > cor[3]:
                temp = cor[1]
                temp1 = cor[3]
                cor = list(cor)
                cor[1] = temp1
                cor[3] = temp
                cor = tuple(cor)
            for x in range(cor[1], cor[3] + 1):
                map_2d[x][cor[0]] += 1


def count_map():
    count = 0
    for line in map_2d:
        for num in line:
            if num > 1:
                count += 1
    print(count)


def print_map():
    global map_2d
    for line in map_2d:
        print(line)


if __name__ == '__main__':
    read_file()
    create_map()
    fill_map()
    count_map()
    # print_map()
