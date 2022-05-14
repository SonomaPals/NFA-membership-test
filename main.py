# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function
import outside.inside.membership as member


def testing(nfa, list):
    for i in range(len(list)):
        print(list[i], member.check(nfa, list[i]))


def main():
    # Example 1
    # https://www.geeksforgeeks.org/conversion-of-epsilon-nfa-to-nfa/
    transition_table = [[[], [1], [2]],[[], [0], []],[[3], [4], []],[[2], [], []],[[2], [], []]]
    # goal = [[[3], [1,4]],[[], [0]],[[3], [4]],[[2], []],[[2], []]]

    start_state = 0
    final_states = [2]
    num_states = len(transition_table)
    # symbols = ['0', '1']
    symbols1 = ['0', '1']
    M2 = eFreeNFA.NFA(num_states, symbols1, transition_table, start_state, final_states).remove_epsilons() # One extra symbol for epsilon
    symbols2 = ['a', 'b']
    M3 = eFreeNFA.NFA(num_states, symbols2, transition_table, start_state, final_states).remove_epsilons() # One extra symbol for epsilon



    # testing(M2, test6a)
    # testing(M3, test6b)


main()



    # test5a = [
    #   "10101",
    #   "11111",
    #   "11101",
    #   "10010",
    #   "10111",
    #   "10110",
    #   "01000",
    #   "00101",
    #   "01011",
    #   "00000"
    # ]

    # test5b = [
    #   "babab",
    #   "bbbbb",
    #   "bbbab",
    #   "baaba",
    #   "babbb",
    #   "babba",
    #   "abaaa",
    #   "aabab",
    #   "ababb",
    #   "aaaaa"
    # ]

    # test6a = [
    #   "101010",
    #   "111111",
    #   "100100",
    #   "110010",
    #   "101001",
    #   "001010",
    #   "010100",
    #   "000110",
    #   "001111",
    #   "000000"
    # ]

    # test6b = [
    #   "bababa",
    #   "bbbbbb",
    #   "baabaa",
    #   "bbaaba",
    #   "babaab",
    #   "aababa",
    #   "ababaa",
    #   "aaabba",
    #   "aabbbb",
    #   "aaaaaa"
    # ]