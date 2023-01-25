
def evaluate(string):
    string = string.replace(" ", "")    
    lis = splitby(string, "+")
    
    for i in range(len(lis)):
        lis[i] = evaluate_mul_div(lis[i])

    output = float(lis[0])
    lis = lis[1:]

    while len(lis) > 0:
        number = float(lis[1])
        lis = lis[2:]
        output += number

    return output


def evaluate_mul_div(string):
        lis = splitby(string, "*")
        if len(lis) == 1:
            return lis[0]
        
        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            number = float(lis[1])
            lis = lis[2:]
            output *= number

        return output


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

testcases = ["1+2*34+5*6", "1+2*34+5*6*2+3*5", "1+2*34+5*61+2*34+5"]

for case in testcases:
    print(case, "->", evaluate(case))