from collections import Counter

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")

	label_powers = "23456789TJQKA"
	hands_ordered = []
	for hand, bid in map(str.split, puzzle_input):
		hands_ordered.append(
			[
				max(Counter(hand).values()) - len(set(hand)), # to get hand type
				*map(label_powers.index, hand), # for second ordering rule
				bid, # for future reference
			]
		)

	print( sum( (idx+1) * int(bid[-1]) for idx, bid in enumerate(sorted(hands_ordered)) ) )

# Forgot to save the code for p2 :\