# Program to convert epsilon-NFA to epsilon-free NFA

def print_lists(all_lists):
    for item in all_lists:
        print(item)

class NFA():
    def __init__(self, num_states, num_symbols, transition_table):
        self.num_states = num_states
        self.num_symbols = num_symbols
        self.transition_table = transition_table

    def print(self):
        print_lists(self.transition_table)

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


        # transition_table = [[[4], [1], [0]], [[], [2], [1,3]], [[], [3], [2]], [[], [], [3]], [[5], [], [1, 2, 4]], [[3], [], [5]]] # 5 states, 2 input symbols + E

        newNFA = NFA(self.num_states, self.num_symbols - 1, empty_table) # Create a new NFA with empty transition table # *** removed - 1 from symbols***
        for k in range(self.num_states): # For every state in the NFA
            for i in epsilon_closures[k]: # For every state in the epsilon closure of the current state
                for j in range(self.num_symbols): # For each of the symbols allowed
                    for item in self.transition_table[i][j]: # For each item in the epsilon closure of this state on this input symbol
                        if item not in newNFA.transition_table[k][j]:
                            newNFA.transition_table[k][j].append(item) # Get only unique items, add to list
        return newNFA


def get_closure(state, col, nfa):
    return nfa.transition_table[state][col]


    # # input_string = input("Enter a string to test: ")
    # input_string = "ababa"
    # # input_chars = input_string.split(" ") # Get each character individually
    # input_chars = []
    # for char in input_string:
    #     if char not in input_chars:
    #         input_chars.append(char)
    # current = [0] * 4 # What is reachable from the current state?
    # next = [0] * 4
    # curr_state = 0 # Start at starting state
    # char_index = 0

    # for i in range(len(input_string)):
    #     curr_char = input_string[i] # Get the current character in the input string
    #     for j in range(len(input_chars)): # Find the corresponding number ID of that input character
    #         if input_chars[j] == curr_char:
    #             char_index = j
    #             break
    #     clo = get_closure(curr_state, char_index, eFreeNFA) # Symbol number NOT index in string
    #     print(clo)
    #     curr_state += 1 # THIS SHOULDN'T JUST BE INCREMENTING FOREVER --> Gets higher than # of states!
         
