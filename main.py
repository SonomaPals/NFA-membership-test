# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function
import outside.inside.membership as member


def testing(nfa, list):
    for i in range(len(list)):
        print(list[i], member.check(nfa, list[i]))


def main():
    input_string = "a+b"
    chars = []
    for char in input_string:
        if char.isalnum():
            chars.append(char)

    transition_table = {
        "q0": {"a": [], "b": ['q1'], "e": ['q2']},
        "q1": {"a": [], "b": ['q0'], "e": []},
        "q2": {"a": ['q3'], "b": ['q4'], "e": []},
        "q3": {"a": ['q2'], "b": [], "e": []},
        "q4": {"a": ['q2'], "b": [], "e": []},
    }


    M2 = eFreeNFA.NFA(2, chars, transition_table, "q0", ["q2"]).remove_epsilons()

    for item in M2.transition_table:
        print(item, M2.transition_table[item])


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