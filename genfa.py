# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022
import random 
import numpy as np
from tabulate import tabulate
class genfa:
    def __init__(self):
        self.newlist = []
        
    def Parse_Input(self, s):
        self.newlist = list(s)

    def checkForMid(self):
        countNumOfParen = 0
        foundFirstClosed = False
        for x in range(len(self.newlist)):
            if (self.newlist[x] == '('):
                countNumOfParen += 1
            if (self.newlist[x] == ')' and foundFirstClosed == False):
                foundFirstClosed = True
                firstClosed = x
            if (countNumOfParen > 1):
                if (self.newlist[x] == '('):
                    finalOpen = x + 1 # + 1 grabs the next index to get the char after the first opening (
        inner = []
        inner = self.newlist[finalOpen:firstClosed]
        NumSymbols = 0
        symbols = []
        for x in range(len(inner)):
            if inner[x] != '+':
                NumSymbols += 1
                symbols.append(inner[x])
        numStates = NumSymbols * 2 #2 States 
        w, h = NumSymbols, numStates
        # a_2d_matrix = np.zeros((h,w))
        # print(a_2d_matrix)

def main():
    s = "((a+b).c)*" 
    newobject = genfa()
    newobject.Parse_Input(s)
    newobject.checkForMid()
    return 0

main()



