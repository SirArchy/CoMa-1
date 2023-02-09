def is_circuit(bases, candidate):
    bases = convert_to_normal_matroid(bases)
    candidate = convert_to_normal_matroid(candidate)
    def is_independent(candidate, bases):
        for basis in bases:
            if all(elem in basis for elem in candidate):
                return False
        return True

    def is_minimal(candidate, bases):
        for i, elem in enumerate(candidate):
            new_candidate = [elem for elem in candidate if elem != candidate[i]]
            if is_independent(new_candidate, bases):
                return False
        return True

    return is_independent(candidate, bases) and is_minimal(candidate, bases)



def convert_to_normal_matroid(bin_matroid):
    normal_matroid = []
    temps = []
    if any(isinstance(i, list) for i in bin_matroid):
        for i in range(len(bin_matroid)):
            for j in range(len(bin_matroid[0])):
                if bin_matroid[i][j] == 1:
                     temps.append(j+1)
            normal_matroid.append(temps)
            temps = [] 
    else:
        for i in range(len(bin_matroid)):
            if bin_matroid[i] == 1:
                     normal_matroid.append(i+1)
    return normal_matroid