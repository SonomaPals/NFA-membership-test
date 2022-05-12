# Regular expression/NFA membership test

## Contributors
<ul>
  <li><a href="https://github.com/jorge747-code">Jorge Calderon</a></li>
  <li><a href="https://github.com/gmook9">Garret Mook</a></li>
  <li><a href="https://github.com/katiepell42">Katie Pell</a></li>
  </ul>

## Usage
  ```
  main.py
  ```

## Input
A regular expression <i>R</i>
<br>
<ul>
The following regular expression conventions are recognized by this program:
<ul>
  <li> The only input characters permitted are lowercase letters a-z and numeric digits 0-9</li>
  <li> Parentheses may be used to manipulate order of operation</li>
  <li> Epsilon is represented using the symbol <i>E</i></li>
  <li> A union is represented by the symbol <i>+</i></li>
  <li> The Kleene star is represented by the standard symbol <i>*</i></li>
  <li> Concatenation is represented by the symbol <i>.</i>
  <ul>
    <i>Note: implicit concatenation is not permitted, i.e. "aba" should be written as a.b.a</i>
    </ul>
  </li>
 
</ul>
  </ul>


A string <i>w</i> <br>



## Task
<ol>
  <li> Convert the regular expression R to an epsilon-NFA <i>M<sub>1</sub></i>. </li>
  <li> Remove epsilon transitions to obtain epsilon-free NFA <i>M<sub>2</sub>.</i> </li>
  <li> Test if the string w is accepted by the epsilon-free NFA <i>M<sub>2</sub>.</i> </li>
  </ol>

## Output

True/false: Whether or not the string w is the in the language of the regular expression R, i.e. if w is in L(R).
<br/>

