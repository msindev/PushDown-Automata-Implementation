from FileHandler import FileHandler

class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, inputString, parsedLines):
        #Retrieve all information
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']

        currentStackSymbol = initStackSymbol
        currentState = initialState

        for char in inputString:
            print('Current TOS', currentStackSymbol)
            for production in productions:
                if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                    currentState = production[3]
                    if(len(production[4]) > 1):
                        self.stack.append(char)
                    elif ((production[4] == 'e') and (len(self.stack) != 0)):
                        print('Entered here')
                        self.stack.pop()
                        break
            currentStackSymbol = self.stack[len(self.stack)-1]
            print('Moved: ({}, {})'.format(currentState, self.stack))

            
        if(len(self.stack) == 1 or currentState in finalStates):
            print('String accepted by PDA.')
        else:
            print('String rejected by PDA.')

def main():
    fh = FileHandler()
    pda = PDA()
    automataFilePath = input('Enter the automata file path: ')
    lines = fh.readFile(automataFilePath)
    inputString = input('Enter input String: ')
    inputString = inputString.rstrip()
    parsedLines = fh.parseFile(lines)
    print(parsedLines)
    pda.compute(inputString, parsedLines)

if __name__ == '__main__':
    main()
