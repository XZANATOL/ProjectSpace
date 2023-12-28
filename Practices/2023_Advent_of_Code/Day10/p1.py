start_coords:list = []
current_coords: list = []
comming_from:str = None

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")

	for row, l in enumerate(puzzle_input):
		if "S" in l:
			start_coords = [row, l.index("S")]
			current_coords = [row, l.index("S")]
			break

	if puzzle_input[start_coords[0]-1][start_coords[1]] in ["7", "F", "|"]:
		current_coords[0] = start_coords[0]-1
		comming_from = "s"
	elif puzzle_input[start_coords[0]+1][start_coords[1]] in ["J", "L", "|"]:
		current_coords[0] = start_coords[0]+1
		comming_from = "n"
	elif puzzle_input[start_coords[0]][start_coords[1]+1] in ["7", "F", "-"]:
		current_coords[1] = start_coords[1]+1
		comming_from = "w"
	else:
		current_coords[1] = start_coords[1]-1
		comming_from = "e"

	step_counter = 1
	pos = puzzle_input[current_coords[0]][current_coords[1]]
	while pos not in [".", "S"]:
		if pos == "|":
			if comming_from == "s":
				current_coords[0] -= 1
			else:
				current_coords[0] += 1
				comming_from = "n"

		elif pos == "-":
			if comming_from == "w":
				current_coords[1] += 1
			else:
				current_coords[1] -= 1
				comming_from = "e"

		elif pos == "L":
			if comming_from == "n":
				current_coords[1] += 1
				comming_from = "w"
			else:
				current_coords[0] -= 1
				comming_from = "s"

		elif pos == "J":
			if comming_from == "n":
				current_coords[1] -= 1
				comming_from = "e"
			else:
				current_coords[0] -= 1
				comming_from = "s"

		elif pos == "7":
			if comming_from == "w":
				current_coords[0] += 1
				comming_from = "n"
			else:
				current_coords[1] -= 1
				comming_from = "e"

		elif pos == "F":
			if comming_from == "s":
				current_coords[1] += 1
				comming_from = "w"
			else:
				current_coords[0] += 1
				comming_from = "n"

		elif pos == ".":
			print("algorithm error")

		pos = puzzle_input[current_coords[0]][current_coords[1]]
		step_counter+=1

print(step_counter/2)
# Again lost the code for p2