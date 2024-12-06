def calculate_cumulative_distance_between(sorted_list_1: list[int], sorted_list_2: list[int]) -> int:
	cumulative_distance = 0
	if len(sorted_list_1) != len(sorted_list_2):
		raise "uh oh"
	index = 0
	while index < len(sorted_list_1):
		cumulative_distance += abs(sorted_list_1[index] - sorted_list_2[index])
		index += 1
	return cumulative_distance

def calculate_similarity_score_for(sorted_list_1: list[int], sorted_list_2: list[int]) -> int:
	cumulative_similarity_score = 0
	right_list_count = {}
	for value in sorted_list_2:
		if value in right_list_count:
			right_list_count[value] += 1
		else:
			right_list_count[value] = 1
	for scoring_value in sorted_list_1:
		if scoring_value in right_list_count:
			cumulative_similarity_score += scoring_value * right_list_count[scoring_value]
	return cumulative_similarity_score