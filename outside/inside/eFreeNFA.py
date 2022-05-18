
class NFA():
    def __init__(self, x):
        self.num_states = x[0] #num_states
        self.num_symbols = len(x[1]) #len(symbols)
        self.symbols = x[1]
        self.transition_table = x[2]
        self.states = self.transition_table.keys()
        self.start_state = x[3]
        self.final_states = x[4]

    def copy(self, original):
        self.num_states = original.num_states
        self.num_symbols = original.num_symbols
        self.symbols = original.symbols
        self.transition_table = original.transition_table
        self.states = original.states
        self.start_state = original.start_state
        self.final_states  = original.final_states

    def without_epsilons(self):
        # newNFA = NFA(self.num_states, self.symbols, self.transition_table, self.start_state, self.final_states) # Create a new NFA with empty transition table # *** removed - 1 from symbols***
        newNFA = self
        if 'e' not in newNFA.symbols:
            return "This NFA does not contain epsilon."
        newNFA.symbols.remove('e') # If it exists, remove epsilon
        for state in self.states: # For every state in the NFA
            for reach in self.transition_table[state]["e"]: # For every reachable state in that state's epsilon closure
                if reach in self.final_states:
                    newNFA.final_states.append(state)
                #             if state in self.final_states and state not in newNFA.final_states: # If that reachable state is a final state
                # newNFA.final_states.append(state) # Add it to the final states
                for symbol in self.symbols:
                    for item in self.transition_table[reach][symbol]:
                        if item not in newNFA.transition_table[state][symbol]:
                            newNFA.transition_table[state][symbol].append(item)
            del newNFA.transition_table[state]["e"]
        
        return newNFA

    def check_string(self, string):
        current = [self.start_state] # Will contain "q0" or something similar
        for char in string:
            next = []
            for state in current:
                for item in self.transition_table[state][char]:
                    next.append(item)   
            if len(next) == 0:
                return False
            current = next
        for item in current:
            if item in self.final_states:
                return True
        return False

    def reachable(self, state): # Determines if this state is reachable from any other state
        for other in self.transition_table: # for each state
            for symbol in self.symbols: # for each symbol
                if state in self.transition_table[other][symbol]: # is the current state in this secondary state + current symbol's closure?
                    return True
        return False

    def outwards(self, state):
        for symbol in self.symbols:
            if self.transition_table[state][symbol] != []:
                return True
        
        return False

    def delete_states(self):
        invalid = []
        for state in self.states:
            if not self.reachable(state) and state != self.start_state:
                invalid.append(state)

        for state in invalid:
            del self.transition_table[state]

        return self

    # def epsilon_to_epsilonFree(self, x): # start with an Epsilon NFA
    #     M1 = NFA(x) # Create an NFA with epsilons
    #     print(self.transition_table)
    #     M2 = self.without_epsilons() # Remove all epsilon transitions from NFA
    #     print(M2.transition_table)
    #     M3 = M2.delete_states()
    #     # delete_states(M2) # Delete
    #     print()
    #     print(M3.transition_table)
