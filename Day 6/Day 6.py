import os
from functools import reduce
text_file = os.path.join(
	os.path.dirname(__file__),
	'input.txt'
)
input_set = open(text_file).read()

solution_one = sum([len(set(people.replace('\n', ''))) for people in input_set.split('\n\n')])

print("Solution one: {}".format(solution_one))


groups = [people.split('\n') for people in input_set.split('\n\n')]

total = 0
for group in groups:
	total += len(reduce(lambda a,b: set(a).intersection(b), group))

print("Solution two: {}".format(total))


