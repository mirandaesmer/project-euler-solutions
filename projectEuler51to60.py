class ProjectEuler51to60:
	def problem55(self) -> int:
		# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
		# Not all numbers produce palindromes so quickly. For example, 349 takes
		# three iterations to arrive at a palindrome. Although no one has proved
		# it yet, it is thought that some numbers, like 196, never produce a
		# palindrome. A number that never forms a palindrome through the reverse
		# and add process is called a Lychrel number. Due to the theoretical
		# nature of these numbers, and for the purpose of this problem, we shall
		# assume that a number is Lychrel until proven otherwise. In addition,
		# you are given that for every number below ten-thousand, it will either
		# (i) become a palindrome in less than fifty iterations, or, (ii) no
		# one, with all the computing power that exists, has managed so far to
		# map it to a palindrome. In fact, 10677 is the first number to be shown
		# to require over fifty iterations before producing a palindrome:
		#     4668731596684224866951378664 (53 iterations, 28-digits).
		# Surprisingly, there are palindromic numbers that are themselves
		# Lychrel numbers; the first example is 4994. How many Lychrel numbers
		# are there below ten-thousand?
		lychrel_count = 0
		for n in range(1, 10000):
			is_lychrel = True  # assume n is Lychrel until proven otherwise
			rev_sum = n
			
			for _ in range(0, 50):
				rev_sum = int(str(rev_sum)) + int(str(rev_sum)[::-1])
				if str(rev_sum) == str(rev_sum)[::-1]:
					is_lychrel = False
					break
			
			if is_lychrel:
				lychrel_count += 1
		return lychrel_count


if __name__ == "__main__":
	euler = ProjectEuler51to60()
	
	# print(euler.problem51())  # TODO unsolved
	# print(euler.problem52())  # solved
	# print(euler.problem53())  # TODO unsolved
	# print(euler.problem54())  # TODO unsolved
	# print(euler.problem55())  # solved
	# print(euler.problem56())  # TODO unsolved
	# print(euler.problem57())  # TODO unsolved
	# print(euler.problem58())  # TODO unsolved
	# print(euler.problem59())  # solved
	# print(euler.problem60())  # TODO unsolved
