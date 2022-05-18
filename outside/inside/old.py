# epsilonNFA file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

# Algorithms that we are implementing
#---------------------
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
#---------------------
import sys #Used to take in input as a file arg
        
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
    #et.right.checked = 1
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
    #finalStateList.append(len(Dict))
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
    
class TreeThatExpressesItself:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.left = None
        self.right = None
        self.checked = 0
        
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
        Dict[w * 2] = {}
        startingStatesList.append(w * 2)
    if copyOfTree.right.checked == 0:
        newDict[copyOfTree.right.value] = newList
        Dict[(w * 2)-1] = newDict 
        FirstStateAdded = (w * 2)-1
        Dict[(w * 2)] = {} 
        poppedList = []
        while (len(finalStateList) != 0):
            poppedList.append(finalStateList.pop())
        finalStateList.append((w * 2))
    concatEpsilonToMultipleStartStates(copyOfTree,FirstStateAdded,poppedList)
    
def kleeneStarForSingleStar(copyOfTree,finalStateList,startStateList):
    global boolForKleene
    #Add 1 new states
    #1 New Start state. Sends EPSILON to the current startStateList
    #After Final
    #Pop the previous value of the startStateList
    # appened the state to theStartSateList
    boolForKleene = 1
    newStartState = {}
    newStartState['e'] = []
    Dict[len(Dict)] = newStartState #Create new start state, put at end
    for x in startStateList:
        newStartState['e'] += [x]
    for x in startStateList:
        startStateList.pop()
    startStateList.append(len(Dict)-1)
    newList = []
    for x in finalStateList:
        for y in startStateList:
            newList.append(y)
            Dict[x]['e'] = newList
    
def kleeneStar(copyOfTree,finalStateList):
    # Look into DYNAMICALLY CREATING LISTS python
    global boolForKleene #QUICK FIX: Adding BOOLEAN so if (copyOfTree.type == 4) and (boolForKleene == 0): doesnt run TWICE
    global officialStartState
    if (regexListInOrder[len(regexListInOrder)-1] == '*') and (copyOfTree.left != None) and (copyOfTree.left.type == 3): #(a+b+c)*
        officialStartState = 0
        Dict[len(Dict)] = []
        boolForKleene = 1
        finalStateList.append(len(Dict)-2)
        officialStartState = len(Dict) - 1
        newDict = {}
        newDict['e'] = list(officialStartState)
        Dict[finalStateList[0]] = newDict
        newDict2 = {}
        newDict2['e'] = list(startingStatesList[0])
        Dict[officialStartState] = newDict2
        copyOfTree.checked = 1
        oldFinal1 = finalStateList.pop() 
        oldFinal2 = finalStateList.pop()
        newDict3 = {}
        newDict4 = {}
        finalStateList.pop()
        finalStateList.append(len(Dict)-1)
        newDict3['e'] = list(finalStateList[0])
        newDict4['e'] = list(finalStateList[0])
        Dict[oldFinal1] = newDict3
        Dict[oldFinal2] = newDict4
    else:    #Plus sign never onto of concat or star #((a+b)c)*
        officialStartState = 0
        Dict[len(Dict)] = []
        boolForKleene = 1
        finalStateList.append(len(Dict)-1)
        officialStartState = len(Dict) - 1
        newDict = {}
        newDict['e'] = list(officialStartState)
        Dict[finalStateList[0]] = newDict
        newDict2 = {}
        newDict2['e'] = list(startingStatesList[0])
        Dict[officialStartState] = newDict2
        copyOfTree.checked = 1
    #print(officialStartState) Start
    #print(finalStateList) Final State
    
def setterForNextLevel(): #Creates a fresh copy of a tree
    global expression_Tree_copy
    copyOfTree = expression_Tree_copy
    if copyOfTree.left.left != None:
        checkNextTreeLevel(copyOfTree)

def unionOfRightTreeHelper(newInitial): #For something in the form: (a+b)+(c+d)
    Dict[newInitial+1] = {}
    newDict = {}
    newList = []
    for x in startingStatesList:
        newList.append(x)
    newDict['e'] = newList
    Dict[newInitial+1] = newDict

