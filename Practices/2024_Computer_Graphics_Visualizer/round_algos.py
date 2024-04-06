import matplotlib.pyplot as plt
import copy

def get_plot():
	graph, plot = plt.subplots()
	plot.grid()
	return plot

def BresenhamAlgorithm(p_k, x0, y0) -> tuple[int]:
	if p_k < 0:
		x0 += 1
		p_k = p_k + 4*x0 + 6
	else:
		x0 += 1
		y0 -= 1
		p_k = p_k + 4*(x0-y0) + 10

	return p_k, x0, y0


def MidPointAlgorithm(p_k, x0, y0) -> tuple[int]:
	if p_k < 0:
		x0 += 1
		p_k = p_k + 2*x0 + 1
	else:
		x0 += 1
		y0 -= 1
		p_k = p_k + 2*(x0-y0) + 1

	return p_k, x0, y0


def Drawwer(center_point: list[int], radius: list[int], grid_map: list[list[int]]) -> None:
	plot = get_plot()
	plt.xlim(-len(grid_map), len(grid_map))
	plt.ylim(-len(grid_map[0]), len(grid_map[0]))

	x0 = 0
	y0 = radius

	if algo_to_run == BresenhamAlgorithm:
		p_k = 3-2*radius
	elif algo_to_run == CircleMidPointAlgorithm:
		p_k = 1 - radius

	x_plot = 0
	y_plot = 0
	quad = [(x0, y0)]

	# 1st Quad
	print("1st Quadrant")
	print((x0, y0))
	grid_map_quad1 = copy.deepcopy(grid_map)
	grid_map_quad1[y0][x0] = 1
	grid_map_quad1[x0][y0] = 1
	while x_plot <= y_plot:
		p_k, x0, y0 = algo_to_run(p_k, x0, y0)

		x_plot = x0 + center_point[0]
		y_plot = y0 + center_point[1]
		if x_plot <= y_plot:
			quad.append((x0, y0))
			print((x_plot, y_plot))
			grid_map_quad1[y_plot][x_plot] = 1
			grid_map_quad1[x_plot][y_plot] = 1

	quad += [(item[1], item[0]) for item in quad[::-1]]
	plot.imshow(grid_map_quad1)


	# 2nd quad
	print("2nd Quadrant")
	grid_map_quad2 = copy.deepcopy(grid_map)
	for x, y in quad[1:]:
		x = -x+center_point[0]
		y = y+center_point[1]
		print((x, y))
		grid_map_quad2[y][x] = 1

	x_offset = -radius*2
	y_offset = -0.5
	data_extent = (x_offset, x_offset + len(grid_map), y_offset, y_offset + len(grid_map[0]))
	plot.imshow(grid_map_quad2, extent=data_extent, origin="lower")


	# 3rd quad
	print("3rd Quadrant")
	grid_map_quad3 = copy.deepcopy(grid_map)
	for x, y in quad[1:-1]:
		x = -x+center_point[0]
		y = -y+center_point[1]
		print((x, y))
		grid_map_quad3[y][x] = 1

	x_offset = -radius*2
	y_offset = -radius*2 - 0.5
	data_extent = (x_offset, x_offset + len(grid_map), y_offset, y_offset + len(grid_map[0]))
	plot.imshow(grid_map_quad3, extent=data_extent, origin="lower")


	# 4th quad
	print("4th Quadrant")
	grid_map_quad4 = copy.deepcopy(grid_map)
	for x, y in quad[:-1]:
		x = x+center_point[0]
		y = -y+center_point[1]
		print((x, y))
		grid_map_quad4[y][x] = 1

	x_offset = -0.5
	y_offset = -radius*2 - 0.5
	data_extent = (x_offset, x_offset + len(grid_map), y_offset, y_offset + len(grid_map[0]))
	plot.imshow(grid_map_quad4, extent=data_extent, origin="lower")
	
	plt.show()


algos = {
	1: BresenhamAlgorithm,
	2: MidPointAlgorithm,
}
algos_names = ["Circle > BresenhamAlgorithm", "Circle > MidPointAlgorithm"]
algo_to_run = None