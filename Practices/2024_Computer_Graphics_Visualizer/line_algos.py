def DigitalDifferentialAnalyzer(start_point: list[int], end_point: list[int], grid_map: list[list[int]]) -> list[list[int]]:
	dx = end_point[0] - start_point[0]
	dy = end_point[1] - start_point[1]
	steps = max(dx, dy)
	xinc = dx/steps
	yinc = dy/steps

	current_point = start_point
	grid_map[current_point[1]][current_point[0]] = 1
	print(current_point)

	for _ in range(steps):
		current_point[0] += xinc
		current_point[1] += yinc

		normalized_point = [round(round(current_point[0],1)+0.1), round(round(current_point[1],1)+0.1)] 
		grid_map[normalized_point[1]][normalized_point[0]] = 1
		print(normalized_point)

	return grid_map


def BresenhamAlgorithm(start_point: list[int], end_point: list[int], grid_map: list[list[int]]) -> list[list[int]]:
	current_point = start_point
	grid_map[current_point[1]][current_point[0]] = 1
	print(current_point)
	delta_x = end_point[0] - start_point[0]
	delta_y = end_point[1] - start_point[1]
	p_k = 2*delta_y - delta_x

	for _ in range(delta_x):
		if p_k < 0:
			p_k = p_k + 2*delta_y
			current_point[0] += 1
		else:
			p_k = p_k + 2*delta_y - 2*delta_x
			current_point[0] += 1
			current_point[1] += 1

		print(current_point)
		grid_map[current_point[1]][current_point[0]] = 1

	return grid_map


def MidPointAlgorithm(start_point: list[int], end_point: list[int], grid_map: list[list[int]]) -> list[list[int]]:
	return BresenhamAlgorithm(start_point, end_point, grid_map)


algos = {
	1: DigitalDifferentialAnalyzer,
	2: BresenhamAlgorithm,
	3: MidPointAlgorithm
}
algos_names = ["Line > DigitalDifferentialAnalyzer", "Line > BresenhamAlgorithm", "Line > MidPointAlgorithm"]