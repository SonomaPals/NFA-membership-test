# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function

def main():
    input_string = 'a+b'
    chars = []
    for char in input_string:
        if char.isalnum():
            chars.append(char)


    # Create one small unit NFA for each input character

    curr_state = 0
    curr_name = 'q' + str(curr_state)
    print(curr_name)
    # for char in chars:

        # create a single unit NFA
        # make it have two states
        # one starting, one accepting
        # one transition from the start to the accepting, with the label of the character (char)












    # transition_table_nums = {
    #     'q0': {'0': [], '1': ['q1'], 'e': ['q2']},   #  list['q0']['1']
    #     'q1': {'0': [], '1': ['q0'], 'e': []},
    #     'q2': {'0': ['q3'], '1': ['q4'], 'e': []},
    #     'q3': {'0': ['q2'], '1': [], 'e': []},
    #     'q4': {'0': ['q2'], '1': [], 'e': []},
    # }

    # transition_table_letters = {
    #     'q0': {'a': [], 'b': ['q1'], 'e': ['q2']},
    #     'q1': {'a': [], 'b': ['q0'], 'e': []},
    #     'q2': {'a': ['q3'], 'b': ['q4'], 'e': []},
    #     'q3': {'a': ['q2'], 'b': [], 'e': []},
    #     'q4': {'a': ['q2'], 'b': [], 'e': []},
    # }

    



    # # letters = ['a', 'b']
    # # nums = ['0', '1']
    # M2 = eFreeNFA.NFA(2, chars, transition_table_nums, 'q0', ['q2']).remove_epsilons()
    # M3 = eFreeNFA.NFA(2, chars, transition_table_letters, 'q0', ['q2']).remove_epsilons()

    # test5a = ['10101', '11111', '11101', '10010', '10111', '10110', '01000', '00101', '01011', '00000']
    # test5b = ['babab', 'bbbbb', 'bbbab', 'baaba', 'babbb', 'babba', 'abaaa', 'aabab', 'ababb', 'aaaaa']
    # test6a = ['101010', '111111', '100100', '110010', '101001', '001010', '010100', '000110', '001111', '000000']
    # test6b = ['bababa', 'bbbbbb', 'baabaa', 'bbaaba', 'babaab', 'aababa', 'ababaa', 'aaabba', 'aabbbb', 'aaaaaa']

    # for i in range(len(test5a)):
    #     print(test5a[i], M2.check_string(test5a[i]), "/", M3.check_string(test5b[i]), test5b[i])

    # for i in range(len(test6a)):
    #     print(test6a[i], M2.check_string(test6a[i]), "/", M3.check_string(test6b[i]), test6b[i])

    
        

main()

