from string import ascii_uppercase

from eulerPrimes import get_proper_divisors


class ProjectEuler21to30:
	def problem21(self) -> int:
		# Let d(n) be defined as the sum of proper divisors of n (numbers less
		# than n which divide evenly into n). If d(a) = b and d(b) = a, where
		# a != b, then a and b are an amicable pair and each of a and b are
		# called amicable numbers.For example, the proper divisors of 220 are
		#     1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
		# therefore d(220) = 284.
		#     The proper divisors of 284 are 1, 2, 4, 71 and 142;
		#     so d(284) = 220.
		# Evaluate the sum of all the amicable numbers under 10000.
		amicable_nums = set()
		
		for a in range(1, 10001):
			a_divs = get_proper_divisors(a)
			b = sum(a_divs)
			
			if a != b and sum(get_proper_divisors(b)) == a:
				amicable_nums.add(a)
				amicable_nums.add(b)
		return sum(amicable_nums)
	
	def _name_score(self, name: str, charset: str, pos: int) -> int:
		sum = 0
		for ch in name:
			sum += charset.index(ch)
		return (pos + 1) * sum  # 1-indexed
	
	def problem22(self) -> int:
		with open("data/problem22.txt") as file_data:
			data = file_data.read().replace('"', '')
		
		name_list = sorted(data.split(","))
		upr = '0' + ascii_uppercase
		scores = [self._name_score(n, upr, i) for i, n in enumerate(name_list)]
		return sum(scores)
	
	def problem29(self) -> int:
		# Consider all integer combinations of a^b for 2<=a<=5 and 2<=b<=5,
		# if they are then placed in numerical order, with any repeats removed,
		# we get the following sequence of 15 distinct terms:
		#     4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
		# How many distinct terms are in the sequence generated by a^b for
		# 2<=a<=100 and 2<=b<=100?
		upper_limit = 100
		solutions = set()
		
		for a in range(2, upper_limit + 1):
			for b in range(2, upper_limit + 1):
				solutions.add(a ** b)
		return len(solutions)

	def problem30(self) -> int:
		# Surprisingly there are only three numbers that can be written as the
		# sum of fourth powers of their digits:
		#     1634, 8208, 9474
		# The sum of these numbers is
		#     1634 + 8208 + 9474 = 19316
		# Find the sum of all the numbers that can be written as the sum of
		# fifth powers of their digits.
		_sum = 0
		for i in range(2, 1000000):
			if i == sum([int(ch) ** 5 for ch in str(i)]):
				_sum += i
		return _sum


if __name__ == "__main__":
	euler = ProjectEuler21to30()
	
	# print(euler.problem22())  # solved
	# print(euler.problem21())  # solved
	# print(euler.problem29())  # solved
	# print(euler.problem30())  # solved

