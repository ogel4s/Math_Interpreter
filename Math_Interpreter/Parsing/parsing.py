
def str_to_number(value):
    """Translate a string that contains a number into a number"""

    number = complex(value)

    if number.imag == 0:
        return float(number.real)
    else:
        return number
    
def validator(parsing_list):
    """Verify the parsed list [Note:This function may be updated if new items are encountered.]"""

    # [Check mode] Negetive
    for ind, neg in enumerate(parsing_list):
        if (neg == '-' and parsing_list[ind - 1] in ['/', '*', '^', '+', '-']):
            return False
    
    # [Check mode] number between two parentheses 
    for ind, finall in enumerate(parsing_list):
        if (isnumber(finall) and parsing_list[ind - 1] == '(' and parsing_list[ind + 1] == ')' and finall[0] != '(') and ('j' not in finall and str_to_number(finall) < 0):
            return False
    
        
    return True

def isnumber(value):
    """Checking the number of a string"""
    try:
        number = complex(value)
        return True
    except ValueError:
        return False

def replacer(parsing_list, value, start, end):
    """Replace part of a list with another value"""
    return parsing_list[:start] + [value] + parsing_list[end + 1:]

def init_parser(expression):
    """Initial parsing of the expression into a separated list of numbers and symbols"""

    expression = expression.replace('**', '^').replace(' ', '')

    # Separation of numbers from operators and symbols
    parsing = []

    start = 0
    end = 0

    while end < len(expression):

        if expression[start].isdigit():
            temp = ""

            while end < len(expression) and expression[end].isdigit():
                temp += expression[end]
                end += 1
            
            parsing.append(temp)

            start = end
        
        else:
            parsing.append(expression[start])
            start += 1
            end += 1
    
    return parsing

