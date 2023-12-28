maps:dict = {
	"seed_to_soil": [],
	"soil_to_fertilizer": [],
	"fertilizer_to_water": [],
	"water_to_light": [],
	"light_to_temperature": [],
	"temperature_to_humidity": [],
	"humidity_to_location": []
}
keys:list = list(maps.keys())


def map_converter(src: str, dst: str, num: int) -> int:
	global maps
	key = f"{src}_to_{dst}"
	for map_rng in maps[key]:
		if num in range(int(map_rng[1]), int(map_rng[1])+int(map_rng[2])):
			return int(map_rng[0]) + (num - int(map_rng[1]))
	return num

if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")
	
	# Serializing inputs
	seeds = puzzle_input.pop(0).split(": ")[1].split(" ")
	puzzle_input.pop(0)
	puzzle_input.pop(0)

	

	while len(puzzle_input) != 0:
		map_line = puzzle_input.pop(0).split(" ")
		maps[keys[0]].append(map_line)

		if len(puzzle_input) == 0:
			break
		if puzzle_input[0] == "":
			puzzle_input.pop(0)
			puzzle_input.pop(0)
			keys.pop(0)
	# ======================================

	# Let the conversion commnece!
	min_loc = None
	for seed in seeds:
		seed_to_soil = map_converter("seed", "soil", int(seed))
		soil_to_fertilizer = map_converter("soil", "fertilizer", seed_to_soil)
		fertilizer_to_water = map_converter("fertilizer", "water", soil_to_fertilizer)
		water_to_light = map_converter("water", "light", fertilizer_to_water)
		light_to_temperature = map_converter("light", "temperature", water_to_light)
		temperature_to_humidity = map_converter("temperature", "humidity", light_to_temperature)
		humidity_to_location = map_converter("humidity", "location", temperature_to_humidity)

		if min_loc is None:
			min_loc = humidity_to_location
		else:
			if humidity_to_location < min_loc:
				min_loc = humidity_to_location

	print(min_loc)