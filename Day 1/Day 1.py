import os
text_file = os.path.basename(__file__).replace('.py','.txt')
input_set = open(text_file).read().splitlines()
input_set = set([int(item) for item in input_set])

def solution_one():
	for x in input_set:
		# python's 'in' is crazy fast on sets, not so much on lists
		if 2020-x in input_set:
			return x*(2020-x)

print("Solution 1: {}".format(solution_one()))

def solution_two():
	second_set = input_set.copy()
	for x in input_set:
		for y in second_set:
			if 2020-x-y in input_set:
				return x*y*(2020-x-y)
		second_set.remove(x)

print("Solution 2: {}".format(solution_two()))
