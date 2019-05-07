# -*- coding: UTF-8 -*-
'''
Author: Sam Yang
Description: This program is a practice from:
http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#a-fraction-class
it is aim to simulate a fraction by implement the show, +, -, *, /, equal, less than, great than method of fraction.
'''

# find GCD = greatest common divisor, using Euclid's Algorithm
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom
    
    # override the built-in str method, the original one will return the reference of the instance
    def __str__(self):
        
        return str(self.num) + "/" + str(self.den)

    # override the built-in add method
    def __add__(self, otherFraction):

        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    # override the built-in sub method
    def __sub__(self, otherFraction):
        
        newNum = self.num * otherFraction.den - self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)


    # override the built-in mul method
    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)
        
    # override the built-in div method
    def __truediv__(self, otherFraction):
        newNum = self.num * otherFraction.den
        newDen = self.den * otherFraction.num
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    # override the built-in eq method, the original one is shallow equality, that means, only when the two object has sam reference, will return true
    def __eq__(self, otherFraction):
        
        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den

        return firstNum == secondNum 

    # override the built-in lt method
    def __lt__(self, otherFraction):

        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den

        return firstNum < secondNum

    # override the built-in gt method
    def __gt__(self, otherFraction):

        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den

        return firstNum > secondNum

f1 = Fraction(2,5)
f2 = Fraction(2,4)
f3 = f1 / f2
print(f3)