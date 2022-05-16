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

from calendar import c
from hashlib import new

from regex import E


class Type:
    SYMBOL = 1
    CONCAT = 2
    UNION  = 3
    STAR = 4

class Exp_Tree:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.left = None
        self.right = None
        self.checked = 0
        
def UnionEndOfTreeHelper(et): 
        global currentState #Re-tell python to use global version
        #----
        #Side left
        #----  
        left = {}
        transitionListleft = []
        x = et.left.value #Will be key of nested dictionary
        left[x] = transitionListleft #nestedDictionary
        Dict[currentState] = left #inserting the dict 'a' into the dict
        left[x] += [currentState+1]
        startingStatesList.append(currentState)
        finalStateList.append(currentState+1)
        #----
        #Side right
        #----
        currentState = 2 + currentState 
        right = {}
        transitionListright = []
        y = et.right.value
        right[y] = transitionListright
        Dict[currentState] = right #inserting the dict 'a' into the dict
        right[y] += [currentState+1]
        startingStatesList.append(currentState)
        finalStateList.append(currentState+1)
        addEpsilon(currentState+2)
        #print(startingStatesList,finaleSateList)
        #print(Dict)

def addEpsilon(NextState):
    global nestedEpsilon
    global curStartState 
    nestedEpsilon = {}
    nestedEpsilon['e'] = []
    Dict[NextState] = nestedEpsilon 
    curStartState = NextState
    
def unionTable(et):
    global newStartState
    global currentState
    global curStartState 
    et.checked = 1
    if et.left.checked == 0:
        newStartState = (curStartState)
        Dict[curStartState]['e'] += startingStatesList
        while len(startingStatesList) != 0: #take previous start states off 
            startingStatesList.pop()
        startingStatesList.append(curStartState) #new state becomes start state
    if et.left.checked == 1:
        newList = []
        newList.append((curStartState + 1))
        Dict[startingStatesList[0]]['e'] += newList
    #print(Dict)


def concatEpsilonToMultipleStartStates(copyOfTree,FirstStateAdded,poppedList):
    #global expression_Tree_copy2
    #Epsilon transition to the NEW start state from the previous FINAL states
    copyOfTree.checked = 1 #Sets the concat to be CHECKED as completed
    for x in poppedList:
        if Dict[x] == {}:
            nested = {}
            nested['e'] = [FirstStateAdded]
            Dict[x] = nested
            
    #checkNextTreeLevel(expression_Tree_copy2)
    #print(finaleSateList,FirstStateAdded)
    setterForNextLevel()
    
def concatTable(copyOfTree):
    global w
    FirstStateAdded = 0
    newDict = {}
    newList = []
    newList.append(w * 2)
    if copyOfTree.left.checked == 0:
        newDict[copyOfTree.left.value] = newList
        Dict[(w * 2)-1] = newDict 
        FirstStateAdded = w * 2 - 1
        Dict[w * 2] = [] 
        startingStatesList.append(w * 2)
    if copyOfTree.right.checked == 0:
        newDict[copyOfTree.right.value] = newList
        Dict[(w * 2)-1] = newDict 
        FirstStateAdded = (w * 2)-1
        Dict[(w * 2)] = [] 
        poppedList = []
        while (len(finalStateList) != 0):
            poppedList.append(finalStateList.pop())
        finalStateList.append((w * 2))
    concatEpsilonToMultipleStartStates(copyOfTree,FirstStateAdded,poppedList)
    
def kleeneStar(copyOfTree,finalStateList):
    global boolForKleene #QUICK FIX: Adding BOOLEAN so if (copyOfTree.type == 4) and (boolForKleene == 0): doesnt run TWICE
    global officialStartState
    officialStartState = 0
    Dict[len(Dict)] = []
    boolForKleene = 1
    finalStateList.append(len(Dict)-1)
    officialStartState = len(Dict) - 1
    newDict = {}
    newDict['e'] = officialStartState
    Dict[finalStateList[0]] = newDict
    newDict2 = {}
    newDict2['e'] = startingStatesList[0]
    Dict[officialStartState] = newDict2
    copyOfTree.checked = 1
    #print(officialStartState) Start
    #print(finalStateList) Final State
    
def setterForNextLevel():
    global expression_Tree_copy
    copyOfTree = expression_Tree_copy
    if copyOfTree.left.left != None:
        checkNextTreeLevel(copyOfTree)
    
def nextNodeUp(copyOfTree,type):
    if copyOfTree.left.checked == 1:
        if copyOfTree.right.type == 1:
            unionTable(copyOfTree)
            unionAlreadyCheckedHelper(copyOfTree) #Comes after unionTable or start State will be changed

