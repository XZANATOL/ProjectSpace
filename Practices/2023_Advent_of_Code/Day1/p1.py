import re

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.readlines()

	s: int = 0
	temp: list[str] = []
	for line in puzzle_input:
		temp.append(re.search(r"\d", line)[0])
		temp.append(re.search(r"\d", line[::-1])[0])
		s += int("".join(temp))
		temp = []

	print(s)