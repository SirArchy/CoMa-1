def abstand(s, t, dateiname="labyrinth.dat"):
    """
    input:
    s() =
    t() =
    dateiname(string) =
    output:
    length of path(int) = 
    """
    maze = labyrinth_einlesen(dateiname)
    path = breitensuche(maze, s, t)
    if path == None:
        return -1
    else:
        return len(path) - 1


def breitensuche(maze, start, end):
    """
    input:
    maze(list) - Labyrinth durch das gesucht wirds
    start(tuple) - Startkoordinate (Reihe, Spalte)
    end(tuple) - Endkoordinate (Reihe, Spalte)
    output:
    path(int) - kürzester Weg von Startpunkt zum Endepunkt
    """
    queue = [start]
    visited = set()

    while len(queue) != 0:
        if queue[0] == start:
            path = [queue.pop(0)] 
        else:
            path = queue.pop(0)
        front = path[-1]
        if front == end:
            return path
        elif front not in visited:
            for i in benachbarteFelder(maze, front, visited):
                newPath = list(path)
                newPath.append(i)
                queue.append(newPath)
            visited.add(front)
    return None


def benachbarteFelder(maze, space, visited):
    """
    input:
    space(tuple) - beinhaltet Koordinate (row, col)
    output:
    final(list) - alle benachbarten passierbaren Felder
    """
    # added alle benachbarten Koordinaten zu spaces
    spaces = list()
    if space[0] > 0:
        spaces.append((space[0] - 1, space[1]))  # Up
    if space[0] < len(maze) - 1:
        spaces.append((space[0] + 1, space[1]))  # Down
    if space[1] > 0:
        spaces.append((space[0], space[1] - 1))  # Left
    if space[1] < len(maze[0]) - 1:
        spaces.append((space[0], space[1] + 1))  # Right

    # prüft ob space Passable ist und fügt es an final an
    final = list()
    for i in spaces:
        if maze[i[0]][i[1]] == 'P' and i not in visited:
            final.append(i)
    return final


def labyrinth_einlesen(filename):
    """
    input:
    filename(string) - 
    output:
    maze
    """
    # filename = "C:\\Users\Fabian\PycharmProjects\CoMa_Proggen\labyrinth.dat"
    maze = list()
    with open(filename, "r") as file:
        for line in file:
            maze.append(list(line.rstrip()))
    return maze



print(abstand((0,1), (0,1), "C:\\Users\Fabian\PycharmProjects\CoMa_Proggen\labyrinth.dat"))
print(abstand((0,9), (2,2)))
print(abstand((0,1), (0,7)))
print(abstand((0,9),(0,7)))

