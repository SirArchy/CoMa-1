def sieve(n):
	"""
	Führt das Sieb des Eratosthenes aus.
	Input: Ein integer n, mindestens 2
	Output: Eine Liste aller Primzahlen kleiner gleich n
	"""
	if n < 2:
		return None
	numbers = [None, None] + list(range(2, n+1))
	for i in range(2, n+1):
		if numbers[i] is not None:
			for k in range(2*i, n+1, i):
				numbers[k] = None
	primes = [num for num in numbers if num is not None]
	return primes
	
def isprime(n):
	"""
	Überprüft, ob eine Zahl prim ist.
	Input: Ein integer n, mindestens 2
	Output: True, falls n prim ist, ansonsten False
	"""
	if n < 2:
		return None
	k = 2
	while k ** 2 <= n:
		if n % k == 0:
			return False
		k += 1
	return True
	
def factorization(n):
	"""
	Errechnet die Primfaktorzerlegung einer Zahl.
	Input: Ein integer n, mindestens 2
	Output: Eine Liste der Form [[p1, v1], [p2, v2], ...] mit n = p1**v1 * p2**v2 * ...
	"""
	if n < 2:
		return None
	factors = dict()
	primes = sieve(n)
	for prime in primes:
		if n % prime == 0:
			factors[prime] = 0
			while n % prime == 0:
				factors[prime] += 1
				n //= prime
	return [list(t) for t in factors.items()]
	
def divisornumber(n):
	"""
	Errechnet die Anzahl der Teiler einer Zahl mithilfe der Primfaktorzerlegung.
	Input: Ein integer n, mindestens 1
	Output: Die Anzahl von Teilern der Zahl als integer
	"""
	if n < 1:
		return None
	if n == 1:
		return 1
	facs = factorization(n)
	num = 1
	for _, v in facs:
		num *= v + 1
	return num
	
def iscoprime(n, m):
	"""
	Überprüft anhand der Teileranzahl, ob n und m teilerfremd sind.
	Input: Zwei integer n und m, jeweils mindestens 1
	Output: True, falls n und m teilerfremd sind, sonst False
	"""
	if n < 1 or m < 1:
		return None
	num1 = divisornumber(n)
	num2 = divisornumber(m)
	num3 = divisornumber(n * m)
	return num1 * num2 == num3
	
	
		
