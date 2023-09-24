
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

def small_calculator(parsing_list):
    """Evaluating a tiny mathematical expression"""

    def _pow(parsing_list):
        
        parsing_list = parsing_list[::-1]

        for ind, pw in enumerate(parsing_list):
            if pw == '^':

                if parsing_list[ind + 1] == '-inf': ############
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

def calculator(priority_list):
    """Calculation of mathematical expression from the list generated based on priorities"""

    if len(priority_list) == 1:
        return priority_list[0]
    
    for ind, item in enumerate(priority_list):
        if item in ['*', '/', '+', '-', '^']:
            data = [priority_list[ind - 2], item, priority_list[ind - 1]]
            priority_list = replacer(priority_list, str(small_calculator(data)), ind-2, ind)
            return calculator(priority_list)

