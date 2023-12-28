import re
from math import ceil

def sol(times, distances):
	res:int = 1
	for t_max, d in zip(times, distances):
		t_max, d = int(t_max), int(d)
		r1 = (-t_max + (t_max**2 - 4*-1*-(d+0.1))**0.5) / (2*-1)
		r2 = (-t_max - (t_max**2 - 4*-1*-(d+0.1))**0.5) / (2*-1)

		res *= int(r2) - ceil(r1) + 1 # Margin Error
	return res


if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")
	
	# Serializing inputs
	times = re.split(r" +", puzzle_input[0])[1:]
	distances = re.split(r" +", puzzle_input[1])[1:]

	"""
	Physcis: d = V * t + 0.5 * a * t^2, a = 0
	then: d = V * t

	Story says, availabe time is the time after you left the button
	# t = t_max - t
	
	Substitute: d = t * (t_max - t)
	therefore, Equation: -t^2 + t*(t_max) - d = 0

	To solve the puzzle, we just need to substitute
	the highest record (d) with (d+0.1) the get the roots
	which are the available time span for breaking the record
	:p
	"""
	print("Part 1:", sol(times, distances))

	times = ["".join(times)]
	distances = ["".join(distances)]
	print("Part 2:", sol(times, distances))