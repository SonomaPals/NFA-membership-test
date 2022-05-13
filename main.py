# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function

def get_num(nfa, char):
  for i in range(len(nfa.symbols)):
    if nfa.symbols[i] == char:
      return i

  return False

def check_membership(nfa, string):
    current = [nfa.start_state]

    for idx in range(len(string)): # The string without the first character
      input_char = get_num(nfa, string[idx])
      # print(input_char)
      next = []
      for state in current:
        # whats the closure of that state?
        for item in nfa.transition_table[state][input_char]:
          next.append(item)
      
      if len(next) == 0:
        return False

      current = next

    for item in current:
      if item in nfa.final_states:
        return True
      
    return False


def main():
    # Example 1
    # https://www.geeksforgeeks.org/conversion-of-epsilon-nfa-to-nfa/
    transition_table = [[[], [1], [2]],[[], [0], []],[[3], [4], []],[[2], [], []],[[2], [], []]]
    goal = [[[3], [1,4]],[[], [0]],[[3], [4]],[[2], []],[[2], []]]

    start_state = 0
    final_states = [2]
    num_states = len(transition_table)
    symbols = ['0', '1']

    M2 = eFreeNFA.NFA(num_states, symbols, transition_table, start_state, final_states).remove_epsilons() # One extra symbol for epsilon


    print(M2.symbols)
    print(M2.transition_table)
    print(goal)

    test5 = [
      "10101",
      "11111",
      "11101",
      "10010",
      "10111",
      "10110",
      "01000",
      "00101",
      "01011",
      "00000"
    ]

    test6 = [
      "101010",
      "111111",
      "100100",
      "110010",
      "101001",
      "001010",
      "010100",
      "000110",
      "001111",
      "000000"
    ]

    for string in test5:
      print(string, check(M2, string))
    # print(check(M2, "01000"))

    for string in test6:
      print(string, check(M2, string))





main()


# 101010 incorrectly gives true (should be false)
# 10101 incorrectly fives true (should be false)


