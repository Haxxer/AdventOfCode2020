input_set = open('Day2.txt').read().splitlines()

def solution_one():

	valid = 0
	for item in input_set:
		num_range, letter, text = item.split(" ")
		start, end = map(int, num_range.split('-'))
		length = len(text.split(letter[0]))
		if length >= start and length <= end:
			valid += 1
	return valid

print(solution_one())


def solution_two():
	valid = 0
	for item in input_set:
		num_range, letter, text = item.split(" ")
		first, second = map(int, num_range.split('-'))
		if (text[first-1] == letter[0]) ^ (text[second-1] == letter[0]):
			valid += 1
	return valid

print(solution_two())

