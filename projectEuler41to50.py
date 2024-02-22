from string import ascii_uppercase
from itertools import permutations
from typing import List

from eulerPrimes import get_primes_up_to


class ProjectEuler41to50:
	def problem42(self) -> int:
		# The nth term of the sequence of triangle numbers is given by,
		#     t_n = \frac12n(n+1)
		# so the first ten triangle numbers are:
		#     1, 3, 6, 10, 15, 21, 28, 36, 45, 55...
		# By converting each letter in a word to a number corresponding to its
		# alphabetical position and adding these values we form a word value.
		# For example, the word value for SKY is
		#     19 + 11 + 25 = 55 = t_{10}.
		# If the word value is a triangle number then we shall call the word a
		# triangle word. Using problem42.txt, a 16K text file containing nearly
		# two-thousand common English words, how many are triangle words?
		with open("data/problem42.txt") as file_data:
			data = file_data.read().replace('"', '')
			word_list = data.split(",")
		
		tri = 0
		triangular_nums = []
		for i in range(1, 10000):
			tri += i
			triangular_nums.append(tri)
		
		u = "0" + ascii_uppercase  # in order to 1-index
		char_sums = [sum([u.index(ch) for ch in w]) for w in word_list]
		return len([s for s in char_sums if s in triangular_nums])
	
	def _has_arith_seq(self, per: List[int]) -> List[int]:
		for i in range(0, len(per) - 2):
			if (per[i + 2] - per[i + 1]) == (per[i + 1] - per[i]):
				return [per[i], per[i + 1], per[i + 2]]
		return []

	def problem49(self) -> int:
		# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
		# increases by 3330, is unusual in two ways: (i) each of the three
		# terms are prime, and, (ii) each of the 4-digit numbers are
		# permutations of one another. There are no arithmetic sequences made
		# up of three 1-, 2-, or 3-digit primes, exhibiting this property, but
		# there is one other 4-digit increasing sequence. What 12-digit number
		# do you form by concatenating the three terms in this sequence?
		result = []
		four_dig_primes = [i for i in get_primes_up_to(10000) if i > 1000]
		
		for prime in four_dig_primes:
			pr_chars = [ch for ch in str(prime)]
			perms = [int(''.join(p)) for p in permutations(pr_chars,4)]
			prime_perms = {p for p in perms if p > prime and p in four_dig_primes}
			
			if not prime_perms:
				continue
			
			seq = self._has_arith_seq(sorted(list(prime_perms)))
			if not seq:
				continue
				
			result.append(seq)

		# Note, does not produce result in example, but works
		return int(''.join([str(r) for r in result[0]]))
		

if __name__ == "__main__":
	euler = ProjectEuler41to50()
	
	# print(euler.problem41())  # TODO unsolved
	# print(euler.problem42())  # solved
	# print(euler.problem43())  # TODO unsolved
	# print(euler.problem44())  # TODO unsolved
	# print(euler.problem45())  # TODO unsolved
	# print(euler.problem46())  # TODO unsolved
	# print(euler.problem47())  # TODO unsolved
	# print(euler.problem48())  # TODO unsolved
	# print(euler.problem49())  # solved
	# print(euler.problem50())  # TODO unsolved
