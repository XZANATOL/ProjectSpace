import re

def reflection_counter(group:list[str]) -> dict:
	for idx in range(1, len(group)):
		first_half, second_half = group[:idx][::-1], group[idx:]
		first_half, second_half = first_half[:len(second_half)], second_half[:len(first_half)]
		if first_half == second_half:
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
	"""
	if perfect_row_count["count"] > perfect_col_count["count"]:
		return 100*(perfect_row_count["perfect_reflection"][0]+1)
	else:
		return perfect_col_count["perfect_reflection"][0]+1
	"""

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n\n")
	
	res:int = 0
	for group in puzzle_input:
		parse_res = mirror_parser(group)
		res += parse_res
	print(res)
