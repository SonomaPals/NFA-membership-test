# Program to convert epsilon-NFA to epsilon-free NFA

def print_lists(all_lists):
    for item in all_lists:
        print(item)

class NFA():
    def __init__(self, num_states, num_symbols):
        self.num_states = num_states
        self.num_symbols = num_symbols

        self.transition_table = []
        for i in range(num_states):
            self.transition_table.append([]) # Add that row to the table
        for i in range(num_states):
            for j in range(num_symbols):
                self.transition_table[i].append([])

    def print(self):
        print_lists(self.transition_table)

def get_closure(state, col, nfa):
    return nfa.transition_table[state][col]

def populate_transitions(myNFA):
 # Transitions from state 0
    myNFA.transition_table[0][0] = [0]           # Input 0
    myNFA.transition_table[0][1] = []            # Input 1
    myNFA.transition_table[0][2] = [0, 1, 2]     # Input 2 (epsilon)

    # Transitions from state 1
    # Inputs: 0 through 2
    myNFA.transition_table[1][0] = []          # Input 0
    myNFA.transition_table[1][1] = [1]         # Input 1
    myNFA.transition_table[1][2] = [1, 2]     # Input 2 (epsilon)

    # # Transitions from state 2
    # # Inputs: 0 through 2
    myNFA.transition_table[2][0] = [0]       # Input 0
    myNFA.transition_table[2][1] = [1]      # Input 1
    myNFA.transition_table[2][2] = [2]          # Input 2 (epsilon)

def create_efree_NFA(myNFA):   
    epsilon_closures = [] # Create a new list of epsilon closures
    for state in myNFA.transition_table:
        epsilon_closures.append(state[-1]) # The last input symbol in each state row is the epsilon closure

    newNFA = NFA(myNFA.num_states, myNFA.num_symbols)


    for k in range(myNFA.num_states):
        for i in epsilon_closures[k]: # For every state in the epsilon closure of state 0
            for j in range(myNFA.num_symbols): # For each of the symbols allowed
                for item in myNFA.transition_table[i][j]: # For each item in the closure of this state on this input symbol
                    if item not in newNFA.transition_table[i][j]:
                        newNFA.transition_table[i][j].append(item) # Get only unique items, add to list

    return newNFA

def main():
    num_states = 3
    num_symbols = 2
    eNFA = NFA(num_states, num_symbols + 1) # The extra (last) column is for epsilons

    populate_transitions(eNFA) # Add all the necessary transitions to the NFA based on the input
    
    eFreeNFA = create_efree_NFA(eNFA)

    eFreeNFA.print()


    # input_string = input("Enter a string to test: ")
    input_string = "ababa"
    # input_chars = input_string.split(" ") # Get each character individually
    input_chars = []
    for char in input_string:
        if char not in input_chars:
            input_chars.append(char)
    current = [0] * 4 # What is reachable from the current state?
    next = [0] * 4
    curr_state = 0 # Start at starting state
    char_index = 0

    for i in range(len(input_string)):
        curr_char = input_string[i] # Get the current character in the input string
        for j in range(len(input_chars)): # Find the corresponding number ID of that input character
            if input_chars[j] == curr_char:
                char_index = j
                break
        clo = get_closure(curr_state, char_index, eFreeNFA) # Symbol number NOT index in string
        print(clo)
        curr_state += 1 # THIS SHOULDN'T JUST BE INCREMENTING FOREVER --> Gets higher than # of states
         


        

main()