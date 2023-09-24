from Calculator.calculator import *
from Parsing.parsing import *
import sys

def computeIO(value):
    """Calculation of expression (from file input or program execution)"""

    if len(value) > 1:
        try:
            result = calculator(determination_calculation_priority(tokenizer(init_parser(''.join(value[1:])))))
            if isnumber(result):
                print(result)
                return result
            else:
                print('Invalid expression')
                exit(0)
        except OverflowError:
            print('OverFlow')
            exit(0)
        except:
            print('Invalid expression')
            exit(0)

    else:
        while True:

            try:
                expression = input('>>>').replace(' ', '')
            except KeyboardInterrupt:
                break

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
                

computeIO(sys.argv)