def unionOfRightTree(copyOfTree): #coming from a parent tree with left checked (nextNodeUp)| For something in the form: (a+b)+(c+d)
    if copyOfTree.left.type == 1 and copyOfTree.right.type == 1: #We are in a right subtree with children as 2 symbols
        newStartingState = int(startingStatesList[0])+1 #new start start will be 1 after the last one
        Dict[newStartingState][copyOfTree.left.value] = startingStatesList[0]+2 #Create a
        poppedLeftInitial = startingStatesList.pop()
        startingStatesList.append(newStartingState)
        Dict[newStartingState+2][copyOfTree.right.value] = newStartingState + 3 #Create b
        startingStatesList.append(newStartingState+2)
        finalStateList.append(newStartingState+1)
        finalStateList.append(newStartingState+3)
        newDict = {}
        newList = []
        for x in startingStatesList:
            newList.append(x)
        newDict['e'] = newList
        Dict[newStartingState+3] = newDict
        #Now reset starting states
        while len(startingStatesList) != 0:
            startingStatesList.pop()
        startingStatesList.append(poppedLeftInitial)
        startingStatesList.append(newStartingState+3)
        newInitial = newStartingState+3
        unionOfRightTreeHelper(newInitial)
 
def nextNodeUp(copyOfTree,type):
    if copyOfTree.left.checked == 1:
        if copyOfTree.right.type == 1:
            unionTable(copyOfTree)
            unionAlreadyCheckedHelper(copyOfTree) #Comes after unionTable or start State will be changed
        if copyOfTree.right.type == 2:
            print("nextNodeUp: CONCAT")
        if copyOfTree.right.type == 3:
            #print("nextNodeUp: UNION")
            unionOfRightTree(copyOfTree.right)
        #4 Star?
          
def checkNextTreeLevel(copyOfTree):
    global boolForKleene 
    global w
    boolForKleene = 0
    #Checks next tree here
    if w == 2:
        if copyOfTree.type == 2:
            foundEndOfTree(copyOfTree,copyOfTree.type)
        if copyOfTree.type == 3:
            foundEndOfTree(copyOfTree,copyOfTree.type)
        if (copyOfTree.type == 4) and (boolForKleene == 0):
            kleeneStarForSingleStar(copyOfTree, finalStateList,startingStatesList)
    if copyOfTree.type == 1:
        pass
    else:
        if copyOfTree.left.checked == 0:
            checkNextTreeLevel(copyOfTree.left)
        if copyOfTree.left.checked == 1: #Check if the CHILD was completed 
            if copyOfTree.type == 2:
                concatTable(copyOfTree)
            if (copyOfTree.type == 4) and (boolForKleene == 0):
                kleeneStarForSingleStar(copyOfTree, finalStateList,startingStatesList)
                #kleeneStar(copyOfTree,finalStateList)
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
            Dict[len(Dict)] = {}
            curStartState = len(Dict)
            finalStateList.append(w*2)
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

class Classifiers:
    LETTER = 1
    PERIOD = 2
    PLUSSIGN  = 3
    STAR = 4
 
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
        temp = startState
        int(temp)
        nestedDict2['e'] = [temp]
        Dict[startState+2] = nestedDict2
        #Add Epsilon from State old final State to new Start State
        startState += 2
        nestedDict3 = {}
        temp2 = startState
        int(temp2)
        nestedDict3['e'] = [temp2]
        Dict[startState-1] = nestedDict3
        finalStateList.append(startState+2) #Update Final State 
        startingStatesList.pop(0) #Pop old starting State to the list
        startingStatesList.append(startState) #Add new starting state to the list
    # if et.left.type == 1 and et.right != None:
    #     print("test")
    
def checkIfParentHasSameType(expression_Tree_copy2):
    x= None
    while (expression_Tree_copy2.left.left != x):
        if expression_Tree_copy2.left.type == 4:
            return 1
        
def foundEndOfTree(et, Parentstype):
    if (Parentstype == 2):
        if (et.left.type == 1 and et.right.type == 1):  #ab (Single tree, just CONCAT )#Symbols on left and right. No Children beyond single tree 3 nodes.
            helperForConcatNoChildren(et)
        else:
            concatTable(et)
    if (Parentstype == 3): # type 3 = '+' 
        if et.left.checked == 1:
            unionAlreadyCheckedHelper(et)
        if et.checked == 0 and et.left.type == 1 and et.right.type == 1: # a + b (Single tree, just UNION)
            UnionEndOfTreeHelper(et)
            unionTable(et)
            setterForNextLevel()
    if (Parentstype == 4):
        if (et.right == None):
            kleeneStarSingleHeleper(et) # a*
            if (checkIfParentHasSameType(expression_Tree_copy2) == 1):
                setterForNextLevel()
        else:
            kleeneStar(et,finalStateList)  #((a+b)c)* 

def checkLeft(etLeft):
    exists = 0
    if etLeft.left == None:
        exists = 0
    if etLeft.left:
        exists = 1
    return exists

