reading_differences:list = []

def recursive_difference(numbers) -> None:
	global reading_differences

	if len(set(numbers)) == 1 and numbers[0] == 0:
		reading_differences[0].append(numbers[0])
		return None

	numbers:list = numbers[::-1]
	differences:list = []

	for idx, number in enumerate(numbers):
		if idx+1 == len(numbers):
			break
		differences.insert(0, number-numbers[idx+1])
	
	reading_differences.insert(0, differences)
	return recursive_difference(differences)


def extrapolate_p1() -> int:
	predictor = reading_differences[0][-1]
	predicted = 0
	for idx in range(len(reading_differences)):
		if idx+1 == len(reading_differences):
			return predicted

		predicted = reading_differences[idx+1][-1] + predicted

def extrapolate_p2() -> int:
	predictor = reading_differences[0][0]
	predicted = 0
	for idx in range(len(reading_differences)):
		if idx+1 == len(reading_differences):
			return predicted

		predicted = reading_differences[idx+1][0] - predicted


if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")

	s_p1, s_p2 = 0, 0
	for reading in puzzle_input:
		reading_list = list(map(int, reading.split(" ")))
		reading_differences.append(reading_list)
		recursive_difference(reading_list)

		s_p1 += extrapolate_p1()
		s_p2 += extrapolate_p2()
		reading_differences = []
	print(s_p1, s_p2)
