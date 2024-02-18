from functools import reduce


class ProjectEuler31to40:
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
	
	print(euler.problem36())  # solved
	print(euler.problem39())  # solved
	print(euler.problem40())  # solved
