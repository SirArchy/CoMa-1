def linear_regression(points, lines):
    """
    Berechnet den kleinsten quadratischen Abstand von den Geraden "lines" zur
    Punktmenge points
    Input: points | List, lines | List
    Output: get_min(r_squared_list) : Int
    """
    r_squared_list = []
    for i in range(len(lines)):
        r_squared_list.append(get_linedistance(points, lines[i]))
    return get_min(r_squared_list)  # minimaler Wert der Liste der R²


def get_linedistance(points, line):
    """
    Berechnet quadratischen Abstand der Gerade "line" zur Punktmenge "points"
    Input: points | List, line | Tuple
    Output: r_squared | Int
    """
    r_squared = 0
    a = line[0]
    b = line[1]
    for j in range(len(points)):
        x = points[j][0]
        y = points[j][1]
        r_squared += ((a * x) + b - y) ** 2
    return r_squared  # aufsummiertes R²


def get_min(int_list):
    """
    Gibt aus Liste ganzer Zahlen "int_list" das Minimum zurück
    Input: int_list | List
    Output: min_distance | Int
    """
    if not int_list:
        return None
    else:
        min_distance = min(int_list)
        return min_distance  # kleinster Eintrag der Liste

def getminidx (intlist):
    if len(intlist) == 0:
        return None
    else:
        minidx = intlist[0]
        for i in range(len(intlist) -1):       
            if minidx > intlist[i+1]:
                minidx = intlist[i+1]
        return minidx

L = [1,2,3,4,5]
P = L[1:-1]
print(P)