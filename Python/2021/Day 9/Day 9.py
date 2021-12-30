# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''


# method to load data from a file
def load_file():
    inp = []
    with open("/Advent of Code/2021\Day 8\input.txt", "r") as file:
        for i in file.readlines():
            inp.append(i.replace(f"\n", ""))
    return inp


# returns a list with tuples [(row, col), (row, col), (row, col), (row, col)]
def get_points(row, col, inp):
    # first row
    if row == 0:
        # first number
        if col == 0:
            return [(row + 1, col), (row, col + 1)]
        # last number
        elif col == len(inp[row]) - 1:
            return [(row + 1, col), (row, col - 1)]
        else:
            return [(row + 1, col), (row, col + 1), (row, col - 1)]
    # last row
    elif row == len(inp) - 1:
        # first number
        if col == 0:
            return [(row - 1, col), (row, col + 1)]
        # last number
        elif col == len(inp[row]) - 1:
            return [(row - 1, col), (row, col - 1)]
        else:
            return [(row - 1, col), (row, col + 1), (row, col - 1)]
    # middle rows
    else:
        # first number
        if col == 0:
            return [(row + 1, col), (row, col + 1), (row - 1, col)]
        # last number
        elif col == len(inp[row]) - 1:
            return [(row + 1, col), (row, col - 1), (row - 1, col)]
        else:
            return [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]


def is_lowest_point(row, col, inp):
    points = get_points(row, col, inp)
    for point in points:
        print(point[0], point[1])

def find_lowest_points(inp):
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            is_lowest_point(row, col, inp)


if __name__ == '__main__':
    inp = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
           [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
           [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
           [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
           [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]

    find_lowest_points(inp)
