from math import factorial


class ProjectEuler41to50:
	def _factorial_digit_sum(self, num: int) -> int:
		# if str() is too slow use (n // (10 ** i)) % 10
		return sum([factorial(int(ch)) for ch in str(num)])
	
	def problem74(self) -> int:
		# The number 145 is well known for the property that the sum of the
		# factorial of its digits is equal to 145:
		#     1! + 4! + 5! = 1 + 24 + 120 = 145
		# Perhaps less well known is 169, in that it produces the longest chain
		# of numbers that link back to 169; it turns out that there are only
		# three such loops that exist:
		#     169 - 363601 - 1454 - 169
		#     871 - 45361 - 871
		#     872 - 45362 - 872
		# It is not difficult to prove that EVERY starting number will
		# eventually get stuck in a loop. For example,
		#     69 - 363600 - 1454 - 169 - 363601 (- 1454)
		#     78 - 45360 - 871 - 45361 (- 871)
		#     540 - 145 (- 145)
		# Starting with 69 produces a chain of five non-repeating terms, but
		# the longest non-repeating chain with a starting number below one
		# million is sixty terms. How many chains, with a starting number below
		# one million, contain exactly sixty non-repeating terms?
		sixty_chain_count = 0
		
		for ini in range(2, 1000000):
			chain_nums = set()
			num = ini
			
			for chain_len in range(1, 62):
				chain_nums.add(num)
				num = self._factorial_digit_sum(num)
				
				if num in chain_nums:
					if chain_len == 60:
						sixty_chain_count += 1
					break
		return sixty_chain_count


if __name__ == "__main__":
	euler = ProjectEuler41to50()

	# print(euler.problem71())  # TODO unsolved
	# print(euler.problem72())  # TODO unsolved
	# print(euler.problem73())  # TODO unsolved
	# print(euler.problem74())  # solved
