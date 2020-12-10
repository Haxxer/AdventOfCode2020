import os
import re
text_file = os.path.join(
	os.path.dirname(__file__),
	'input.txt'
)
input_set = open(text_file).read().splitlines()
regex = re.compile(r' bags{0,}\.{0,}')

input_set = dict(zip(
	[regex.sub('', bag_set).split(' contain ')[0] for bag_set in input_set],
	[{
		'name': [sub_bag[2:] for sub_bag in regex.sub('', bag_set).split(' contain ')[1].split(', ')] if 'no other bags' not in bag_set else [],
		'num': [int(sub_bag[0]) for sub_bag in regex.sub('', bag_set).split(' contain ')[1].split(', ')] if 'no other bags' not in bag_set else []
	} for bag_set in input_set]
))

def search_bags(search_term):

	containers = []

	for parent_bag, child_bags in input_set.items():
		if search_term in child_bags['name']:
			containers.append(parent_bag)

	final_containers = []

	for container in containers:
		final_containers += search_bags(container)

	final_containers += containers

	return final_containers

print("First solution: {}".format(len(set(search_bags('shiny gold')))))


def bagception(search_term):

	total = sum(input_set[search_term]['num'])

	for index, child_bag in enumerate(input_set[search_term]['name']):

		total += bagception(child_bag) * input_set[search_term]['num'][index]
	
	return total

	
print("Second solution: {}".format(bagception('shiny gold')))