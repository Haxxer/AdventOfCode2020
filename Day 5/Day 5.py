import os
import math
text_file = os.path.join(
	os.path.dirname(__file__),
	os.path.basename(__file__).replace('.py','.txt')
)
input_set = open(text_file).read().splitlines()

def solution_one(boarding_pass):

	row = 0
	nums = [0, 127]
	for letter in boarding_pass[:7]:
		if letter == "B":
			nums[0] = math.ceil((nums[0]+nums[1])/2)
			row = nums[0]
		else:
			nums[1] = math.floor((nums[0]+nums[1])/2)
			row = nums[1]

	col = 0
	nums = [0,7]
	for letter in boarding_pass[7:]:
		if letter == "R":
			nums[0] = math.ceil((nums[0]+nums[1])/2)
			col = nums[0]
		else:
			nums[1] = math.floor((nums[0]+nums[1])/2)
			col = nums[1]

	return [row, col, row*8+col]


seats = list(map(solution_one, input_set))

print("Solution one: {}".format(max(seats)[2]))


def solution_two(seats):
	seats.sort()
	for index, seat in enumerate(seats):
		if index > 0 and index != len(seats)-1:
			subtract = seat[1] - seats[index-1][1]
			if subtract != 1 and subtract != -7:
				return seat[0]*8 + (seat[1]-1)
	
	
print("Solution one: {}".format(solution_two(seats)))