def sieve(n): #SCHAUEN OB BESSERE IMPLEMENTIERUNG GIBT
    if n < 2:
        return None
    else:
        primes = list()
        for num in range(2, n+1):
            if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
                primes.append(num)
        return primes

"""
def isprime(n): #SCHAUEN OB BESSERE IMPLEMENTIERUNG GIBT
    if n == 2:
        return True
    elif n > 1:
        for i in range(2, int(n//2)):
            if (n % i) == 0:
                return False
                break
            else:
                return True
    else: 
        return None
"""

def isprime(n) :
    if (n <= 1) :
        return None
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True


def factorization(n): #VIELLEICHT ZU LANGSAM
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

