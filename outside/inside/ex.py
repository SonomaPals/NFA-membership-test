import itertools
from queue import Queue

#--------------------------
#--------Problem 1---------
#--------------------------

# The reason a class is used is so that we can access the variable in other functions
class DfaClass:
    def __init__(self):
        # Two lists will be created
        # One list to hold all possible strings in the buffer
        # One list to hold the number of each state
        possibleStringList = []
        dictionaryCounter = {}
        counterList = []
        # Append state 0 to the list of state numbers
        counterList.append(0)
        counterForDict = 0
        # Append state 0 which is an empty string to the list of possible states in the buffer
        possibleStringList.append("")
        # Cartesian product of abcd and to get all possible states in the buffer of length 5
        for i in range(1, 6):
            for str in itertools.product("abcd", repeat=i):
                someString = ""
                someString = someString.join(str)
                possibleStringList.append(someString)
                counterForDict = counterForDict + 1
                counterList.append(counterForDict)
        # Create the dictionary for state numbers and states               
        for aString in possibleStringList: 
            key = possibleStringList.index(aString)
            dictionaryCounter[key] = aString
        # Create the variables like prev and next that will be used in other functions
        self.possibleStringList = possibleStringList
        next = [0] * len(self.possibleStringList)
        self.prev = [1] * len(self.possibleStringList)
        self.next = next
        self.dictionaryCounter = dictionaryCounter

    # Uses base4 encoding to the the state number on transition
    def grabStateNum(self,inputString):
        stateNum = 0
        CharactersOfTheString = []
        # We know an empty string will have an Answer of 0
        if (inputString == ""):
            return 0
        # Copy each character fromt he inputted string to a list
        for x in inputString:
            CharactersOfTheString.append(x)
        # Base4 encoding
        for index in range(0, len(CharactersOfTheString)):
            # Search for an 'a' in the string
            if CharactersOfTheString[index] == 'a':
                stateNum = stateNum + 1 * pow(4, (len(CharactersOfTheString) - 1) - index)
            # Search for an 'b' in the string
            elif CharactersOfTheString[index] == 'b':
                stateNum = stateNum + 2 * pow(4, (len(CharactersOfTheString) - 1) - index)
            # Search for an 'c' in the string
            elif CharactersOfTheString[index] == 'c':
                stateNum = stateNum + 3 * pow(4, (len(CharactersOfTheString) - 1) - index)
            # Search for an 'd' in the string
            elif CharactersOfTheString[index] == 'd':
                stateNum = stateNum + 4 * pow(4, (len(CharactersOfTheString) - 1) - index)
            #If NONE of these work then the string does not contain a,b,c, or d and we should exit
            else:
                print("NO a,b,c, or d detected. Exiting. Goodbye")
                exit(9)
        return stateNum

    # Function to check if the string being transitioned to is in the DFA
    def isValid(self,string):
        # If the length of the string is less than 6 return true
        if len(string) < 6:
            return True
        # Initiliaze 4 variables to be False for a string appended with a,b,c, and d
        founda = False
        foundb = False
        foundc = False
        foundd = False
        #Check the string to see if it contains a,b,c, and d. 
        for char in string:
            if char == 'a':
                founda = True
            if char == 'b':
                foundb = True
            if char == 'c':
                foundc = True
            if char == 'd':
                foundd = True
        #Must have found all 4 a,b,c, and d to return True
        if (founda and foundb and foundc and foundd):
            return True
        else:
            return False
     
    # Function to append a, b, c, and d to the given string
    # Then finds the transiton to the next state on the char 
    # Only if it is a valid string being less than length 6
    # or containing a, b, c, and d   
    def transBigQual(self, stateNum, string):
        stateCounter = 0
        string1 = "".join((string,"a"))
        string2 = "".join((string,"b"))
        string3 = "".join((string,"c"))
        string4 = "".join((string,"d"))
        if(self.isValid(string1)):
            if(5 < len(string1)):
                string1 = string1[1:]
            stateCounter += self.prev[self.grabStateNum(string1)]
        if(self.isValid(string2)):
            if(5 < len(string2)):
                string2 = string2[1:]
            stateCounter += self.prev[self.grabStateNum(string2)]
        if(self.isValid(string3)):
            if(5 < len(string3)):
                string3 = string3[1:]
            stateCounter += self.prev[self.grabStateNum(string3)]
        if(self.isValid(string4)):
            if(5 < len(string4)):
                string4 = string4[1:]
            stateCounter += self.prev[self.grabStateNum(string4)]
        self.next[stateNum] = stateCounter

# Function to calculate the Delta of each state in the dictionary 
# on each of the four characters a,b,c, and d
# Then computes the number of strings w of length n over with the given
# proprties. After computer it returns this as the answer
def count(self,n):
    for c in range(n):
        for j, k in self.dictionaryCounter.items(): 
            self.transBigQual(j, k)
        self.prev = self.next
        self.next = [0] * len(self.possibleStringList)
    return self.prev[0]

##############################################################################################################


# Builds out UI and runs the specified option
def main():
    print("Select from the following options by selecting the option number:")
    print()
    print("1: Compute the number of strings 'w' of length n over {a,b,c,d}\n")
    print("0: Terminate the program\n")

    user_input = int(input("Enter Selection: "))

    while user_input != 0:
        if user_input == 1:
            newObject = DfaClass() 
            n = int(input("Enter length n: "))  
            print()
            print("n =", n, "   Answer:",  count(newObject,n))  
            print()    
    return 0

main()