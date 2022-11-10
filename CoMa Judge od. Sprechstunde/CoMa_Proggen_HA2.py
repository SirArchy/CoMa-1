def convert_to_standard(a1, a2, b1, b2):
    # Umformen zur Standartform
    x1 = min(a1, b1)
    y1 = min(a2, b2)
    x2 = max(a1, b1)
    y2 = max(a2, b2)
    sorted_tuple = (x1, y1, x2, y2)
    return sorted_tuple


def intersects(h, a1, a2, b1, b2):
    # überschneiden sich die Rechtecke oder nicht

    if b1 < 0 or a1 > 6:
        return False
    elif b2 < 0 or a2 > h:
        return False
    else:
        return True


def get_delta_x1(a1, b1):
    # Seitenlänge aller x-Werte
    if max(a1, b1) >= 6:
        delta_x1 = abs(min(a1, b1) - max(0, 6))
    else:
        delta_x1 = abs(max(a1, b1) - min(0, 6))
    return delta_x1


def get_delta_x2(h, a2, b2):
    # Seitenlänge aller y-Werte
    if max(a2, b2) >= h:
        delta_x2 = abs(min(a2, b2) - max(0, h))
    else:
        delta_x2 = abs(max(a2, b2) - min(0, h))
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
        return f"Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt {L}."


print(get_lattice_point_number(5, -2, 5, 0, 9))
a = get_lattice_point_number(5, -2, 4, 1, 9)
print(a)
print(get_lattice_point_number(3, 0, 0, 0, 0))
print(get_lattice_point_number(0, 0, 0, 0, 0))
print(get_lattice_point_number(1, -2, 5, 0, 9))
