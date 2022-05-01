# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022
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
        print(self.newlist[finalOpen:firstClosed])           

def main():
    s = "((a+b)c)*"
    newobject = genfa()
    newobject.Parse_Input(s)
    newobject.checkForMid()
    return 0

main()



