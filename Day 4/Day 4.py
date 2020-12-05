import re
import os
text_file = os.path.join(
	os.path.dirname(__file__),
	os.path.basename(__file__).replace('.py','.txt')
)
input_set = open(text_file).read()

multisplit = re.compile(r'[ :]')
passports = input_set.split("\n\n")
passports = [multisplit.split(passport.replace("\n", " ")) for passport in passports]

def solution_one():
	return [passport for passport in passports if len("".join(passport[0::2]).replace("cid", "")) == 21]

valid_passports = solution_one()
print("Solution one: {}".format(len(valid_passports)))

def solution_two(valid_passports):
	return len(list(filter(test_passport, valid_passports)))

def test_passport(passport):
	keys = passport[0::2]
	vals = passport[1::2]
	for key, val in zip(keys, vals):
		if not rule(key, val):
			return False
	return True
			
def rule(type, val):
	if type == "byr":
		return int(val) >= 1920 and int(val) <= 2002
	elif type == "iyr":
		return int(val) >= 2010 and int(val) <= 2020
	elif type == "eyr":
		return int(val) >= 2020 and int(val) <= 2030
	elif type == "hgt":
		if val[-2:] == "in":
			return int(val[:-2]) >= 59 and int(val[:-2]) <= 76
		elif val[-2:] == "cm":
			return int(val[:-2]) >= 150 and int(val[:-2]) <= 193
		return False
	elif type == "hcl":
		return re.match(r'#[0-9a-f]{6}', val)
	elif type == "ecl":
		return val in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
	elif type == "pid":
		return re.match(r'^[0-9]{9}$', val)
	elif type == "cid":
		return True

print("Solution two: {}".format(solution_two(valid_passports)))