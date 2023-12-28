import re

def isValidPos(i, j, n, m) -> bool:
	if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
		return False
	return True

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")
	
	n = len(puzzle_input)
	m = len(puzzle_input[0])

	s:int = 0
	for row, line in enumerate(puzzle_input):
		stars_idx = [m.start() for m in re.finditer(r"\*", line)]

		for star in stars_idx:
			i = row
			j = star
			matches = []

			# filter upper
			if isValidPos(i-1, j, n, m):
				numbers = [[x.start(), x.end(), x[0]] for x in re.finditer(r"\d+", puzzle_input[i-1])]
				for number in numbers:
					test = (number[0] <= star <= number[1]) or (star+1 == number[0]) or (star+1 == number[1]-1) or (star-1 == number[0]) or (star-1 == number[1]-1)
					if test:
						matches.append(number[2])

			# filter same row
			if isValidPos(i, j, n, m):
				numbers = [[x.start(), x.end(), x[0]] for x in re.finditer(r"\d+", puzzle_input[i])]
				for number in numbers:
					test = (number[0] <= star <= number[1]) or (star+1 == number[0]) or (star+1 == number[1]-1) or (star-1 == number[0]) or (star-1 == number[1]-1)
					if test:
						matches.append(number[2])

			# filter lower
			if isValidPos(i+1, j, n, m):
				numbers = [[x.start(), x.end(), x[0]] for x in re.finditer(r"\d+", puzzle_input[i+1])]
				for number in numbers:
					test = (number[0] <= star <= number[1]) or (star+1 == number[0]) or (star+1 == number[1]-1) or (star-1 == number[0]) or (star-1 == number[1]-1)
					if test:
						matches.append(number[2])
			
			if len(matches) == 2:
				s += int(matches[0])*int(matches[1])

	print(s)