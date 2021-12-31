# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''


# class represents a lanternfish
import os


class Lanternfish():

    def __init__(self, start_day):
        self.start_day = start_day

    def minus_day(self):
        self.start_day -= 1
        if self.start_day < 0:
            self.start_day = 6

    def get_day(self):
        return self.start_day


def load_file():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    inp = []
    with open(ROOT_DIR + "\input.txt", "r") as file:
        for num in file.read():
            if num.isdigit():
                inp.append(int(num))
    return inp


if __name__ == '__main__':
    days = [3, 4, 3, 1, 2]
    fishes = []
    # days = load_file()
    # create fishes
    for day in days:
        fishes.append(Lanternfish(day))

    # subtract day per fisch
    for i in range(80):
        for fish in fishes:
            if fish.get_day() == 0:
                fishes.append(Lanternfish(9))
                fish.minus_day()
            else:
                fish.minus_day()

    print(f"Total Fische: {len(fishes)}")
