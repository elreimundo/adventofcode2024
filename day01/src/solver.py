from .calculator import calculate_cumulative_distance_between
from .parser import parse

def solve(input: list[str]) -> int:
	[left_list, right_list] = parse(input)
	return calculate_cumulative_distance_between(sorted(left_list), sorted(right_list))
