def sieve(n):
    if n < 2:
        return None
    primes = [2]
    for i in range(3, n + 1, 2):
        primes.append(i)
    i = 2
    while i <= int(n ** (1 / 2)):
        if i in primes:
            for j in range(i * 2, n + 1, i):
                if j in primes:
                    primes.remove(j)
        i = i + 1
    return primes


def isprime(n):
    if n < 2:
        return None
    if n == 2 or n == 3 or n == 5:
        return True
    else:
        if (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
            return False
        else:
            return True


def factorization(n):
    factorization_list = []
    pkek_list = []
    primfactors = []
    if n < 2:
        return None
    # Primfaktorzerlegung
    counter = 2
    while counter * counter <= n:
        while (n % counter) == 0:
            primfactors.append(counter)
            n //= counter
        counter += 1
    if n > 1:
        primfactors.append(n)
    # pk und ek Berechnung
    while len(primfactors) > 0:
        i = 0
        pkek_list = [primfactors[i], primfactors.count(primfactors[i])]
        factorization_list.append(pkek_list)
        primfactors = list(filter(lambda a: a != primfactors[i], primfactors))
    if not pkek_list:
        pkek_list = [n, 1]
        factorization_list.append(pkek_list)
    return factorization_list


def divisornumber(n):
    if n == 1:
        return 1
    elif n < 1:
        return None
    factorization_list = factorization(n)
    teilerzahl = 1
    for list in factorization_list:
        teilerzahl = teilerzahl * (list[1] + 1)
    return teilerzahl


def iscoprime(n, m):
    if n == 1:
        return True
    elif n < 1 or m < 1:
        return None
    elif divisornumber(n * m) == divisornumber(n) * divisornumber(m):
        return True
    else:
        return False
