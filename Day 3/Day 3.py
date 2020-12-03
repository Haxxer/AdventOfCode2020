import os
from functools import reduce
text_file = os.path.basename(__file__).replace('.py','.txt')
input_set = open(text_file).read().splitlines()

def solution_one():
	trees = 0

	width = len(input_set[0])

	x_pos = 0
	for slope in input_set:
		if slope[x_pos%width] == "#":
			trees += 1
		x_pos += 3

	return trees

print("Solution 1: {}".format(solution_one()))


def solution_two():

	slopes = [
		{"x_speed": 1, "y_speed": 1, "x_pos": 0, "y_pos": 0, "trees": 0},
		{"x_speed": 3, "y_speed": 1, "x_pos": 0, "y_pos": 0, "trees": 0},
		{"x_speed": 5, "y_speed": 1, "x_pos": 0, "y_pos": 0, "trees": 0},
		{"x_speed": 7, "y_speed": 1, "x_pos": 0, "y_pos": 0, "trees": 0},
		{"x_speed": 1, "y_speed": 2, "x_pos": 0, "y_pos": 0, "trees": 0}
	]

	width = len(input_set[0])
	height = len(input_set)

	for y in range(height):
		for slope in slopes:
			if slope['y_pos'] >= height:
				continue
			if input_set[slope['y_pos']][slope['x_pos']%width] == "#":
				slope['trees'] += 1

			slope['y_pos'] += slope['y_speed']
			slope['x_pos'] += slope['x_speed']

	
	trees = reduce(lambda x, y: x*y, [slope['trees'] for slope in slopes])

	return trees

print("Solution 2: {}".format(solution_two()))