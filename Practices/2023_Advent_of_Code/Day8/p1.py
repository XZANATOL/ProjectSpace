current_pos:str = "AAA"
counter:int = 0

def loop_instructions(intrusction) -> None:
	global current_pos, counter
	for intrusction in intrusctions:
		if current_pos == "ZZZ":
			return

		counter += 1
		if intrusction == "L":
			current_pos = game_map[current_pos][0]
		elif intrusction == "R":
			current_pos = game_map[current_pos][1]
		else:
			print(intrusction)

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")

	intrusctions = puzzle_input.pop(0)
	puzzle_input.pop(0) # get rid of the empty line

	game_map:dict = {}
	for idx, line in enumerate(puzzle_input):
		line = line.split(" = ")
		line[1] = line[1].replace("(", "").replace(")", "")
		game_map[line[0]] = [*line[1].split(", ")]

	while current_pos != "ZZZ":
		loop_instructions(intrusctions)
	
	print(counter)