def checkNextTreeLevel(copyOfTree):
    global boolForKleene 
    global w
    boolForKleene = 0
    if w == 2:
        if copyOfTree.type == 2:
            foundEndOfTree(copyOfTree,copyOfTree.type)
        if copyOfTree.type == 3:
            foundEndOfTree(copyOfTree,copyOfTree.type)
        if (copyOfTree.type == 4) and (boolForKleene == 0):
            foundEndOfTree(copyOfTree, copyOfTree.type)
    if copyOfTree.left.checked == 0:
        checkNextTreeLevel(copyOfTree.left)
    if copyOfTree.left.checked == 1: #Check if the CHILD was completed 
        if copyOfTree.type == 2:
            concatTable(copyOfTree)
        if (copyOfTree.type == 4) and (boolForKleene == 0):
            kleeneStar(copyOfTree,finalStateList)
        if copyOfTree.type == 3:
            nextNodeUp(copyOfTree,copyOfTree.type)

def unionAlreadyCheckedHelper(et):
    global curStartState
    if et.right.checked == 0: #Check if dealing wiht a unchecked right side
        if et.right.type == 1: #Check if dealing with one symbol in right subtree
            nestedDict = {}
            newList =  []
            newList.append(w*2)
            nestedDict[et.right.value] = newList
            Dict[w+2] = nestedDict
            et.checked = 1
            Dict[len(Dict)] = []
            curStartState = len(Dict)
            #addEpsilon(w*2)

def concatNoChildrenHelperEpsilon(copyOfTree,StartState): #Adding Epsilon for a tree with 1 parent node(CONCAT) and 2 children(SYMBOLS)
    newList = []
    nestedDict = {}
    newList.append(StartState+2)
    nestedDict['e'] = newList
    Dict[StartState+1] = nestedDict
    copyOfTree.checked = 1
    

def helperForConcatNoChildren(copyOfTree): #If in a concat tree with children as symbols
    global w
    StartState = 0
    newDict = {}
    newDict2 = {}
    newList = []
    newList2 = []
    poppedList = []
    newList.append(StartState+1)
    if copyOfTree.left.checked == 0:
        newDict[copyOfTree.left.value] = newList
        Dict[StartState] = newDict 
        FirstStateAdded = StartState - 1
        startingStatesList.append(StartState)
        startingStatesList.append(StartState+2)
    if copyOfTree.right.checked == 0:
        newList2.append(StartState+3)
        newDict2[copyOfTree.right.value] = newList2
        Dict[StartState+2] = newDict2
        while (len(finalStateList) != 0):
            poppedList.append(finalStateList.pop())
        finalStateList.append(StartState+3)
        startingStatesList.pop(StartState+1)
    concatNoChildrenHelperEpsilon(copyOfTree,StartState)
    
def kleeneStarSingleHeleper(et):
    startState = 0
    finalStateList.append(startState+1)
    if et.right == None:
        #Put in a state for the single symbol
        startingStatesList.append(startState)
        nestedDict = {}
        newList = []
        newList.append(startingStatesList[0] + 1)
        nestedDict[et.left.value] = newList
        Dict[startState] = nestedDict
        #Add New State for epsilon transition
        nestedDict2 = {}
        nestedDict2['e'] = startState
        Dict[startState+2] = nestedDict2
        #Add Epsilon from State old final State to new Start State
        startState = startState + 2
        nestedDict3 = {}
        nestedDict3['e'] = startState
        Dict[startState-1] = nestedDict3
        finalStateList.append(startState+2) #Update Final State 
        startingStatesList.pop(0) #Pop old starting State to the list
        startingStatesList.append(startState) #Add new starting state to the list
    # if et.left.type == 1 and et.right != None:
    #     print("test")
    
def foundEndOfTree(et, Parentstype):
    if (Parentstype == 2):
        if (et.left.type == 1 and et.right.type == 1):   
            helperForConcatNoChildren(et)
        else:
            print("concat")
            concatTable(et)
    if (Parentstype == 3): # type 3 = '+'
        #print("-------------")
        #print (et.left.value, et.right.value)
        if et.left.checked == 1:
            unionAlreadyCheckedHelper(et)
        if et.checked == 0:
            UnionEndOfTreeHelper(et)
            unionTable(et)
            setterForNextLevel()
    if (Parentstype == 4):
        if (et.right == None):
            kleeneStarSingleHeleper(et)
        else:
            kleeneStar(et,finalStateList)  

def checkLeft(etLeft):
    exists = 0
    if etLeft.left == None:
        exists = 0
    if etLeft.left:
        exists = 1
    return exists

def expressionTreeOrder(et):
    #print("first node:")
    #print(et.value, et.type)
    if checkLeft(et) == 1:
        #print("Something in left:")
        #print(et.left.value, et.left.type)
        if checkLeft(et.left) == 0: #Check if nothing is in the left of the left (check if end of tree)
            Parentstype = et.type
            #print("parent's type is: ", Parentstype)
            #print(et.right.value, et.right.type)
            foundEndOfTree(et, Parentstype)
        recusriveExpressionTreeOrder(et.left)
    #if not et.left:
        #print("empty")
        
def recusriveExpressionTreeOrder(et):
    if checkLeft(et) == 1:
        #print("Something in left:")
        #print(et.left.value, et.left.type)
        #if checkLeft(et.left) == 0:
            #print(et.right.value, et.right.type)
       #expressionTreeOrder(et.left)
       expressionTreeOrder(et)
    # if not et.left:
    #     print("empty")   
        

