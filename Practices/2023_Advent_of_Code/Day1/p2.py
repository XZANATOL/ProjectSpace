import re

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.readlines()

	converters = {
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9"
	}
	patterns = [
		r"one",
		r"two",
		r"three",
		r"four",
		r"five",
		r"six",
		r"seven",
		r"eight",
		r"nine",
		r"\d"
	]
	s: int = 0
	temp: list[str] = []
	temp_joined: str = ""
	empty_data = ('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')


	for line in puzzle_input:

		for pattern in patterns:
			# Learned a new method in re :p
			for m in re.finditer(pattern, line):
				temp.append([m.start(0), m[0]])

		temp = sorted(temp, key=lambda x: (x[0],x[1]))
		for r in [temp[0], temp[-1]]:
			try:
				r = int(r[1])
				temp_joined += str(r)
			except:
				r = converters[r[1]]
				temp_joined += r

		s += int(temp_joined)
		temp = []
		temp_joined = ""

	print(s)