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

	discarded_inputs = [".","1","2","3","4","5","6","7","8","9","0"]
	matches = []
	s:int = 0
	for row, line in enumerate(puzzle_input):
		numbers = [[m.start(), m[0]] for m in re.finditer(r"\d+", line)]
		
		for number in numbers:
			# number[0] is column index start
			i = row
			j = number[0]
			
			for _ in str(number[1]):
				if (isValidPos(i - 1, j - 1, n, m)):
					matches.append(puzzle_input[i - 1][j - 1])
				if (isValidPos(i - 1, j, n, m)):
					matches.append(puzzle_input[i - 1][j])
				if (isValidPos(i - 1, j + 1, n, m)):
					matches.append(puzzle_input[i - 1][j + 1])
				if (isValidPos(i, j - 1, n, m)):
					matches.append(puzzle_input[i][j - 1])
				if (isValidPos(i, j + 1, n, m)):
					matches.append(puzzle_input[i][j + 1])
				if (isValidPos(i + 1, j - 1, n, m)):
					matches.append(puzzle_input[i + 1][j - 1])
				if (isValidPos(i + 1, j, n, m)):
					matches.append(puzzle_input[i + 1][j])
				if (isValidPos(i + 1, j + 1, n, m)):
					matches.append(puzzle_input[i + 1][j + 1])
				j+=1
			
			for match in matches:
				if match not in discarded_inputs:
					s+= int(number[1])
					break

			matches = []

	print(s)