def tokenizer(parsing_list):
    """Normalization of the result of the initial parsing of the expression for use in the calculation unit"""

    
    # Remove empty character [init]
    while '' in parsing_list:
        parsing_list.remove('')

    # Calculation of sentence marks and removal of extra parts [Note: This section will be updated if a new addition is encountered]
    for ind, ch in enumerate(parsing_list):
        if (ch == '-' and parsing_list[ind + 1] == '+') or (ch == '+' and parsing_list[ind + 1] == '-'):
            parsing_list = replacer(parsing_list, '-', ind, ind+1)
            return tokenizer(parsing_list)
    
    # Calculate symbol inf number [Note: This section will be updated if a new addition is encountered]
    for ind, inf in enumerate(parsing_list):
        if inf == '-(-inf)':
            parsing_list[ind] = 'inf'
            return tokenizer(parsing_list)

    # Inf number
    for ind, inf in enumerate(parsing_list):
        if inf == 'n':
            parsing_list = replacer(parsing_list, parsing_list[ind - 1] + inf + parsing_list[ind + 1], ind-1, ind+1)
            return tokenizer(parsing_list)
    
    # Decimal number
    for ind, point in enumerate(parsing_list):
        if point == '.':
            parsing_list = replacer(parsing_list, parsing_list[ind - 1] + point + parsing_list[ind + 1], ind-1, ind+1)
            return tokenizer(parsing_list)
    
    # Scientific number
    for ind, e in enumerate(parsing_list):
        if e == 'e':
            parsing_list = replacer(parsing_list, parsing_list[ind - 1] + e + parsing_list[ind+1] + parsing_list[ind+2], ind-1, ind+2)
            return tokenizer(parsing_list)
    
    # Complex number
    for ind, j in enumerate(parsing_list):
        if j == 'j':
            if parsing_list[ind - 4] == '-':
                parsing_list = replacer(parsing_list, parsing_list[ind - 5] + parsing_list[ind - 4] + parsing_list[ind - 3] + parsing_list[ind - 2] + parsing_list[ind - 1] + j + parsing_list[ind + 1], ind-5, ind+1)
                return tokenizer(parsing_list)
            else:
                parsing_list = replacer(parsing_list, parsing_list[ind - 4] + parsing_list[ind - 3] + parsing_list[ind - 2] + parsing_list[ind - 1] + j + parsing_list[ind + 1], ind-4, ind+1)
                return tokenizer(parsing_list)
    
    # Negetive [Needs final validation]
    for ind, neg in enumerate(parsing_list):
        
        if (neg == '-' and ind == 0 and isnumber(parsing_list[ind + 1])) or \
           (neg == '-' and isnumber(parsing_list[ind + 1]) and parsing_list[ind - 1] in ['/', '*', '+', '-', '^', '(', '']) or \
           ((neg == '-' or (lambda value: all([True if item == '-' else False for item in value]))(neg)) and parsing_list[ind + 1] == '-'):
            
            parsing_list = replacer(parsing_list, neg + parsing_list[ind + 1], ind, ind+1)
            return tokenizer(parsing_list)
        
    # Positive
    for ind, pos in enumerate(parsing_list):
        if (pos == '+' and isnumber(parsing_list[ind + 1]) and parsing_list[ind - 1] in ['/', '*', '+', '-', '^', '(']) or \
           ((pos == '+' or (lambda value: all([True if item == '+' else False for item in value]))(pos)) and parsing_list[ind + 1] == '+'):
            parsing_list = replacer(parsing_list, pos + parsing_list[ind + 1], ind, ind+1)
            return tokenizer(parsing_list)
        
    # Removing repeated negative and positive symbols
    for ind, neg_pos in enumerate(parsing_list):
        if (lambda value: all([True if item == '-' else False for item in value]))(neg_pos)  and len(neg_pos) > 1:#######
            parsing_list[ind] = '+' if len(neg_pos) % 2 == 0 else '-'
            return tokenizer(parsing_list)
        elif (lambda value: all([True if item == '+' else False for item in value]))(neg_pos) and len(neg_pos) > 1:#######
            parsing_list[ind] = '+'
            return tokenizer(parsing_list)
     
    # Removing ineffective symbols and determining the final causes of the expression
    for ind, sym in enumerate(parsing_list):
        if (sym == '+' and isnumber(parsing_list[ind + 1]) and parsing_list[ind - 1] in ['/', '*', '+', '-', '^', '(']) or \
           (sym == '+' and parsing_list[ind - 1] == '(' and parsing_list[ind + 1] == '(') or \
           (sym == '+' and ind == 0):
            
            parsing_list[ind] = ''    

    ### Finall normalize [Note: This section will be updated if a new addition is encountered] ###

    # Remove empty characters [1]
    while '' in parsing_list:
        parsing_list.remove('')
    
    # Entering the negative behind a complex number into it
    for ind, finall in enumerate(parsing_list):
        if finall[0] == '-' and 'j' in finall:
            finall = finall[1:]
            new_value = str(-1 * str_to_number(finall))
            parsing_list[ind] = new_value

    # Put a negetive number between two parentheses [Needs final validation]
    for ind, finall in enumerate(parsing_list):
        if (isnumber(finall) and parsing_list[ind - 1] == '(' and parsing_list[ind + 1] == ')' and finall[0] != '(') and ('j' not in finall and str_to_number(finall) < 0):
            parsing_list = replacer(parsing_list, parsing_list[ind - 1] + finall + parsing_list[ind + 1], ind-1, ind+1)
            return tokenizer(parsing_list)
    
    # Remove positive symbol from a number
    for ind, finall in enumerate(parsing_list):
        if isnumber(finall) and finall[0] == '+':
            parsing_list[ind] = finall[1:]
            return tokenizer(parsing_list)
    
    # Remove parentheses from inf number
    for ind, finall in enumerate(parsing_list):
        if (finall in ['inf', '-inf'] and parsing_list[ind - 1] == '(' and parsing_list[ind + 1] == ')'):
            parsing_list[ind - 1] = ''
            parsing_list[ind + 1] = ''
            return tokenizer(parsing_list)
        elif ('inf' in finall and '(' in finall and ')' in finall):
            new_value = ''.join([item for item in finall if item not in [')', '(']])
            parsing_list[ind] = ''.join(tokenizer(init_parser(new_value)))
            return tokenizer(parsing_list)

    # Remove empty characters [2]
    while '' in parsing_list:
        parsing_list.remove('')
    
    # Verifying the validity of the parsed list
    if validator(parsing_list):
        return parsing_list
    
    return tokenizer(parsing_list)

def determination_calculation_priority(data):
    """Generating a sequence of input expressions based on the precedence of operators to calculate the final result of the input expression"""

    # Determining the precedence of operators
    precedence = {
        '^': 3,
        '/': 2,
        '*': 2,
        '-': 1,
        '+': 1
    }

    # Determining the associativity of operators
    associativity = {
        '^': 'R',
        '/': 'L',
        '*': 'L',
        '-': 'L',
        '+': 'L'
    }

    
    data += ['0']
    operators = []
    output = []

    while len(data) != 1:
        current_token = data.pop(0)

        if isnumber(current_token):
            
            output.append(current_token)

        elif current_token in precedence.keys():
            

            while len(operators) != 0:

                satisfied = False

                if operators[-1].isalpha():
                   
                    satisfied = True

                if operators[-1] not in [')', '(']:
                    if precedence[operators[-1]] > precedence[current_token]:
                        satisfied = True

                    elif precedence[operators[-1]] == precedence[current_token]:
                        if associativity[operators[-1]] == 'L':
                            satisfied = True

                satisfied = satisfied and operators[-1] != '('

                if not satisfied:
                    break

                output.append(operators.pop())

            operators.append(current_token)

        elif current_token == "(":            
            operators.append(current_token)

        elif current_token == ")":
            while True:
                if len(operators) == 0:
                    break

                if operators[-1] == "(":
                    break

                output.append(operators.pop())

            if len(operators) != 0 and operators[-1] == "(":
                operators.pop()

    output.extend(operators[::-1])

    return output

