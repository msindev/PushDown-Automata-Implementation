import FileHandler as fh

class PDA:

    def __init__(self):
        stack = []

    def compute(self, inputString, parsedLines):
        #Retrieve all information
        initStackSymbol = parsedLines['initial_stack']
        stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']

        global currentStackSymbol
        global currentState

        for char in inputString:
            for production in productions:
                if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                    currentState = production[3]
                    if(len(production[4]) > 1):
                        stack.append(upper(char))
                    elif ((production[4] == e) and (len(stack) != 0)):
                        stack.pop()
            print('Moved: ({}, {}'.format(currentState, stack))

        if(len(stack) == 0 or currentState in finalStates):
            print('String accepted.')
        else:
            print('String rejected.')

    def main(self):
        automataFilePath = input('Enter the automata file path: ')
        lines = fh.readFile(automataFilePath)
        inputString = input('Enter input String: ')
        inputString = inputString.rstrip()
        parsedLines = fh.parseFile(lines)
        compute(inputString, parsedLines)
