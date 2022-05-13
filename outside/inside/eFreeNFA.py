
class NFA():
    def __init__(self, num_states, symbols, transition_table, start, end):
        self.num_states = num_states
        self.num_symbols = len(symbols)
        self.symbols = symbols
        self.transition_table = transition_table
        self.start_state = start
        self.final_states = end

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
                

        newNFA = NFA(self.num_states, self.symbols, empty_table, 0, self.final_states) # Create a new NFA with empty transition table # *** removed - 1 from symbols***
        for k in range(self.num_states): # For every state in the NFA
            for i in epsilon_closures[k]: # For every state in the epsilon closure of the current state
                for j in range(self.num_symbols): # For each of the symbols allowed
                    for item in self.transition_table[i][j]: # For each item in the epsilon closure of this state on this input symbol
                        if item not in newNFA.transition_table[k][j]:
                            newNFA.transition_table[k][j].append(item) # Get only unique items, add to list


        for i in range(len(self.final_states)): # for every final state
            for j in range(len(epsilon_closures)): # for every epsilon closure (one for each state)
                if self.final_states[i] in epsilon_closures[j]: # if the epsilon closure contains a final state
                    newNFA.final_states.append(j)
  
        newNFA.final_states = set(newNFA.final_states)

        return newNFA

    def get_closure(self, state, col):
        return self.transition_table[state][col]


  