def evaluate(string):
    # convert string to list
    current = ""
    open_brackets = ["{", "[", "("]
    closed_brackets = ["}", "]", ")"]

    for i in string:
        if i in open_brackets: # offene Klammer --> current auf "" setzen und Inhalt auf Stack packen
            stack = stack.append(current)
            evaluate(string.replace(current + i,"",1)) #REKURSION
        elif i in closed_brackets: # geschlossene Klammer --> Current auswerten und mit Stack verbinden
            current = eval_depth0(current)
            current = stack[-1] + current
        else: # keine Klammer --> string bis zur nächsten Klammer in current speichern
            current += i
    return current


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