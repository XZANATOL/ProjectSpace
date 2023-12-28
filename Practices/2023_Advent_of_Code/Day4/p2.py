import itertools
import re

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")
	
	s:dict = {}
	res:int = 0
	for line in puzzle_input:
		game_num, data = line.split(": ")
		game_num = int(re.search(r"\d+", game_num)[0])
		obtained_nums, winning_nums = data.split(" | ")
		obtained_nums = [x for x in obtained_nums.split(" ") if x != ""]
		winning_nums = [x for x in winning_nums.split(" ") if x != ""]

		count:int = 0
		for obtained_num in obtained_nums:
			if obtained_num in winning_nums:
				count += 1

		s[game_num] = [1, count]

	for card_num in s.keys():
		iter_per_card = s[card_num][0]
		winning_count = s[card_num][1]
		for i in range(iter_per_card):
			temp = card_num
			for j in range(winning_count):
				temp+=1
				if s.get(temp):
					s[temp][0]+=1

	for card_num in s.keys():
		res += s[card_num][0]

	print(res)