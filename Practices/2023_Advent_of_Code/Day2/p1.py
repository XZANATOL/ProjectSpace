import re

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.readlines()

	#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
	s:int = 0
	colors = [r"\d red", r"\d green", r"\d blue"]

	for line in puzzle_input:

		game_id = re.search(r"\d+", line)[0]

		reds = [ int(m) for m in re.findall(r"(\d+) red", line) ]
		greens = [ int(m) for m in re.findall(r"(\d+) green", line) ]
		blues = [ int(m) for m in re.findall(r"(\d+) blue", line) ]

		reds, greens, blues = [max(reds), max(greens), max(blues)]

		if all([
				reds <= 12,
				greens <= 13,
				blues <= 14,
			]):
			s += int(game_id)

	print(s)