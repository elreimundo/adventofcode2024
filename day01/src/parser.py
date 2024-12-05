import re

def parse(lines: list[str]) -> list[list[int], list[int]]:
	regexp = re.compile(r'\s*(\d+)\s+(\d+)\s*')
	left_list, right_list = [], []
	for line in lines:
		matches = regexp.match(line.strip())
		if (matches != None):
			left_list.append(int(matches.group(1)))
			right_list.append(int(matches.group(2)))
	return [left_list, right_list]
