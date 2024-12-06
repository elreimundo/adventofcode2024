from .calculator import calculate_cumulative_distance_between, calculate_similarity_score_for
from .parser import parse

def solve(input: list[str]) -> int:
	[left_list, right_list] = parse(input)
	return calculate_cumulative_distance_between(sorted(left_list), sorted(right_list))

def solve_similiarity(input: list[str]) -> int:
	[left_list, right_list] = parse(input)
	return calculate_similarity_score_for(sorted(left_list), sorted(right_list))