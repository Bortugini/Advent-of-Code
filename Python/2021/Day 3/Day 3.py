# _*_ coding: utf-8 _*_
'''
Created on

@author: Thomas
'''
# bytes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
bytes = []


def read_file():
    global bytes
    bytes = []
    with open("/Advent of Code/2021\Day 3\Data.txt", "r") as file:
        for line in file.read().split():
            bytes.append(line)


def most_bit(bytes, bit, invert=False):
    count_zero = 0
    count_one = 0
    for i in range(len(bytes)):
        if bytes[i][bit] == "0":
            count_zero += 1
        else:
            count_one += 1
    if count_one > count_zero:
        if invert:
            return "0"
        else:
            return "1"
    elif count_one == count_zero:
        return "e"
    else:
        if invert:
            return "1"
        else:
            return "0"


def del_bytes(byte, bit, target):
    nums = []
    for num in byte:
        if num[bit] in target:
            nums.append(num)

    return nums


def get_byte(bytes, invert=False):
    for bit in range(12):
        if len(bytes) == 1:
            break
        most = most_bit(bytes, bit, invert)
        if most in "1":
            bytes = del_bytes(bytes, bit, "1")
        elif most in "0":
            bytes = del_bytes(bytes, bit, "0")
        else:
            if invert:
                bytes = del_bytes(bytes, bit, "0")
            else:
                bytes = del_bytes(bytes, bit, "1")
    return bytes


def part_1():
    gamma = ""
    epsilon = ""
    for bit in range(12):
        if most_bit(bytes, bit) in "1":
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        # 11
        if bit == 11:
            print(f"Lösung 1: {int(gamma, 2) * int(epsilon, 2)}")


def part_2():
    oxygen = int(get_byte(bytes)[0], 2)
    co2 = int(get_byte(bytes, True)[0], 2)
    print(f"Lösung 2: {oxygen * co2}")


if __name__ == '__main__':
    read_file()
    part_1()
    part_2()