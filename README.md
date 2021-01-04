# PushDown Automata Simulation

The code PDA . py file  shows the transistions for a PDA.
## Input-
The automata file is loaded from a specific file which has the following input format-

    Line 1: Total States
    Line 2: Input Word Symbols
    Line 3: Stack Symbols
    Line 4: Initial State Symbol
    Line 5: Initial Stack Symbol
    Line 6: List of Final States
    Line 7 and onwards: Productions in form of
         (Current State, Current Input Symbol, Current Top of Stack, Next State, Push/Pop Operation Symbol)

Currently 3 examples have been included-

 1. 0ⁿ1ⁿ  
 2. Number of 0's = Number of 1's
 3. Palindrome - wcwᴿ
## Usage
To run use - `python PDA.py`
You can also define your own productions and use them. Make sure to give full path of the automata file, or better keep the automata file in the same directory as the program.

## Output
![Pushdown Automata Working Example Screenshot](https://github.com/mohitwildbeast/PushDown-Automata-Implementation/blob/master/PushDown%20Automata%20Example%20Screenshot.png)
