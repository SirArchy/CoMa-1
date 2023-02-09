import random


def updatePosition(n, m, pos, rnd):
    """ 
    input:
    n: Anzahl der Reihen des Welt-Rechtecks,
    m: Anzahl der Spalten des Welt-Rechtecks,
    pos: Position der Figur als nichtnegative ganze Zahl,
    rnd: zufälliger Float im halboffenen Intervall [0, 1),
    
    output:
    pos: aktualisierte Position der Figur als nichtnegative ganze Zahl
    """
    left_edge = []
    right_edge = []
    if n == 1 and m == 1:
        left_edge.append(0)
        right_edge.append(0)
    else:
        for i in range(0, (m * n) - 1, m): # linken Rand bestimmen
            left_edge.append(i)
        for j in range((m - 1), (m * n), m): # rechten Rand bestimmen
            right_edge.append(j)
    # Bewegung
    if 0 <= rnd < 0.25: # nach rechts
        if pos in right_edge:
            pos = pos - (m - 1)
        else:
            pos = pos + 1
    elif 0.25 <= rnd < 0.5: # nach links
        if pos in left_edge:
            pos = pos + (m - 1)
        else:
            pos = pos - 1
    elif 0.5 <= rnd < 0.75: # nach unten
        if ((n - 1) * m) <= pos <= ((n - 1) * m) + (m - 1):
            pos = pos - (m * (n-1))
        else:
            pos = pos + m
    elif 0.75 <= rnd < 1: # nach oben
        if 0 <= pos <= (m - 1):
            pos = pos + (m * (n-1))
        else:
            pos = pos - m
    return pos


def updatePositions(n,m,positions):
    """
    input:
    n: Anzahl der Reihen des Welt-Rechtecks,
    m: Anzahl der Spalten des Welt-Rechtecks,
    positions: Liste mit allen Positionen der Figuren
    
    output:
    keiner
    """
    for i in positions:
        rnd = random.random()
        i[1] = updatePosition(n, m, i[1], rnd)


def sortPositions(positions):
    """
    input:
    positions: Liste mit allen Positionen der Figuren
    
    output:
    pos: aufsteigend nach den zweiten Einträgen der Teillisten sortierte Liste mit Positionen
    """
    positions.sort(key=lambda x: x[1])


def extractSquare(positions):
    """
    input:
    positions: Liste mit allen Positionen der Figuren
    
    output:
    pos: alle Figuren auf dem Feld mit dem höchsten Index in positions
    """
    sortPositions(positions)
    square = [positions[-1]] #letzten Eintrag von positions an square anfügen
    del positions[-1]
    for i in reversed(positions): #von hinten durch die Liste iterieren
        if i[1] == square[0][1]:
            square.insert(0, i)
            del positions[-1]
            if len(positions) == 0:
                break
        else:
            break
    return (positions,square)


def giftExchange(square):
    """
    input:
    square: alle letzten Elemente mit dem gleichen Eintrag in der zweiten Position aus positions Liste
    
    output:
    keiner
    """
    nr_H = 0
    nr_HH = 0
    nr_ZH = 0
    nr_Z = 0
    # count positions
    for i in square:
        if i[0] == 'H':
            nr_H = nr_H + 1
        if i[0] == 'ZH':
            nr_ZH = nr_ZH + 1
    # Austausch a)
    if nr_ZH > 0 and nr_H > 0:
        for i in square:
            if i[0] == 'H':
                i[0] = 'HH'
    # count positions
    for i in square:
        if i[0] == 'Z':
            nr_Z = nr_Z + 1
        if i[0] == 'HH':
            nr_HH = nr_HH + 1
        if i[0] == 'H':
            nr_H = nr_H + 1
    # Austausch b)
    if nr_Z > 0 and nr_H > 0 or nr_Z > 0 and nr_HH > 0:
        if nr_Z >= (2*nr_HH):
            for i in square:
                if i[0] == 'H':
                    i[0] = 'Z'
                if i[0] == 'HH':
                    i[0] = 'Z'
        elif nr_Z < (2*nr_HH):
            for i in square:
                if i[0] == 'Z':
                    i[0] = 'ZH'


def christmasFated(positions):
    """
    input:
    positions: Liste mit allen Positionen der Figuren
    
    output:
    "Zombies ate my Christmas!": nur noch Zombies "Z" oder "ZH" in positions gibt
    "Ho, ho, ho, and a merry Zombie-Christmas!": keine Zombies "Z" und mindestens einen Menschen "H" oder "HH" in positions gibt
    """
    positions_type = []
    for i in positions: # Typen auslesen
        positions_type.append(i[0])
    if "H" not in positions_type and "HH" not in positions_type:
        return True
    elif "Z" not in positions_type:
        return True
    else:
        return False


