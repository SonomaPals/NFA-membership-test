# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022
class genfa:
    def __init__(self):
        self.parseList = []
        
    def Parse_Input(self, s):
        self.parseList = []

        for i in s:
            self.parseList.append(i.split())

        print(self.parseList)


def main():
    s = "((a+b)c)*"
    newobject = genfa()
    newobject.Parse_Input(s)
    return 0

main()



