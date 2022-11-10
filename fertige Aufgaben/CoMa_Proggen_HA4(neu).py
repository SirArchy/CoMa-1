def linear_regression(points, lines):
    """
    Führt das Sieb des Eratosthenes aus.
    Input: Ein integer n, mindestens 2
    Output: Eine Liste aller Primzahlen kleiner gleich n
    """
    r_squared_list = []
    for i in range(len(lines)):
        r_squared_list.append(get_linedistance(points, lines[i]))
    return get_min(r_squared_list)  # minimaler Wert der Liste der R² (int)


def get_linedistance(points, line):
    """
    Führt das Sieb des Eratosthenes aus.
    Input: Ein integer n, mindestens 2
    Output: Eine Liste aller Primzahlen kleiner gleich n
    """
    r_squared = 0
    a = line[0]
    b = line[1]
    for j in range(len(points)):
        x = points[j][0]
        y = points[j][1]
        r_squared += ((a * x) + b - y) ** 2
    return r_squared  # aufsummiertes R² (int)


def get_min(int_list):
    """
    Führt das Sieb des Eratosthenes aus.
    Input: Ein integer n, mindestens 2
    Output: Eine Liste aller Primzahlen kleiner gleich n
    """
    if not int_list:
        return None
    else:
        min_distance = min(int_list)
        return min_distance  # kleinster Eintrag der Liste (int)