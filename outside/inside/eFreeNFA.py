
class NFA():
    def __init__(self, num_states, symbols, transition_table, start, end):
        self.num_states = num_states
        self.num_symbols = len(symbols)
        self.symbols = symbols
        self.transition_table = transition_table
        self.states = transition_table.keys()
        self.start_state = start
        self.final_states = end

    def remove_epsilons(self):
        newNFA = NFA(self.num_states, self.symbols, self.transition_table, self.start_state, self.final_states) # Create a new NFA with empty transition table # *** removed - 1 from symbols***
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
