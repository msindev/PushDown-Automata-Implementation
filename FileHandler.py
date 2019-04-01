import os

class FileHandler:

    def __init__(self):
        pass

    def readFile(self, filePath):
        lines=[]
        if(os.path.isfile(filePath)):
            try:
                with open(filePath) as file:
                    lines = [line.rstrip() for line in file]
            except IOError as e:
                print("File could not be opened.")
                return 0
        else:
            print('{} :File was not found in the specified path.'.format(filePath))
        return lines

    def ParseFile(self,lines):
        ''' Line 1: Total States
            Line 2: Input Word Symbols
            Line 3: Stack Symbols
            Line 4: Initial State Symbol
            Line 5: Initial Stack Symbol
            Line 6: List of Final States
            Line 7 and onwards: Productions in form of
                    (Current State, Current Input Symbol, Current Top of Stack, Next State, Push/Pop Operation Symbol)
            '''
        states = lines[0].rstrip()
        input_symbols = lines[1].rstrip()
        stack_symbols = lines[2].rstrip()
        initial_state = lines[3][0]
        initial_stack = lines[4][0]
        final_states = lines[5]
        productions = lines[6:]
        return (states, input_symbols, stack_symbols, initial_state, initial_stack, final_states, productions)

    
