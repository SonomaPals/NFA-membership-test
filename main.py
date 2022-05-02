# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

from re import I
import outside.inside.knfa as knfa # Import Katie's knfa.py file --> uses convert_nfa function
import outside.inside.parse as parse # Import Jorge's parse.py file --> uses parse function

def empty(num_states, num_symbols):
    empty_table = []
    for i in range(num_states):
        empty_table.append([])
        for j in range(num_symbols):
            empty_table[i].append([])

    return empty_table


def main():
    # regex = input("Enter a regular expression: ")
    # regex =  "(a+a.b)*.(a+E)"
    # print(parse.parse(regex))

    # Example from: https://www.geeksforgeeks.org/conversion-of-epsilon-nfa-to-nfa/
    transition_table = [
        [
            [], [1], [0, 2]
        ],
        [
            [], [0], [1]
        ],
        [
            [3], [4], [2]
        ],
        [
            [2], [], [3]
        ],
        [
            [2], [], [4]
        ]
    ]
    num_states = len(transition_table)
    num_symbols = len(transition_table[0]) - 1 # Don't count the epsilon column

            
    goal = [
                [
                    [3], [1,4]
                ],
                [
                    [], [0]
                ],
                [   
                    [3], [4]
                ],
                [
                    [2], []
                ],
                [
                    [2], []
                ]
            ]
    newNFA = knfa.NFA(num_states, num_symbols, transition_table).remove_epsilons() # One extra symbol for epsilon
    newNFA.print()
    print("****************************")
    for item in goal:
        print(item)

    
main()