def print_tree(et):
    if et.type == Type.SYMBOL:
        # evaluate symbol: it is going to create a nfa for the symbol. ex. if symbol is a, then it will create a nfa for a. 
        regexListInOrder.append(et.value)
    elif et.type == Type.CONCAT:
        print_tree(et.left)
        regexListInOrder.append(".")
        print_tree(et.right)
    elif et.type == Type.UNION:
        print_tree(et.left)
        regexListInOrder.append("+")
        print_tree(et.right)
    elif et.type == Type.STAR:
        print_tree(et.left)
        regexListInOrder.append("*")
    

def create_tree(regex_string):
    stack = []
    for char in regex_string:
        if char.isalnum():
            stack.append(Exp_Tree(Type.SYMBOL, char))
        else:
            if char == "+":
                node = Exp_Tree(Type.UNION)
                node.right = stack.pop()
                node.left = stack.pop()
            elif char == ".":
                node = Exp_Tree(Type.CONCAT)
                node.right = stack.pop()
                node.left = stack.pop()
            elif char == "*":
                node = Exp_Tree(Type.STAR)
                node.left = stack.pop()
            stack.append(node)
    return stack[0]

# The regular-expression operator star has the highest precedence and is left associative.
# The regular-expression operator concatenation has the next highest precedence and is left associative.
# The regular-expression operator + has the lowest precedence and is left associative.
def Precedence(a, b):
    p = ["+", ".", "*"]
    return p.index(a) > p.index(b)

def postfix(regex_list):
    stack = []
    string = ""

    for char in regex_list:
        if char.isalpha():
            string = string + char
            continue

        if char == ")":
            while len(stack) != 0 and stack[-1] != "(":
                string = string + stack.pop()
            stack.pop()
        elif char == "(":
            stack.append(char)
        elif char == "*":
            string = string + char
        elif len(stack) == 0 or stack[-1] == "(" or Precedence(char, stack[-1]):
            stack.append(char)
        else:
            while len(stack) != 0 and stack[-1] != "(" and not Precedence(char, stack[-1]):
                string = string + stack.pop()
            stack.append(char)

    while len(stack) != 0:
        string = string + stack.pop()
    return string

# return the string regex as a list (parse the regex into a list) 
# and add a dot "." between consecutive symbols for concatenation
def prepare_regex(regex_string):
    temp = []
    for i in range(len(regex_string)):
        if i != 0\
            and (regex_string[i-1].isalnum() or regex_string[i-1] == ")" or regex_string[i-1] == "*")\
            and (regex_string[i].isalnum() or regex_string[i] == "("):
            temp.append(".")
        temp.append(regex_string[i])
    regex_string = temp
    return postfix(regex_string)

def readTree(et):
    return 0

class genfa:
    def __init__(self,s):
        self.newlist = list(s)
        self.lastParen = 0


    def createTransitionTable(self,w,h,symbols):
        global Dict
        Dict = {}
        for x in range(h):
            Dict[x] = {}
        for b in range(h):
           # for i in range(len(symbols)+1): #adds a colums in each row. One for each symbols and one for epsilon
            Dict[b] = {}

    
    def lastParenIndexFinder(self):
        for x in range(len(self.newlist)):
            for j in range(len(self.newlist)):
                if (self.newlist[x] == ')'):
                    if(self.newlist[j] != ')'):
                        self.lastParen = x #found index of the last parentheses 
        return self.lastParen
                
    def expressionTree(self):
        self.lastParen
        
    def findSymbols(self):
        NumSymbols = 0
        global symbols
        symbols = []
        for x in range(len(self.newlist)):
            if str(self.newlist[x]).isalnum():
                symbols.append(self.newlist[x])
                NumSymbols += 1
        numStates = NumSymbols * 2 #2 States 
        global w,h
        w, h = NumSymbols, numStates
        self.createTransitionTable(w,h,symbols)
    
    # def grabNextSymbol(regex,i):
    
    
    def parse(self,regex):
        for i in range(len(regex)):
            if str(regex[i]).isalpha():
                if str(regex[i+1]).isalpha():
                    return 0



def main2():
    global currentState
    global startingStatesList
    global regexListInOrder
    global finalStateList
    global expression_Tree_copy
    global expression_Tree_copy2
    regexListInOrder = []
    currentState = 0
    startingStatesList = []
    finalStateList = []
    #((a+b)c)*
    input = "ab" 
    s = input
    newobject = genfa(s)
    newobject.findSymbols()
    #print(newobject.lastParenIndexFinder())
    regex = prepare_regex(input) # return a postfix string
    #print(regex)
    expression_Tree = create_tree(regex)
    print_tree(expression_Tree)
    newobject.parse(regex)
    #print(regexListInOrder)
    readTree(expression_Tree)
    #print("-------------")
    expression_Tree_copy = expression_Tree
    expression_Tree_copy2 = expression_Tree
    expressionTreeOrder(expression_Tree)
    print("input is: ", input)
    print(Dict)
    return 0

main2()



