

import outside.inside.eFreeNFA as eFreeNFA # Import Katie's knfa.py file --> uses convert_nfa function

def get_num(nfa, char):
  for i in range(len(nfa.symbols)):
    if nfa.symbols[i] == char:
      return i

  return False

def check(nfa, string):
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






