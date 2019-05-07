# this is hill climbing algorithm
# the goal is to simulate the infinite monkey theorem
# main concept is keep trying, and only print if the result better than last time

import random

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]

    return res

def score(goal, teststring):
    numScore = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numScore = numScore + 1

    return numScore / len(goal)

def main():

    goalString = "methinks it is like a weasel"
    newString = generateOne(28)
    best = 0
    newScore = score(goalString, newString)
    while newScore < 1:
        if newScore > best:
            print(newString)
            best = newScore
        newString = generateOne(28)
        newScore = score(goalString, newString)

main()