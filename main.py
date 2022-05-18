# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function
# import outside.inside.genfa as eNFA

# for every character in the input
# current state on this input gives --> _______

def test2(string, nfa):
  start = nfa.start_state
  for char in string:
    reachable = nfa.transition_table[start][char]


def test(string, nfa):
    current = [0]*len(nfa.transition_table) # number of states, each has a zero for now
    starting_state = 0 # this can be initialized to be whatever state it needs to be...
    current[starting_state] = 1 # mark the starting state as visit-able without even reading input
    # input_string = "1100" # BUG: THIS REQUIRES THAT INPUTS BE THE ACTUAL CHARACTERS 0 AND 1 THEMSELVES.... HOPEFULLY CAN TRANSLATE LATER...

    while string != "":
      for i in range(len(current)): # for every state
        if current[i]: # if it's marked with a 1 in the 'current' vector
          reachable = nfa.transition_table[i][int(string[0])] # mark all states in the closure of [state][input symbol] as reachable
          next = [0] * len(nfa.transition_table) # create 'next' vector
          for i in reachable:
            next[i] = 1 # mark those as reachable in the 'next' vector

      string = string[1:]
      current = next

    for i in range(len(current)):
      if current[i] == 1 and i in nfa.final_states:
        return True

    return False


def main():
    # Example from: https://www.geeksforgeeks.org/conversion-of-epsilon-nfa-to-nfa/
    transition_table = [[[], [1], [2]],[[], [0], []],[[3], [4], []],[[2], [], []],[[2], [], []]]
    # goal = [[[3], [1,4]],[[], [0]],[[3], [4]],[[2], []],[[2], []]]

    start_state = 0
    final_states = [2]
    num_states = len(transition_table)
    symbols = ['a', 'b']

    M2 = eFreeNFA.NFA([num_states, symbols, transition_table, start_state, final_states]).remove_epsilons() # One extra symbol for epsilon

    # print(goal)
    # print(M2.transition_table)
    # print(M2.final_states)

    print(test("110", M2))




main()
