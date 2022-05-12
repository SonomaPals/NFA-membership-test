# epsilonNFA file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

# Union = "+"
# +1 to numStates
# epsilon to start states of symbols between the "+" sign

# Concatenation = "."
# left side of "." symbol grab the final state
# right side of "." symbol grab the initain state
# set a epsilon transition from the final state of the left to the initial state of the right
# Note: There can be more than 1 symbols on either side, i.e. (a+b).c

# Star = "*"
# +1 to numStates
# epsilon transition to the previous start state from the new state
# epsilon transiton from the previous final state to the new state
# (Note: New state becomes a final state and start state)
class genfa:
    def __init__(self,s):
        self.newlist = list(s)
        self.lastParen = 0

    def populateTransitionTable(self):
        print(self.transition_table)
    
    def createTransitionTable(self,w,h,symbols):
        transition_table = []
        counter = 0
        for x in range(h):
            transition_table.append([x])
        for b in range(h):
            for i in range(len(symbols)+1): #adds a colums in each row. One for each symbols and one for epsilon
                transition_table[b].insert(counter+1," ")
        self.transition_table = transition_table
        self.populateTransitionTable()
    
    def lastParenIndexFinder(self):
        for x in range(len(self.newlist)):
            for j in range(len(self.newlist)):
                if (self.newlist[x] == ')'):
                    if(self.newlist[j] != ')'):
                        self.lastParen = x #found index of the last parentheses 
        return self.lastParen
                
    def expressionTree(self):
        self.lastParen
    
    
    # def checkForMid(self):
    #     countNumOfParen = 0
    #     foundFirstClosed = False
    #     for x in range(len(self.newlist)):
    #         if (self.newlist[x] == '('):
    #             countNumOfParen += 1
    #         if (self.newlist[x] == ')' and foundFirstClosed == False):
    #             foundFirstClosed = True
    #             firstClosed = x
    #         if (countNumOfParen > 1):
    #             if (self.newlist[x] == '('):
    #                 finalOpen = x + 1 # + 1 grabs the next index to get the char after the first opening (
    #     inner = []
    #     inner = self.newlist[finalOpen:firstClosed]
    #     NumSymbols = 0
    #     symbols = []
    #     for x in range(len(inner)):
    #         if inner[x] != '+':
    #             NumSymbols += 1
    #             symbols.append(inner[x])
    #     numStates = NumSymbols * 2 #2 States 
    #     w, h = NumSymbols, numStates
    #     self.createTransitionTable(w,h,symbols)
        
    def findSymbols(self):
        NumSymbols = 0
        symbols = []
        for x in range(len(self.newlist)):
            if str(self.newlist[x]).isalnum():
                symbols.append(self.newlist[x])
                NumSymbols += 1
        numStates = NumSymbols * 2 #2 States 
        w, h = NumSymbols, numStates
        self.createTransitionTable(w,h,symbols)
            
def main2():
    s = "((a+b).c)*" 
    newobject = genfa(s)
    newobject.findSymbols()
    print(newobject.lastParenIndexFinder())
    return 0

main2()



