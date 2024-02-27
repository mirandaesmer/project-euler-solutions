class ProjectEuler91to100:
	
	def problem92(self) -> int:
		# A number chain is created by continuously adding the square of the 
		# digits in a number to form a new number until it has been seen before.
		# Any chain that arrives at 1 or 89 will become stuck in an endless
		# loop. What is most amazing is that EVERY starting number will
		# eventually arrive at 1 or 89. How many starting numbers below ten
		# million will arrive at 89?
		count = 0
		for num in range(2, 10000000):
			while True:
				if num == 1:
					break
				elif num == 89:
					count += 1
					break
				num = sum([int(ch) ** 2 for ch in list(str(num))])
		return count


if __name__ == "__main__":
	euler = ProjectEuler91to100()
	
	print(euler.problem92())
