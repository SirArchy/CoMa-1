def evaluate(string):
    stack = [] # Initialize the stack
    current = ""
    depth = 0
    max_depth = 0

    open_brackets = ["{", "[", "("]
    closed_brackets = ["}", "]", ")"]

    if not check(string, open_brackets, closed_brackets):
        raise Exception ("syntaktisch inkorrekt")

    i = 0
    while i < len(string):
        if string[i] in open_brackets: 
            stack.append(current) # Use the append method of the list
            current = ""
            depth += 1
            max_depth = max(depth, max_depth)
        elif string[i] in closed_brackets: 
            current = eval_depth0(current) # Instead of eval_depth0
            current = stack.pop() + current
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
    return term


def evaluate_mul(string_list): #WORKS
    string_list = splitby(string_list, "*") 

    if len(string_list) == 1:
        return string_list[0]

    output = int(string_list[0])
    string_list = string_list[1:]

    while len(string_list) > 0:
        operator = string_list[0]
        number = int(string_list[1])
        string_list = string_list[2:]
        if operator == "*":
            output *= number             
    return str(output)


def evaluate_add(string_list): #WORKS
    output = int(string_list[0])
    string_list = string_list[1:]

    while len(string_list) > 0:
        number = int(string_list[1])
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


testcases = ["15+20*{1*2+[3+2*3+4+5]+5}*{(1+2)+3}*6+(((3)))", "15+20*{1*2+[3+2]+5}*{(1+2)+3}*6+(((3)))","1+(1+1)*(1+1)","{1+1}*[1+1]+38","[{1}+5]*({2}+[{1*(3)}+2])","{3+2)+1"]
for case in testcases:
    print(case, "->", evaluate(case))