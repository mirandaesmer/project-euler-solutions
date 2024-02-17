class ProjectEuler21to30:
	def problem29(self) -> int:
		# TODO missing description
		upper_limit = 100
		solutions = set()
		
		for a in range(2, upper_limit + 1):
			for b in range(2, upper_limit + 1):
				solutions.add(a ** b)
		return len(solutions)


if __name__ == "__main__":
	euler = ProjectEuler21to30()
	
	print(euler.problem29())  # solved