def mergeSquare(square, intermediate):
    """
    input:
    square: alle letzten Elemente mit dem gleichen Eintrag in der zweiten Position aus positions Liste
    intermediate: Zwischenspeicher-Liste
    
    output:
    intermediate: Endliste nachdem square an die gegebene Liste intermediate angefügt wurde 
    """
    for i in square:
        intermediate.append(i)
    return intermediate


def christmasFate(positions):
    """
    input:
    n: Anzahl der Reihen des Welt-Rechtecks,
    m: Anzahl der Spalten des Welt-Rechtecks,
    pos: Position der Figur als nichtnegative ganze Zahl,
    rnd: zufälliger Float im halboffenen Intervall [0, 1),
    
    output:
    
    """
    positions_type = []
    for i in positions:
        positions_type.append(i[0])
    if "H" not in positions_type and "HH" not in positions_type:
        return "Zombies ate my Christmas!"
    elif "Z" not in positions_type:
        return "Ho, ho, ho, and a merry Zombie-Christmas!"


def zombieChristmas(n,m,positions): # nochmal überarbeiten
    """
    input:
    n: Anzahl der Reihen des Welt-Rechtecks,
    m: Anzahl der Spalten des Welt-Rechtecks,
    positions: Liste mit allen Positionen der Figuren
    
    output:
    pos: aktualisierte Position der Figur als nichtnegative ganze Zahl
    """
    intermediate_list = []
    while not christmasFated(positions):
        updatePositions(n,m,positions) # Bewegung aller Figuren
        while len(positions) > 0:
            extracted_square = extractSquare(positions) # Feld mit allen Figuren
            giftExchange(extracted_square) # Gift Exchange mit allen Figuren des Feldes
            intermediate_list = mergeSquare(extracted_square, intermediate_list) # Anfügen an positions
        positions = intermediate_list
    print(christmasFate(intermediate_list))




"""""
print(updatePosition(1, 1, 0, 0.4870226888229471)) # gibt -1 zurück, soll aber 0 zurück geben 

positions = [['Z',0],['ZH',2],['H',3],['H',1],['H',1],['H',1],['Z',1],['Z',1]]
zombieChristmas(2, 2, positions)

positions = [['Z',0],['ZH',4],['H',10],['HH',14]]
print(updatePosition(3,5,0,0.3))
print(updatePosition(3,5,4,0.8))
print(updatePosition(3,5,7,0.8))
print(updatePosition(15,50,7,0.77))
print(updatePosition(15,50,0,0.3))
print(updatePosition(15,50,49,0.1))
print(updatePosition(15,50,700,0.6))


positions = [['Z', 184], ['Z', 161], ['Z', 160], ['Z', 160]]
sortPositions(positions)
print(positions)


positions = [['Z', 160], ['Z', 160], ['Z', 160], ['Z', 161], ['Z', 161], ['Z', 161], ['Z', 162], ['Z', 162], ['Z', 162]]
print(positions)
square = extractSquare(positions)
print(square)
print(positions)
square = extractSquare(positions)
print(square)
print(positions)
square = extractSquare(positions)
print(square)
print(positions)


square = [['Z', 160], ['H', 160], ['Z', 160], ['ZH', 160], ['H', 160], ['Z', 160], ['ZH', 160], ['H', 160], ['Z', 160], ['ZH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160], ['H', 160], ['Z', 160], ['ZH', 160]]
giftExchange(square)
print(square)
square = [['H', 160], ['H', 160], ['Z', 160], ['ZH', 160], ['H', 160], ['Z', 160], ['Z', 160], ['H', 160], ['Z', 160], ['Z', 160], ['HH', 160], ['Z', 160], ['ZH', 160]]
giftExchange(square)
print(square)
square = [['Z', 160], ['H', 160], ['Z', 160], ['ZH', 160]]
giftExchange(square)
print(square)
square = [['H', 160], ['H', 160], ['Z', 160], ['ZH', 160]]
giftExchange(square)
print(square)



print(christmasFated([['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]]))
print(christmasFated([['HH', 160], ['HH', 160], ['Z', 160], ['ZH', 160]]))
print(christmasFated([['HH', 160], ['HH', 160], ['H', 160], ['ZH', 160]]))


intermediate = [['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]]
mergeSquare([['Z', 159], ['Z', 159]], intermediate)
print(intermediate)


christmasFate([['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]])
christmasFate([['Z', 160], ['Z', 160], ['ZH', 160], ['ZH', 160]])

"""""

