# regular-expression-NFA-membership-test
input a regular expression,  outputs ‘yes’ if w is in L(R), ‘no’ else
<br/>
<br/>
*Task:*
<br/>
Implement a program that tests membership of a given string w in a regular expression R.
Specifically, your program will take as input a regular expression (such as (a ∪ a.b)*.(a ∪ epsilon) and
a string w = abaab, and outputs ‘yes’ if w is in L(R), ‘no’ else. Three steps are involved in
solving this problem: 1) convert the regular expression to an epsilon-NFA 2) remove epsilon-moves and 3)
Test if w is accepted by the epsilon-free NFA.
<br/>
<br/>
**Programmed By:
<br/>
Garret Mook
<br/>
Katie Pell
<br/>
Jorge Calderon**
