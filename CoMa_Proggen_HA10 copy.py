
def evaluate(string):
    # convert string to list
    current = ""
    stack = []
    open_brackets = ["{", "[", "("]
    closed_brackets = ["}", "]", ")"]
    for i in string:
        if i in open_brackets:
            stack.append(current)
            current = ""
        elif i in closed_brackets:
            current = evaluate_mul_div(current)
            current = stack[-1] + current
            stack.pop
        else:
            current += i
    return stack


def evaluate_mul_div(string):
        lis = splitby(string, "+*")
        if len(lis) == 1:
            return lis[0]
        
        output = int(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = int(lis[1])
            lis = lis[2:]

            if operator == "*":
                output *= number

            elif operator == "+":
                output += number

        return str(output)


def splitby(string, separators):
        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                lis.append(current)
                lis.append(ch)
                current = ""
            else:
                current += ch
        lis.append(current)
        return lis


testcases = ["15+20* {1*2+[3+2]+5}*{(1+2)+3}*6+(((3)))","1+(1+1)*(1+1)","{1+1}*[1+1]+38","[{1}+5]*({2}+[{1*(3)}+2])","{3+2)+1"]
for case in testcases:
    print(case, "->", evaluate(case))

"""
def convert_string_to_matrix(string):
    matrix_A = string.split(",")
    matrix_A_list = []
    for item in matrix_A:
        subl = []
        for num in item.split():
            subl.append(int(num))
        matrix_A_list.append(subl)
    return matrix_A_list


def convert_matrix_to_string(matrix):
    s = ''
    for i in range(len(matrix)):
        s += str(matrix[i]).replace(',', '')
        if i != len(matrix) -1: 
            s += ', '
    string_matrix = s.replace('[', '').replace(']', '')
    return string_matrix
"""