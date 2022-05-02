# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function
import outside.inside.genfa as eNFA


def main():
    # Example from: https://www.geeksforgeeks.org/conversion-of-epsilon-nfa-to-nfa/
    transition_table = [[[], [1], [2]],[[], [0], []],[[3], [4], []],[[2], [], []],[[2], [], []]]
    num_states = len(transition_table)
    num_symbols = len(transition_table[0]) - 1 # Don't count the epsilon column

    goal = [[[3], [1,4]],[[], [0]],[   [3], [4]],[[2], []],[[2], []]]
    newNFA = eFreeNFA.eFreeNFA(num_states, num_symbols, transition_table).remove_epsilons() # One extra symbol for epsilon

    for item in newNFA.transition_table:
        for thing in item:
            thing.sort()
    
    print(newNFA.transition_table == goal)

main()


# TESTING STRING MEMBERSHIP ~~ IDEAS

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
         
