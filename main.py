# # Main file for CS 454 Final Project
# # Garret Mook, Katie Pell, Jorge Calderon
# # Spring 2022

# import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function
# # import outside.inside.genfa as eNFA

# # for every character in the input
# # current state on this input gives --> _______

# def test2(string, nfa):
#   start = nfa.start_state
#   for char in string:
#     reachable = nfa.transition_table[start][char]


# def test(string, nfa):
#     current = [0]*len(nfa.transition_table) # number of states, each has a zero for now
#     starting_state = 0 # this can be initialized to be whatever state it needs to be...
#     current[starting_state] = 1 # mark the starting state as visit-able without even reading input
#     # input_string = "1100" # BUG: THIS REQUIRES THAT INPUTS BE THE ACTUAL CHARACTERS 0 AND 1 THEMSELVES.... HOPEFULLY CAN TRANSLATE LATER...

#     while string != "":
#       for i in range(len(current)): # for every state
#         if current[i]: # if it's marked with a 1 in the 'current' vector
#           reachable = nfa.transition_table[i][int(string[0])] # mark all states in the closure of [state][input symbol] as reachable
#           next = [0] * len(nfa.transition_table) # create 'next' vector
#           for i in reachable:
#             next[i] = 1 # mark those as reachable in the 'next' vector

#       string = string[1:]
#       current = next

#     for i in range(len(current)):
#       if current[i] == 1 and i in nfa.final_states:
#         return True

#     return False


# def main():
#     # Example from: https://www.geeksforgeeks.org/conversion-of-epsilon-nfa-to-nfa/
#     transition_table = [[[], [1], [2]],[[], [0], []],[[3], [4], []],[[2], [], []],[[2], [], []]]
#     # goal = [[[3], [1,4]],[[], [0]],[[3], [4]],[[2], []],[[2], []]]

#     start_state = 0
#     final_states = [2]
#     num_states = len(transition_table)
#     symbols = ['a', 'b']

#     M2 = eFreeNFA.NFA([num_states, symbols, transition_table, start_state, final_states]).remove_epsilons() # One extra symbol for epsilon

#     # print(goal)
#     # print(M2.transition_table)
#     # print(M2.final_states)

#     print(test("110", M2))




# main()



# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

import outside.inside.eFreeNFA as efNFA # Import Katie's knfa.py file --> uses convert_nfa function
import outside.inside.epsilonNFA as reNFA

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
    x = reNFA.printInfo(reNFA.regexToNFA(userInput)) # G/J code to go from regex to epsilon-NFA --> returns tuple of NFA definition
    # print(x)
    return efNFA.NFA(x) # Return the NFA object corresponding to this userInput

def epsilonNFA_to_epsilonFreeNFA(M1):
    mid = M1.without_epsilons() # Remove epsilon transitions
    mid = mid.delete_states() # Remove any unnecessary states
    return mid

def main():
    usrInput = "a+b" # regex
    M1 = regex_to_epsilonNFA(usrInput) #  create epsilon NFA
    M2 = epsilonNFA_to_epsilonFreeNFA(M1) # creates epsilon-free NFA

    M1.print()

    print()
    # testA = ["bcacbcacbcacacacacbcbcbcbcacacbc", "acacbcacacacacacacbcbcbc", "acacacbc", "aaaabbbbc", "abc"] # First 3 should pass, last 2 should fail
    testA = ["a", "b", "ab", "abb", ""]
    for string in testA:
        print(M2.check_string(string))

    
main()

# python old.py "ab"
# python old.py "a+b"
# python old.py "((a+b)c)*"
# python old.py "a+b+c"
# python old.py "a+b"
# python old.py "a*"
# python old.py "(ab)*"
# python old.py "(b+a)*"
# python old.py "(a+b)+(c+d)"