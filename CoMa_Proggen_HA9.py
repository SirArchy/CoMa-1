def evaluate(string):
    return None


def check(myStr):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                raise ValueError("syntaktisch inkorrekt") # muss geändert werden, muss eigene exception sein
    if len(stack) == 0:
        return "Balanced"
    else:
        raise ValueError("syntaktisch inkorrekt") # muss geändert werden, muss eigene exception sein

string = "((()"
print(check(string))


"""
print(evaluate("1+(1+1)*(1+1)")) # (5 , 1)
print(evaluate("{1+1}*[1+1]+38")) # (42 , 1)
print(evaluate("[{1}+5]*([{2}+[{1*(3)}+2])")) # (42 , 4)
print(evaluate("{3+2)+1")) # Exception ( "syntaktisch inkorrekt")
print(evaluate('4+c*(13)'))
print(evaluate('8-4'))
"""
