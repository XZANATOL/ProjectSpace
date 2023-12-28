import re

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.readlines()

	s:int = 0
	for line in puzzle_input:

		game_id = re.search(r"\d+", line)[0]

		reds = [ int(m) for m in re.findall(r"(\d+) red", line) ]
		greens = [ int(m) for m in re.findall(r"(\d+) green", line) ]
		blues = [ int(m) for m in re.findall(r"(\d+) blue", line) ]

		reds, greens, blues = [max(reds), max(greens), max(blues)]

		s += (reds*greens*blues)

	print(s)