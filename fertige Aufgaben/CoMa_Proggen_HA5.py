def get_eqclasses(n, E):
    L = [[] for i in range(n)]
    for e in E:
        L[e[0]].append(e[1])
    for i in range(n):
        L[i].insert(0, i)
    for i in range(n):
        L[i].sort()
    for i in range(n):
        for j in range(i + 1, n):
            if not set(L[i]).isdisjoint(L[j]) and L[i]!=L[j]:
                return []
    L.sort()  # L sortieren
    last_first_index = -1
    equivalence_classes = []
    for i in range(n):
        if L[i][0] != last_first_index:
            equivalence_classes.append(L[i])
            last_first_index = L[i][0]
    return equivalence_classes


def get_classes(n, E):
    L = [[]for i in range(n)]
    for e in E:
        L[e[0]].append(e[1]) # Liste L mit e füllen
    for i in range(n): # Liste V erstellen
        L[i].insert(0,i)
    return L


def are_equal(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


def are_disjoint(list1, list2):
    set_list1 = set(list1)
    set_list2 = set(list2)
    if set_list1.isdisjoint(set_list2):
        return True
    else:
        return False


print(get_classes(2,[(1, 0), (0, 1)])) # [[0, 1], [0, 1]]   gibt aber [[0, 1], [1, 0]] zurück
print(are_equal([0, 1],[0, 1])) # True
print(are_disjoint([0, 1],[0, 1])) # False
print(are_equal([0, 1],[1, 0])) # True
print(are_disjoint([0, 1],[1, 0])) # False
print(are_equal([1, 0],[0, 1])) # True
print(are_disjoint([1, 0],[0, 1])) # False
print(are_equal([1, 0],[1, 0])) # True
print(are_disjoint([1, 0],[1, 0])) # False
print(get_eqclasses(2,[(1, 0), (0, 1)])) # [[0, 1]]