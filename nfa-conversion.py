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

def get_closure(state, col, nfa):
    return nfa.transition_table[state][col]

def main():
    num_states = 3
    num_symbols = 2
    myNFA = NFA(num_states, num_symbols + 1) # The extra (last) column is for epsilons

    # Transitions from state 0
    # Inputs: 0 through 2
    myNFA.transition_table[0].append([0])           # Input 0
    myNFA.transition_table[0].append([])            # Input 1
    myNFA.transition_table[0].append([0, 1, 2])     # Input 2

    # Transitions from state 1
    # Inputs: 0 through 2
    myNFA.transition_table[1].append([])            # Input 0
    myNFA.transition_table[1].append([1])           # Input 1
    myNFA.transition_table[1].append([1, 2])        # Input 2

    # # Transitions from state 2
    # # Inputs: 0 through 2
    myNFA.transition_table[2].append([0])           # Input 0
    myNFA.transition_table[2].append([1])           # Input 1
    myNFA.transition_table[2].append([2])           # Input 2

    epsilon_closures = []
    for state in myNFA.transition_table:
        epsilon_closures.append(state[-1]) # The last input symbol in each state row is the epsilon list


    # print(get_closure(0, 0, myNFA))

    # # epsilon_closures[0] # the epsilon closure of state 0

    e_free_closures = []


    for state in epsilon_closures[0]: # for every state in the closure of state 0
        # for each input symbol i that's not an epsilon:
            e_free_closures.append([])
            for i in range(num_symbols):
                curr_closure = myNFA.transition_table[state][i] # list of this state's transitions on input a (closure on input i)
                # add all elements of this list to the a-closure of state 0
                for item in curr_closure:
                    e_free_closures[-1].append(item)


    print(e_free_closures)


    




    #     for item in myNFA.transition_table[state][0]:
    #         e_free_closures.append(item)
    #     # 0 and 1 and 2
    #     # get the a moves from 0, 1 and 2 and put them in 0 on a
    #     # get the b moves from 0, 1 and 2 and put them in 0 on b

    # print(e_free_closures)



main()