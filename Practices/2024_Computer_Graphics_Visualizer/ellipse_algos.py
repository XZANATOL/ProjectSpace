import matplotlib.pyplot as plt
import copy
import sys

def get_plot():
	graph, plot = plt.subplots()
	plot.grid()
	return plot


def EllipseMidPointAlgorithm(center_point: list[int], radius_point: list[int], grid_map: list[list[int]]) -> None:
	plot = get_plot()

	plt.xlim(-len(grid_map), len(grid_map))
	plt.ylim(-len(grid_map[0]), len(grid_map[0]))

	x0 = 0
	y0 = radius_point[1]

	p_k = radius_point[1]**2 - radius_point[0]**2 * radius_point[1] + 0.25*radius_point[0]**2

	x_plot = 0
	y_plot = 0
	quad = [(x0, y0)]

	# 1st Quad
	print("1st Quadrant")
	print((x0, y0))
	grid_map_quad1 = copy.deepcopy(grid_map)
	grid_map_quad1[y0][x0] = 1
	while 2*radius_point[1]**2 * x0 < 2*radius_point[0]**2 * y0:
		print(2*radius_point[1]**2 * x0, 2*radius_point[0]**2 * y0)
		if p_k < 0:
			x0 += 1
			p_k = p_k + 2*radius_point[1]**2 * x0 + radius_point[1]**2
		else:
			x0 += 1
			y0 -= 1
			p_k = p_k + 2*radius_point[1]**2 * x0 - 2*radius_point[0]**2 * y0  + radius_point[1]**2

		x_plot = x0 + center_point[0]
		y_plot = y0 + center_point[1]
		quad.append((x0, y0))
		print((x_plot, y_plot))
		grid_map_quad1[y_plot][x_plot] = 1

	quad += [(item[1], item[0]) for item in quad[::-1]]
	plot.imshow(grid_map_quad1)
	plt.show()
	
	# !!!!!
	sys.exit()

algos = {
	1: EllipseMidPointAlgorithm
}
algos_names = ["Ellipse > EllipseMidPointAlgorithm"]