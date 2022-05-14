
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
        newNFA = NFA(self.num_states, self.symbols, self.transition_table, 0, self.final_states) # Create a new NFA with empty transition table # *** removed - 1 from symbols***
        for state in self.states: # For every state in the NFA
            for reach in self.transition_table[state]["e"]: # For every reachable state in that state's epsilon closure
                if reach in self.final_states and state not in newNFA.final_states:
                    newNFA.final_states.append(reach)
                for symbol in self.symbols:
                    for item in self.transition_table[reach][symbol]:
                        if item not in newNFA.transition_table[state][symbol]:
                            newNFA.transition_table[state][symbol].append(item)
            
            del newNFA.transition_table[state]["e"]
        return newNFA
