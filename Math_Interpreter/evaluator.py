from Calculator.calculator import *
from Parsing.parsing import *


def computeIO():

    while True:
        # Input
        try:
            expression = input('>>>').replace(' ', '').replace('**', '^').lower().replace('pi', '3.1415926535897932384626433832795')
        except KeyboardInterrupt:
            break
        
        # Calculate
        try:
            result = calculator(determination_calculation_priority(tokenizer(init_parser(expression))))
            if isnumber(result):
                print(result)
            else:
                print('Invalid expression')
        except OverflowError:
            print('OverFlow')
        except:
            print('Invalid expression')

computeIO()