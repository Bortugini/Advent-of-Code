# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''


# crab class represents a crab-submarine
class Crab:

    def __init__(self, position):
        self.position = position
        self.fuel = 0

    def set_position(self, position):
        if self.position > position:
            self.fuel = self.position - position
        else:
            self.fuel = position - self.position

    def set_fuel(self):
        self.fuel = 0

    def get_fuel(self):
        return self.fuel


# method to load data from a file
def load_file():
    inp = []
    with open("/Advent of Code/2021\Day 7\Input.txt", "r") as file:
        for num in file.readline().split(","):
            if num.isdigit():
                inp.append(int(num))
    return inp


if __name__ == '__main__':
    inp = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    inp = load_file()
    crabs = []
    # generate crabs
    for num in inp:
        crabs.append(Crab(num))
    # calculate the fuel for every position and stores the sum on sum_of_fuel
    sum_of_fuel = [0] * len(crabs)
    for i in range(len(crabs)):
        for crab in crabs:
            crab.set_position(i)
            sum_of_fuel[i] += crab.get_fuel()
            crab.set_fuel()

    print(f"Bestes ergebnis ist: {sum_of_fuel.index(min(sum_of_fuel))} mit {min(sum_of_fuel)} Fuel")
