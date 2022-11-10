prim_liste = []


def sieve(n):
    if (n < 2):
        return None
    not_prime_list = []
    prime_list = []
    for i in range(2, n+1):
        if i not in not_prime_list:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                not_prime_list.append(j)
    return prime_list


def isprime(n):
    if n > 2:
        for i in range(n):
            if (n % i) == 0:
                return False
            else:
                return True
    else:
        return None


def factorization(n):
    factorization_liste = []
    if (n < 2):
        return None
    not_prime_list = []
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                not_prime_list.append(j)
        for i in range(len(prime_list)):
            if prime_list[i] % n == 0:
                primfactor_liste = []
                ek = prim_liste[i] // n
                primfactor_liste.append(prim_liste[i], ek)
                factorization_liste.append(primfactor_liste)
    print(factorization_liste)


factorization(13)


def divisornumber(n):
    i = 1
    teiler_anzahl = 0
    while i <= n:
        if n % i == 0:
            teiler_anzahl += 1
            i = i + 1
        elif n == 1:
            return 1
        elif n < 1:
            return None
    return teiler_anzahl


def coprime(n, m):
    while m != 0:
        n, m = m, n % m
    return n


def iscoprime(n, m):
    if coprime(n, m) == 1:
        return True
    elif n < 1 or m < 1:
        return None
    else:
        return False