def expressionTreeOrder(et):
    if checkLeft(et) == 1:
        if checkLeft(et.left) == 0: #Check if nothing is in the left of the left (check if end of tree)
            Parentstype = et.type
            foundEndOfTree(et, Parentstype)
        recusriveExpressionTreeOrder(et.left)
        
def recusriveExpressionTreeOrder(et):
    if checkLeft(et) == 1:
       expressionTreeOrder(et)

def creationOfExpressionTree(regex_string):
    stack = []
    for char in regex_string:
        if char.isalnum():
            stack.append(TreeThatExpressesItself(Classifiers.LETTER, char))
        else:
            if char == "+":
                node = TreeThatExpressesItself(Classifiers.PLUSSIGN)
                node.right = stack.pop()
                node.left = stack.pop()
            elif char == ".":
                node = TreeThatExpressesItself(Classifiers.PERIOD)
                node.right = stack.pop()
                node.left = stack.pop()
            elif char == "*":
                node = TreeThatExpressesItself(Classifiers.STAR)
                node.left = stack.pop()
            stack.append(node)
    return stack[0]

# The regular-expression operator star has the highest precedence and is left associative.
# The regular-expression operator concatenation has the next highest precedence and is left associative.
# The regular-expression operator + has the lowest precedence and is left associative.
def orderOfEval(a, b):
    order = ["+", ".", "*"]
    return order.index(a) > order.index(b)

# def orderEvalUsingPostFix(regex_list):
#     container = []
#     words = ""
#     for char in regex_list:
#         if char.isalnum():
#             words += char
#             continue
#         if char == ")":
#             while len(container) != 0 and container[-1] != "(":
#                 words = words + container.pop()
#             container.pop()
#         elif char == "(":
#             container.append(char)
#         elif char == "*":
#             words = words + char
#         elif len(container) == 0 or container[-1] == "(" or orderOfEval(char, container[-1]):
#             container.append(char)
#         else:
#             while len(container) != 0 and container[-1] != "(" and not orderOfEval(char, container[-1]):
#                 words = words + container.pop()
#             container.append(char)

#     while len(container) != 0:
#         words = words + container.pop()
#     return words

def orderEvalUsingPostFix(regex_list):
    container = []
    words = ""
    for char in regex_list:
        if char.isalnum():
            words += char
            continue
        if char == ")":
            while len(container) != 0 and container[-1] != "(":
                words += container.pop()
            container.pop()
        elif char == "(":
            container.append(char)
        elif char == "*":
            words = words + char
        elif len(container) == 0 or container[-1] == "(" or orderOfEval(char, container[-1]):
            container.append(char)
        else:
            while len(container) != 0 and container[-1] != "(" and not orderOfEval(char, container[-1]):
                words = words + container.pop()
            container.append(char)

    while len(container) != 0:
        words = words + container.pop()
    return words


# return the string regex as a list (parse the regex into a list) 
# and add a dot "." between consecutive symbols for concatenation
def parseRegexIntoList(regex_string):
    temp = []
    for i in range(len(regex_string)):
        if i != 0\
            and (regex_string[i-1].isalnum() or regex_string[i-1] == ")" or regex_string[i-1] == "*")\
            and (regex_string[i].isalnum() or regex_string[i] == "("):
            temp.append(".")
        temp.append(regex_string[i])
    regex_string = temp
    return orderEvalUsingPostFix(regex_string)

def printInfo(Dict): #Function to return info for E-Free NFA portion of the project.
    return (h,symbols,Dict,startingStatesList[0],finalStateList)

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

    def parse(self,regex):
        for i in range(len(regex)):
            if str(regex[i]).isalpha():
                if str(regex[i+1]).isalpha():
                    return 0

def transformTTable(Dict):
    print(Dict)
    symbolsPlusEpsilon = symbols
    symbolsPlusEpsilon.append("e")
    for x in symbolsPlusEpsilon:
        for y in range(len(Dict)):
            r = Dict[y].get(x, None)
            if r == None:
                Dict[y][x] = []
    #print(printInfo(Dict))

def main2(inp):
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
    userInput = inp
    s = userInput
    newobject = genfa(s)
    newobject.findSymbols()
    regex = parseRegexIntoList(userInput) # return a postfix string
    expression_Tree = creationOfExpressionTree(regex)
    newobject.parse(regex)
    expression_Tree_copy = expression_Tree
    expression_Tree_copy2 = expression_Tree
    expressionTreeOrder(expression_Tree)
    print("input is: ", userInput)
    transformTTable(Dict)
    return 0

usrInput = "((a+b)c)*"
#usrInput = sys.argv[1]
main2(usrInput)


