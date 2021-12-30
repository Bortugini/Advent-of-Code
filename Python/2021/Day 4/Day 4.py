# _*_ coding: utf-8 _*_
"""
Created on

@author: Thomas
"""
import numpy as np

# numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
# fields = [
#     [[22, 13, 17, 11, 0],
#      [8, 2, 23, 4, 24],
#      [21, 9, 14, 16, 7],
#      [6, 10, 3, 18, 5],
#      [1, 12, 20, 15, 19]],
#
#     [[3, 15, 0, 2, 22],
#      [9, 18, 13, 17, 5],
#      [19, 8, 7, 25, 23],
#      [20, 11, 10, 24, 4],
#      [14, 21, 16, 12, 6]],
#
#     [[14, 21, 17, 24, 4],  # winner Line
#      [10, 16, 15, 9, 19],  # summ of all unmarked nums = 188
#      [18, 8, 23, 26, 20],  # multiply with the last num 188 * 24 = 4512
#      [22, 11, 13, 6, 5],
#      [2, 0, 12, 3, 7]
#      ]]
numbers = []
fields = []


def inp():
    global numbers
    global fields
    with open("/Advent of Code/2021\Day 4\input.txt", "r") as file:
        numbers = [np.uint8(number) for number in file.readline().strip().split(",")]
        raw_sheets = file.readlines()
        for i in range(0, len(raw_sheets), 6):
            temp_sheet = []

            for j in range(i + 1, i + 6):
                temp_sheet.append(
                    [np.uint8(number) for number in raw_sheets[j].split()]
                )

            fields.append(temp_sheet)


def find_num(board, num, board_pos):
    for i in range(len(board)): # row
        for j in range(len(board[0])): # col
            if board[i][j] == num:
                board[i][j] = "X"
                check(board, num)
    return board


def check_col(board):
    column = []
    for j in range(len(board[0])):  # col
        column.clear()
        for i in range(len(board)):  # row
            column.append(board[i][j])
        if column == ["X", "X", "X", "X", "X"]:
            return True
    return False


def check(board, num):
    value = 0
    if board[0] == ["X", "X", "X", "X", "X"] or check_col(board):
        print(calc(board, num, value))


def calc(board, num, value):
    for line in board:
        if not ["X", "X", "X", "X", "X"] == line:
            for number in line:
                if not "X" == number:
                    value += number

    return value * num

if __name__ == '__main__':
    positions = []  # row col board
    field_pos = 0
    inp()
    for num in numbers:
        for field in fields:
            field = find_num(field, num, field_pos)
    print(positions)