import re

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")
	
	s, res = [0]*2
	for line in puzzle_input:
		game_num, data = line.split(": ")
		obtained_nums, winning_nums = data.split(" | ")
		obtained_nums = [x for x in obtained_nums.split(" ") if x != ""]
		winning_nums = [x for x in winning_nums.split(" ") if x != ""]

		for obtained_num in obtained_nums:
			if obtained_num in winning_nums:
				if s == 0:
					s=1
				else:
					s*=2

		res += s
		s=0

	print(res)