# Main file for CS 454 Final Project
# Garret Mook, Katie Pell, Jorge Calderon
# Spring 2022

from re import I
import outside.inside.knfa as knfa # Import Katie's knfa.py file --> uses convert_nfa function
import outside.inside.parse as parse # Import Jorge's parse.py file --> uses parse function

def main():
    # regex = input("Enter a regular expression: ")
    regex =  "(a+a.b)*.(a+E)"
    print(parse.parse(regex))

    # Current test code --> Uses example NFA
    num_states = 3
    num_symbols = 3 # Already includes epsilon
    epsilon_NFA = knfa.NFA(num_states, num_symbols) # Constructor for empty transition table - filled in during conversion

    # # Goal code --> template for when Garret outputs the transition table for the E-NFA
    # num_states = len(gtable) # Number of nested lists in gtable (number of states)
    # num_symbols = len(gtable[0]) # Number of nested lists in each nested list in gtable (number of symbols) --> ALREADY WILL INCLUDE E IN NUMBER OF COLUMNS
    # epsilon_NFA = knfa.NFA(len(gtable), len(gtable[0]) - 1, gtable) # Use Garret's output as transition table input, removing E column
   
    epsilon_free_NFA = knfa.convert_nfa(epsilon_NFA)
    epsilon_free_NFA.print()
    
    
main()
