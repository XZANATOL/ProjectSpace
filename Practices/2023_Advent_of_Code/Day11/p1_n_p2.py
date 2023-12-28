import re

clear_rows:list = []
clear_columns:list = []
hashtages_coords:list = []

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")
	clear_columns = list(range(0, len(puzzle_input[0])))

	for idx, line in enumerate(puzzle_input):
		hashtages = re.finditer(r"#", line)
		if not line.count("#"):
			clear_rows.append(idx)
		else:
			for hashtage in hashtages:
				hashtages_coords.append([idx, hashtage.start()])
				if hashtage.start() in clear_columns:
					clear_columns.remove(hashtage.start())

	res:int = 0
	c_multi:int = 0
	for idx, start_galaxy in enumerate(hashtages_coords):
		for idx_other, other_galaxy in enumerate(hashtages_coords[idx:]):

			distance = abs(other_galaxy[1] - start_galaxy[1])
			distance += abs(other_galaxy[0] - start_galaxy[0])
			
			coord_max_row = max([other_galaxy[0],start_galaxy[0]])
			coord_min_row = min([other_galaxy[0],start_galaxy[0]])
			for clear_row in clear_rows:
				if clear_row in range(coord_min_row, coord_max_row+1) and clear_row != start_galaxy[0]:
					c_multi += 1

			coord_max_col = max([other_galaxy[1],start_galaxy[1]])
			coord_min_col = min([other_galaxy[1],start_galaxy[1]])
			for clear_col in clear_columns:
				if clear_col in range(coord_min_col, coord_max_col+1) and clear_col != start_galaxy[1]:
					c_multi += 1
			
			res += distance
			#print("Galaxy ", idx+1, idx_other+idx+1, ":", distance)

print("p1:", res + c_multi*1)
print("p2:", res + c_multi*(1_000_000-1))