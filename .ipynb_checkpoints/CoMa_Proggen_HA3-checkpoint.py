def linear_regression(points, lines):
    int_list = []

    def get_linedistance(points, lines):
        for i in range(len(lines)):
            for j in range(len(points)):
                a = lines[i][0]
                x = points[j][0]
                b = lines[i][1]
                y = points[j][1]
                int_list.append(
                    ((a * x) + b - y)**2)
        return (int_list)

    def get_min(int_list):
        if len(int_list) == 0:
            return None
        else:
            min_distance = min(int_list)
            print(min_distance)

    get_linedistance(points, lines)
    get_min(int_list)


linear_regression([(-1, 1), (0, 2), (1, 1), (3, -1)], [(1, 1), (-1, 2)])
