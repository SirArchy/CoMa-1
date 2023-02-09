import re


def evaluate(string):
    stack = []
    current = ""
    depth = 0
    max_depth = 0

    open_brackets = ["{", "[", "("]
    closed_brackets = ["}", "]", ")"]
    operators = ["*",'+', "{", "[", "(","}", "]", ")"]

    number_pattern = r'[a-zA-Z]'
    if re.search(number_pattern, string):
        raise Exception ("syntaktisch inkorrekt")

    if not check(string, open_brackets, closed_brackets):
        raise Exception ("syntaktisch inkorrekt")

    i = 0
    while i < len(string):
        if string[i] in open_brackets:
            if string[i-1] not in operators and i != 0:
                raise Exception ("syntaktisch inkorrekt")
            stack.append(current)
            current = ""
            depth += 1
            max_depth = max(depth, max_depth)
        elif string[i] in closed_brackets:
            if i != len(string)-1:
                if string[i+1] not in operators or string[i+1] in open_brackets:
                    raise Exception ("syntaktisch inkorrekt")
            current = eval_depth0(current) 
            current = stack.pop() + str(current)
            depth -= 1
        else: 
            current += string[i]
        i += 1
    return (eval_depth0(current), max_depth)


def eval_depth0(term):
    term = splitby(term, "+")
    for i in range(len(term)):
        term[i] = evaluate_mul(term[i])  
    term = evaluate_add(term) 
    return int(term)


def evaluate_mul(string_list): #WORKS
    string_list = splitby(string_list, "*") 

    if len(string_list) == 1:
        return string_list[0]
    try:
        output = int(string_list[0])
    except ValueError:
        raise Exception ("syntaktisch inkorrekt")
    string_list = string_list[1:]

    while len(string_list) > 0:
        operator = string_list[0]
        try:
            number = int(string_list[1])
        except ValueError:
            raise Exception ("syntaktisch inkorrekt")
        string_list = string_list[2:]
        if operator == "*":
            output *= number             
    return str(output)


def evaluate_add(string_list): #WORKS
    try:
        output = int(string_list[0])
    except ValueError:
        raise Exception ("syntaktisch inkorrekt")
    
    string_list = string_list[1:]

    while len(string_list) > 0:
        try:
            number = int(string_list[1])
        except ValueError:
            raise Exception ("syntaktisch inkorrekt")
        output += number
        string_list = string_list[2:]
    return str(output)


def check(myStr, open_brackets, closed_brackets):
    stack = []
    for i in myStr:
        if i in open_brackets:
            stack.append(i)
        elif i in closed_brackets:
            pos = closed_brackets.index(i)
            if ((len(stack) > 0) and
                (open_brackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def splitby(string, separator): #WORKS
        lis = []
        current_term = ""
        for ch in string:
            if ch in separator:
                lis.append(current_term)
                lis.append(ch)
                current_term = ""
            else:
                current_term += ch
        lis.append(current_term)
        return lis

