first_set = open('Day1.txt').read().splitlines()
first_set = set([int(item) for item in first_set])

def solution_one():
	for x in first_set:
		# python's 'in' is crazy fast on sets, not so much on lists
		if 2020-x in first_set:
			return x*(2020-x)

print("Solution 1: {}".format(solution_one()))

def solution_two():
	second_set = first_set.copy()
	for x in first_set:
		for y in second_set:
			if 2020-x-y in first_set:
				return x*y*(2020-x-y)
		second_set.remove(x)

print("Solution 2: {}".format(solution_two()))
