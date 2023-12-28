import re

def reflection_counter(group:list[str]) -> dict:
	for idx in range(1, len(group)):
		first_half, second_half = group[:idx][::-1], group[idx:]

		mismatches:int = 0
		for row_top, row_bot in zip(first_half, second_half):
			for char_first, char_last in zip(row_top, row_bot):
				if char_first != char_last:
					mismatches += 1
				if mismatches > 1:
					break
		if mismatches == 1:
			return idx
	return 0
		

def mirror_parser(group:str) -> int:
	group = group.split("\n")

	perfect_row_count = reflection_counter(group)	

	# Transpose the grid
	transposed:list = ["".join(i) for i in list(zip(*group))]
	perfect_col_count = reflection_counter(transposed)

	print(perfect_row_count)
	print(perfect_col_count)
	print("========================")
	
	return 100*(perfect_row_count) + (perfect_col_count)

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n\n")
	
	res:int = 0
	for group in puzzle_input:
		parse_res = mirror_parser(group)
		res += parse_res
	print(res)
