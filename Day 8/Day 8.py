import os
import copy

text_file = os.path.join(
	os.path.dirname(__file__),
	'input.txt'
)
input_set = open(text_file).read().splitlines()
input_set = [
	[line.split(' ')[0], int(line.split(' ')[1])]
	for line in input_set
]

class Program(object):

	def __init__(self, input):
		super(Program, self).__init__()

		self.input = input
		self._potential_rulesets = None

	@property
	def potential_rulesets(self):

		if not self._potential_rulesets:

			potential_bad_lines = []
			for index, line in enumerate(self.input):
				if line[0] == "jmp" or line[0] == "nop":
					potential_bad_lines.append(index)

			self._potential_rulesets = []
			for bad_line in potential_bad_lines:
				new_ruleset = copy.deepcopy(self.input)
				new_ruleset[bad_line][0] = "jmp" if new_ruleset[bad_line][0] == "nop" else "nop"
				self._potential_rulesets.append(new_ruleset)
		
		return self._potential_rulesets

	def execute_solution_one(self):
		self.accumilator = 0
		self.current_line = 0
		self.visited_lines = set()
		self.current_ruleset = self.input
		self.execute()

	def execute_solution_two(self):
		for ruleset in self.potential_rulesets:
			self.accumilator = 0
			self.current_line = 0
			self.visited_lines = set()
			self.current_ruleset = ruleset
			self.success = False
			self.execute()
			if self.success:
				break

	def execute(self):
		
		if self.current_line > len(self.current_ruleset)-1:
			self.success = True
			return
		elif self.current_line not in self.visited_lines:
			self.visited_lines.add(self.current_line)
		else:
			return

		line = self.current_ruleset[self.current_line]

		if line[0] == "nop":
			self.current_line += 1
		elif line[0] == "acc":
			self.accumilator += line[1]
			self.current_line += 1
		elif line[0] == "jmp":
			self.current_line += line[1]			

		self.execute()

gameboy = Program(input_set)

gameboy.execute_solution_one()
print("Solution one: {}".format(gameboy.accumilator))

gameboy.execute_solution_two()
print("Solution two: {}".format(gameboy.accumilator))