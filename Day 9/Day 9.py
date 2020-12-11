import os
from functools import reduce

text_file = os.path.join(
	os.path.dirname(__file__),
	'input.txt'
)
input_set = open(text_file).read().splitlines()
input_set = [int(line) for line in input_set]

def is_number_invalid(index):
	number = input_set[index]
	for outer in input_set[index-25:index-1]:
		for inner in input_set[index-24:index]:
			if outer+inner == number:
				return False
	return number

for index in range(25,len(input_set)):
	invalid = is_number_invalid(index)
	if invalid:
		solution_one = invalid
		print("Solution one: {}".format(solution_one))


def search_solution(number):
	start_index = 0
	end_index = 1
	solution = 0
	
	while solution != number:
		solution = sum(input_set[start_index:end_index])
		if solution < number:
			end_index += 1
		elif solution > number:
			start_index += 1

	return min(input_set[start_index:end_index]) + max(input_set[start_index:end_index])


print("Solution two: {}".format(search_solution(solution_one)))