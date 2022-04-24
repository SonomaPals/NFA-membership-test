# Regular expression and NFA membership test
### Input
A regular expression <i>R</i>
<br/>
A string <i>w</i>
<br/>

### Task
<ol>
  <li> Convert the regular expression R to an epsilon-NFA <i>M<sub>1</sub></i>. </li>
  <li> Remove epsilon transitions to obtain epsilon-free NFA <i>M<sub>2</sub>.</i> </li>
  <li> Test if the string w is accepted by the epsilon-free NFA <i>M<sub>3</sub>.</i> </li>
  </ol>

### Output

True/false: Whether or not the string w is the in the language of the regular expression R, i.e. if w is in L(R).
<br/>

### Contributors
Garret Mook
<br/>
Katie Pell
<br/>
Jorge Calderon

### Individual file information
<b>nfa-conversion.py</b>
<ul>
  <li><em>Input</em>: Transition table for epsilon-NFA</li>
  <li><em>Output</em>: Equivalent epsilon-free NFA, represented by a transition table</li>
</ul>
