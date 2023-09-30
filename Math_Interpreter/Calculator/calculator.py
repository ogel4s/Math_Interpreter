import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent).replace('\\', '/'))

from Trigonometry.trigonometry import *

tri_func = ['sin','cos','tan','cot','sec','csc','sinh','cosh','tanh','coth','csch','sech','arcsin','arccos','arctan','arccot','arcsec','arccsc','arcsinh','arccosh','arctanh','arccoth','arcsech','arccsch']


def str_to_number(value):
    """Translate a string that contains a number into a number"""
    number = complex(value)

    if number.imag == 0:
        return float(number.real)
    else:
        return number

def replacer(parsing_list, value, start, end):
    """Replace part of a list with another value"""
    return parsing_list[:start] + [value] + parsing_list[end + 1:]

def number_calculator(parsing_list):
    """Evaluating a tiny mathematical expression"""

    def _pow(parsing_list):
        
        parsing_list = parsing_list[::-1]

        for ind, pw in enumerate(parsing_list):
            if pw == '^':

                if parsing_list[ind + 1] == '-inf':
                    value = ((str_to_number(parsing_list[ind + 1]) * -1) ** str_to_number(parsing_list[ind - 1]))

                elif parsing_list[ind + 1][0] == '(' and parsing_list[ind + 1][0] == '-' and 'j' not in parsing_list[ind + 1]:
                    number = str_to_number(str(str_to_number(parsing_list[ind + 1]))[1:])
                    value =  (number * -1) ** str_to_number(parsing_list[ind - 1])
                elif parsing_list[ind + 1][0] == '-':
                    number = str_to_number(parsing_list[ind+1][1:])
                    value = -1 * (number ** str_to_number(parsing_list[ind - 1]))
                else:
                    number = str_to_number(parsing_list[ind + 1])
                    value = number ** str_to_number(parsing_list[ind - 1])
                
                
                
                parsing_list = replacer(parsing_list, str(value), ind-1, ind+1)
                return _pow(parsing_list[::-1])
        
        return parsing_list[::-1]

    def _mul(parsing_list):

        for ind, mul in enumerate(parsing_list):

            if mul == '*':
                value = str_to_number(parsing_list[ind - 1]) * str_to_number(parsing_list[ind + 1])
                parsing_list = replacer(parsing_list, str(value), ind-1, ind+1)
                return _mul(parsing_list)
        
        return parsing_list
    
    def _div(parsing_list):

        for ind, div in enumerate(parsing_list):
            if div == '/':
                if str_to_number(parsing_list[ind + 1]) == 0 and str_to_number(parsing_list[ind - 1]) > 0:
                    value = float('inf')
                elif str_to_number(parsing_list[ind + 1]) == 0 and str_to_number(parsing_list[ind - 1]) < 0:
                    value = float('-inf')
                elif str_to_number(parsing_list[ind + 1]) == 0 and str_to_number(parsing_list[ind - 1]) == 0:
                    value = float('NAN')
                else:
                    value = str_to_number(parsing_list[ind - 1]) / str_to_number(parsing_list[ind + 1])
                    
                parsing_list = replacer(parsing_list, str(value), ind-1, ind+1)
                return _div(parsing_list)
        
        return parsing_list
    
    def _sum(parsing_list):

        for ind, sm in enumerate(parsing_list):
            if sm == '+':
                value = str_to_number(parsing_list[ind - 1]) + str_to_number(parsing_list[ind + 1])
                parsing_list = replacer(parsing_list, str(value), ind-1, ind+1)
                return _sum(parsing_list)
        
        return parsing_list
    
    def _sub(parsing_list):

        for ind, sub in enumerate(parsing_list):
            if sub == '-':
                value = str_to_number(parsing_list[ind - 1]) - str_to_number(parsing_list[ind + 1])
                parsing_list = replacer(parsing_list, str(value), ind-1, ind+1)
                return _sub(parsing_list)
        
        return parsing_list
    
    return str_to_number(_sum(_sub(_mul(_div(_pow(parsing_list)))))[0])

def trigonometry_calculator(parsing_list):

    try:

        if not any(map(lambda x: x in tri_func, parsing_list)) or len(parsing_list) == 1:
            return parsing_list
        
        for ind, tri in enumerate(parsing_list):
            
            if tri == 'sin':
                value = str(Trigonometry.sin(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'cos':
                value = str(Trigonometry.cos(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'tan':
                value = str(Trigonometry.tan(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'cot':
                value = str(Trigonometry.cot(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'sec':
                value = str(Trigonometry.sec(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'csc':
                value = str(Trigonometry.csc(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'sinh':
                value = str(Trigonometry.sinh(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'cosh':
                value = str(Trigonometry.cosh(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'tanh':
                value = str(Trigonometry.tanh(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'coth':
                value = str(Trigonometry.coth(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'sech':
                value = str(Trigonometry.sech(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'csch':
                value = str(Trigonometry.csch(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arcsinh':
                value = str(Trigonometry.arcsinh(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arccosh':
                value = str(Trigonometry.arccosh(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arctanh':
                value = str(Trigonometry.arctanh(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arccoth':
                value = str(Trigonometry.arccoth(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arcsech':
                value = str(Trigonometry.arcsech(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arccsch':
                value = str(Trigonometry.arccsch(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arcsin':
                value = str(Trigonometry.arcsin(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arccos':
                value = str(Trigonometry.arccos(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arctan':
                value = str(Trigonometry.arctan(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arccot':
                value = str(Trigonometry.arccot(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arcsec':
                value = str(Trigonometry.arcsec(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)
            elif tri == 'arccsc':
                value = str(Trigonometry.arccsc(str_to_number(parsing_list[ind - 1])))
                parsing_list = replacer(parsing_list, value, ind-1, ind)
                return trigonometry_calculator(parsing_list)

    except:
        return parsing_list
    
def calculator(priority_list):
    """Calculation of mathematical expression from the list generated based on priorities"""
    
    if len(priority_list) == 1:
        return priority_list[0]
    
    for ind, item in enumerate(priority_list):
        if item in ['*', '/', '+', '-', '^']:
            data = [priority_list[ind - 2], item, priority_list[ind - 1]]
            priority_list = replacer(priority_list, str(number_calculator(data)), ind-2, ind)
            return calculator(priority_list)
        elif item in tri_func:
            return calculator(trigonometry_calculator(priority_list))


