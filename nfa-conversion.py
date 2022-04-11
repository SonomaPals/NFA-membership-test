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
            state_list = [] # Create a "row" in the table for each state
        for j in range(num_symbols):
            input_list = [] # Create a "cell" in the row for each input state
            state_list.append(input_list) # Add that cell to its row
            
            self.transition_table.append(state_list) # Add that row to the table


def main():
    # num_states = 3;
    # num_symbols = 2;
    myNFA = NFA(3, 2)
    print_lists(myNFA.transition_table)

    


main()