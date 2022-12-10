# _*_ coding: utf-8 _*_
'''
Created on

A = rock      1 points
B = paper     2 points
C = scissors  3 points

X = rock      1 points
Y = paper     2 points
Z = scissors  3 points

points
Lose  = 0
Draw  = 3
Win   = 6

@author: Thomas
'''
import os
games = []
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(ROOT_DIR + "\strategy.txt") as file:
    for line in file:
        line = line.strip()
        games.append(line)
# Part 1
choices = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
points_choice = {"rock": 1, "paper": 2, "scissors": 3}
points_result = {"lose": 0, "draw": 3, "win": 6}

points = 0
for game in games:
    opponent_choice = choices[game[0]]
    my_choice = choices[game[2]]
    if opponent_choice == my_choice:
        points += points_result["draw"] + points_choice[my_choice]
    elif (opponent_choice, my_choice) in [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")]:
        points += points_result["lose"] + points_choice[my_choice]
    else:
        points += points_result["win"] + points_choice[my_choice]

print("Part 1 " + str(points))

# Part 2
choices = {"A": "rock", "B": "paper", "C": "scissors", "X": "lose", "Y": "draw", "Z": "win"}

points = 0
for game in games:
    opponent_choice = choices[game[0]]
    my_choice = choices[game[2]]
    if (opponent_choice, my_choice) in [("paper", "draw"), ("rock", "win"), ("scissors", "lose")]:
        points += points_result[my_choice] + points_choice["paper"]
    elif (opponent_choice, my_choice) in [("paper", "lose"), ("rock", "draw"), ("scissors", "win")]:
        points += points_result[my_choice] + points_choice["rock"]
    else:
        points += points_result[my_choice] + points_choice["scissors"]

print("Part 2 " + str(points))