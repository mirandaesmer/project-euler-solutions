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


if __name__ == "__main__":
	euler = ProjectEuler31to40()
	
	print(euler.problem36())  # solved
