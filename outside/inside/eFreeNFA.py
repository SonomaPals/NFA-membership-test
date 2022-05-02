
class eFreeNFA():
    def __init__(self, num_states, num_symbols, transition_table):
        self.num_states = num_states
        self.num_symbols = num_symbols
        self.transition_table = transition_table

    def print(self):
        for item in self.transition_table:
            print(item)

    def remove_epsilons(self):
        epsilon_closures = [] # Create a new list of epsilon closures
        for state in self.transition_table:
            epsilon_closures.append(state[-1]) # The last input symbol in each state row is the epsilon closure

        for i in range(len(epsilon_closures)):
            if i not in epsilon_closures[i]:
                epsilon_closures[i].append(i)

        empty_table = []
        for i in range(self.num_states):
            empty_table.append([])
            for j in range(self.num_symbols):
                empty_table[i].append([])

        newNFA = eFreeNFA(self.num_states, self.num_symbols - 1, empty_table) # Create a new NFA with empty transition table # *** removed - 1 from symbols***
        for k in range(self.num_states): # For every state in the NFA
            for i in epsilon_closures[k]: # For every state in the epsilon closure of the current state
                for j in range(self.num_symbols): # For each of the symbols allowed
                    for item in self.transition_table[i][j]: # For each item in the epsilon closure of this state on this input symbol
                        if item not in newNFA.transition_table[k][j]:
                            newNFA.transition_table[k][j].append(item) # Get only unique items, add to list
        return newNFA

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

    def get_closure(self, state, col):
        return self.transition_table[state][col]


  