def evaluate(string):
    lis = splitby(string, "+(){}[]")
    lis = [x.strip(' ') for x in lis]

    for i in range(len(lis)):
        lis[i] = evaluate_mul_div(lis[i])

    output = float(lis[0])
    lis = lis[1:]

    while len(lis) > 0:
        operator = lis[0]
        number = int(lis[1])
        lis = lis[2:]

        if operator == "+":
            output += number

    return output


def evaluate_mul_div(string):
        lis = splitby(string, "x/")
        if len(lis) == 1:
            return lis[0]
        
        output = int(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = int(lis[1])
            lis = lis[2:]

            if operator == "x":
                output *= number

            elif operator == "/":
                output /= number

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


testcases = ["1+(1+1)*(1+1)","{1+1}*[1+1]+38","[{1}+5]*({2}+[{1*(3)}+2])","{3+2)+1"]

for case in testcases:
    print(case, "->", evaluate(case))