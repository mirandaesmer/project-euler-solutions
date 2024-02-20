from typing import List


def is_prime(n, prev_primes) -> bool:
	if n % 10 not in [1, 3, 7, 9]:
		return False
	
	for p in prev_primes:
		if n % p == 0:
			return False
	return True


def gen_primes(upto) -> List[int]:
	primes = [2, 3, 5, 7]

	for i in range(11, upto + 1):
		if is_prime(i, primes):
			primes.append(i)
	return primes

def gen_ith_prime(i):
	primes = [2, 3, 5, 7]
	curr = 4
	num = 11
	
	while curr < i:
		if is_prime(num, primes):
			primes.append(num)
			curr += 1
		num += 1
	return primes[-1]


# Helper functions for prime related problems
if __name__ == "__main__":
	# print(gen_primes(50))  # DEBUG
	pass
