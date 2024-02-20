from functools import reduce
from typing import Set

from eulerPrimes import is_prime


class ProjectEuler31to40:
	def _get_all_digit_rotations(self, num: int) -> Set[int]:
		digits = len(str(num))
		if digits == 1:
			return {num}
		
		concat_nums = str(num) + str(num)
		return {int(concat_nums[0 + i: digits+i]) for i in range(1, digits)}
		
	def problem35(self) -> int:
		# The number, 197, is called a circular prime because all rotations of
		# the digits: 197, 971, and 719, are themselves prime. There are
		# thirteen such primes below 100:
		#     2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
		# How many circular primes are there below one million?
		all_primes = [2, 3, 5, 7]
		cir_candidates = [2, 3, 5, 7]
		limit = 1000000
		
		for i in range(11, limit + 1):
			if is_prime(i, all_primes):
				all_primes.append(i)
			
				# rotated primes do not contain 0, 2, 4, 5, 6, 8 at all
				s = str(i)
				if s.count('0') or s.count('2') or s.count('4') or s.count('5') or s.count('6') or s.count('8'):
					continue
				else:
					cir_candidates.append(i)
				
		rotations_map = {p: self._get_all_digit_rotations(p) for p in cir_candidates}
		sol_count = 0
		
		for k, rotations in rotations_map.items():
			prime_rots = [r in all_primes for r in rotations]
			if all(prime_rots):
				sol_count += 1
		return sol_count
	
	def problem36(self) -> int:
		# The decimal number, 585 = 1001001001 (binary), is palindromic in both
		# bases. Find the sum of all numbers, less than one million, which are
		# palindromic in base 10 and base 2. Please note that the palindromic
		# number, in either base, may not include leading zeros.
		palin_sum = 0
		for i in range(0, 1000000):
			i_rev = int(str(i)[::-1])
			j = bin(i)[2:]
			j_rev = bin(i)[:1:-1]
			
			if i == i_rev and j == j_rev:
				palin_sum += i
		return palin_sum

	def problem39(self) -> int:
		# If p is the perimeter of a right angle triangle with integral length
		# sides, {a, b, c}, there are exactly three solutions for p = 120.
		#     {20,48,52}, {24,45,51}, {30,40,50}
		# For which value of p <= 1000, is the number of solutions maximised?
		perim_triples = [0] * 1001
		
		# limit search space as much as possible
		for p in range(12, 1001):
			for a in range(1, p // 3):
				max_b = (p - a) // 2 if p - a % 2 == 0 else ((p - a) // 2) + 1
				for b in range(a + 1, max_b):
					c = p - a - b
					if c != a and c != b and ((a ** 2) + (b ** 2) == c ** 2):
						perim_triples[p] += 1
		
		return perim_triples.index(max(perim_triples))
	
	def problem40(self) -> int:
		# An irrational decimal fraction is created by concatenating the
		# positive integers:
		#     0.123456789101112131415161718192021
		# It can be seen that the 12 digit of the fractional part is 1. If d[n]
		# represents the n digit of the fractional part, find the value of the
		# following expression:
		#     d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
		full_str = ''.join([str(i) for i in range(0, 1000000)])
		digits = [int(full_str[10 ** i]) for i in range(0, 7)]
		return reduce(lambda x, y: x * y, digits)


if __name__ == "__main__":
	euler = ProjectEuler31to40()
	
	# print(euler.problem35())  # solved
	# print(euler.problem36())  # solved
	# print(euler.problem39())  # solved
	# print(euler.problem40())  # solved
