def convert_to_standard(a1, a2, b1, b2):
    # Umformen zur Standartform
    x1 = min(a1, b1)
    y1 = min(a2, b2)
    x2 = max(a1, b1)
    y2 = max(a2, b2)
    sorted_tuple = (x1, y1, x2, y2)
    return sorted_tuple


def intersects(h, a1, a2, b1, b2):
    # ueberschneiden sich die Rechtecke oder nicht
    
    if b1 < 0 or a1 > 6:
        return False
    elif b2 < 0 or a2 > h:
        return False
    else:
        return True


def get_delta_x1(a1, b1):
    # Seitenlaenge aller x-Werte
    if b1 >= 6 and a1 <= 0:
        delta_x1 = 6
    elif b1 <= 6 and a1 >= 0:
        delta_x1 = b1 - a1 
    elif b1 >= 6:
        delta_x1 = abs(a1 - 6)
    else:
        delta_x1 = abs(b1 - 0)
    return delta_x1


def get_delta_x2(h, a2, b2): #hier ist der Fehler
    # Seitenlaenge aller y-Werte  
    if b2 >= h and a2 <= 0:
        delta_x2 = h - 0
    elif b2 <= h and a2 >= 0:
        delta_x2 = b2 - a2 
    elif b2 >= h:
        delta_x2 = abs(a2 - h)
    else:
        delta_x2 = abs(b2 - 0)
    return delta_x2


def get_lattice_point_number(h, a1, a2, b1, b2):
    sorted_tuple = convert_to_standard(a1, a2, b1, b2)
    if h < 0:
        return "Die Eingabe ist fehlerhaft."
    elif not intersects(h, sorted_tuple[0], sorted_tuple[1], sorted_tuple[2], sorted_tuple[3]):
        return "Der Schnitt der gegebenen Rechtecke ist leer."
    elif intersects(h, sorted_tuple[0], sorted_tuple[1], sorted_tuple[2], sorted_tuple[3]):
        delta_x1 = get_delta_x1(sorted_tuple[0], sorted_tuple[2])
        delta_x2 = get_delta_x2(h, sorted_tuple[1], sorted_tuple[3])
        L = (delta_x1 + 1) * (delta_x2 + 1) 
        return "Die Anzahl der Gitterpunkte im Rechteck betraegt " + str(L) + "."


print(get_lattice_point_number(3,-11,5,1,-2)) # Die Anzahl der Gitterpunkte im Rechteck betraegt 8.
print(convert_to_standard(-11,5,1,-2)) # (-11, -2, 1, 5)
print(intersects(3,-11,-2,1,5)) # True
print(get_delta_x1(-11,1)) # 1
print(get_delta_x2(3,-2,5)) # 3