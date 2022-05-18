# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as efNFA # Import Katie's knfa.py file --> uses convert_nfa function
import outside.inside.gold as reNFA

def test1():
    input_string = 'a+b'
    chars = []
    for char in input_string:
        if char.isalnum():
            chars.append(char)

    transition_table_nums = {
        'q0': {'0': [], '1': ['q1'], 'e': ['q2']},   #  list['q0']['1']
        'q1': {'0': [], '1': ['q0'], 'e': []},
        'q2': {'0': ['q3'], '1': ['q4'], 'e': []},
        'q3': {'0': ['q2'], '1': [], 'e': []},
        'q4': {'0': ['q2'], '1': [], 'e': []},
    }

    transition_table_letters = {
        'q0': {'a': [], 'b': ['q1'], 'e': ['q2']},
        'q1': {'a': [], 'b': ['q0'], 'e': []},
        'q2': {'a': ['q3'], 'b': ['q4'], 'e': []},
        'q3': {'a': ['q2'], 'b': [], 'e': []},
        'q4': {'a': ['q2'], 'b': [], 'e': []},
    }

    letters = ['a', 'b']
    nums = ['0', '1']
    M2 = efNFA.NFA([2, nums, transition_table_nums, 'q0', ['q2']]).remove_epsilons()
    M3 = efNFA.NFA([2, letters, transition_table_letters, 'q0', ['q2']]).remove_epsilons()

    test5a = ['10101', '11111', '11101', '10010', '10111', '10110', '01000', '00101', '01011', '00000']
    test5b = ['babab', 'bbbbb', 'bbbab', 'baaba', 'babbb', 'babba', 'abaaa', 'aabab', 'ababb', 'aaaaa']
    test6a = ['101010', '111111', '100100', '110010', '101001', '001010', '010100', '000110', '001111', '000000']
    test6b = ['bababa', 'bbbbbb', 'baabaa', 'bbaaba', 'babaab', 'aababa', 'ababaa', 'aaabba', 'aabbbb', 'aaaaaa']

    for i in range(len(test5a)):
        print(test5a[i], M2.check_string(test5a[i]), "/", M3.check_string(test5b[i]), test5b[i])

    for i in range(len(test6a)):
        print(test6a[i], M2.check_string(test6a[i]), "/", M3.check_string(test6b[i]), test6b[i])

def regex_to_epsilonNFA(userInput):
    # usrInput = "ab" # Get user input
    x = reNFA.nfaInfo(reNFA.regexToNFA(userInput)) # G/J code to go from regex to epsilon-NFA --> returns tuple of NFA definition
    return efNFA.NFA(x) # Return the NFA object corresponding to this userInput

def epsilonNFA_to_epsilonFreeNFA(M1):
    mid = M1.without_epsilons() # Remove epsilon transitions
    mid = mid.delete_states() # Remove any unnecessary states
    return mid

def main():
    usrInput = "((a+b)c)*"
    M1 = regex_to_epsilonNFA(usrInput)
    M2 = epsilonNFA_to_epsilonFreeNFA(M1)

    testA = ["bcacbcacbcacacacacbcbcbcbcacacbc", "acacbcacacacacacacbcbcbc", "acacacbc", "aaaabbbbc", "abc"] # First 3 should pass, last 2 should fail
    for string in testA:
        print(M2.check_string(string))


    # python old.py "ab"
    # python old.py "a+b"
    # python old.py "((a+b)c)*"
    # Should pass
    # bcacbcacbcacacacacbcbcbcbcacacbc
    # acacbcacacacacacacbcbcbc
    # acacacbc
    # Should fail
    # aaaabbbbc
    # abc

    # python old.py "(ab)*"
    # Should pass
    # abababababababababab
    # ababababab
    # ab
    # Should fail
    # aaaaab
    # bba

    
main()
