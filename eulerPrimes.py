from math import ceil, sqrt
from typing import List, Set


def is_prime(n: int, prev_primes: List[int]) -> bool:
	if n % 10 not in [1, 3, 7, 9]:
		return False
	
	for p in prev_primes:
		if n % p == 0:
			return False
	return True


def get_primes_up_to(limit: int) -> List[int]:
	primes = [2, 3, 5, 7]

	for i in range(11, limit + 1):
		if is_prime(i, primes):
			primes.append(i)
	return primes


def get_ith_prime(i: int) -> int:
	primes = [2, 3, 5, 7]
	curr = 4
	num = 11
	
	while curr < i:
		if is_prime(num, primes):
			primes.append(num)
			curr += 1
		num += 1
	return primes[-1]


def get_divisor_count(n: int) -> int:
	if n == 1:
		return 1
	
	root = sqrt(n)
	divs = 2  # 1 and itself
	
	if root - int(root) == 0.0:  # perfect squares
		divs += 1
	
	for i in range(2, ceil(root)):
		if n % i == 0:
			divs += 2
	return divs


def get_proper_divisors(n: int) -> Set[int]:
	root = sqrt(n)
	divisors = {1}
	for i in range(2, ceil(root)):
		if n % i == 0:
			divisors.add(i)
			divisors.add(int(n / i))
	return divisors


# NOTE: Helper functions for prime related problems
if __name__ == "__main__":
	pass
