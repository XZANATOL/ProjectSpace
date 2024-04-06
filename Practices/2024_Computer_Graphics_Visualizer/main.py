import matplotlib.pyplot as plt
import json

import line_algos as line_algorithms
import round_algos as round_algorithms
import ellipse_algos as ellipse_algorithms

def choose_line_algo(algo: int) -> list[list[int]]:
	start_point: list[int] = list(map(int, input("Starting Point | x y > ").split()))
	end_point: list[int] = list(map(int, input("Ending Point | x y > ").split()))
	start_point, end_point = sorted([start_point, end_point])

	x_dimension = abs(max([start_point[0], end_point[0]]) * 2)
	y_dimension = abs(max([start_point[1], end_point[1]]) * 2)
	grid_map = [[0 for _ in range(x_dimension)] for _ in range(y_dimension)]

	return line_algorithms.algos[algo](start_point, end_point, grid_map)


def choose_round_algo(algo: int) -> list[list[int]]:
	center_point: list[int] = list(map(int, input("Center Point | x y > ").split()))
	radius: int = int(input("Radius > "))
	round_algorithms.algo_to_run = round_algorithms.algos[algo]

	grid_map = [[0 for _ in range(radius*2)] for _ in range(radius*2)]
	return round_algorithms.Drawwer(center_point, radius, grid_map)


def choose_ellipse_algo(algo: int) -> list[list[int]]:
	center_point: list[int] = list(map(int, input("Center Point | x y > ").split()))
	radius_point: list[int] = list(map(int, input("Center Point | x y > ").split()))

	grid_map = [[0 for _ in range(radius_point[1]*2)] for _ in range(radius_point[0]*2)]
	return ellipse_algorithms.EllipseMidPointAlgorithm(center_point, radius_point, grid_map)



if __name__ == "__main__":
	algos = [
		line_algorithms.algos_names,
		round_algorithms.algos_names,
		ellipse_algorithms.algos_names
	]
	choices_to_print = dict(enumerate([algo for name in algos for algo in name], 1))
	choices = {
		"1": [choose_line_algo, 1],
		"2": [choose_line_algo, 2],
		"3": [choose_line_algo, 3],
		"4": [choose_round_algo, 1],
		"5": [choose_round_algo, 2],
		"6": [choose_ellipse_algo, None]
	}
	print(json.dumps(choices_to_print, indent=3))
	choice = input("Choose shape > ")

	FinalGrid: list[list[int]] | None = choices[choice][0](*choices[choice][1:])

	if FinalGrid is not None:
		graph, plots = plt.subplots()
		plots.imshow(FinalGrid)
		plt.gca().invert_yaxis()
		plots.grid()
		plt.show()