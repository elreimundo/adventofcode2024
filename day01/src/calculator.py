def calculate_cumulative_distance_between(sorted_list_1: list[int], sorted_list_2: list[int]) -> int:
	cumulative_distance = 0
	if len(sorted_list_1) != len(sorted_list_2):
		raise "uh oh"
	index = 0
	while index < len(sorted_list_1):
		cumulative_distance += abs(sorted_list_1[index] - sorted_list_2[index])
		index += 1
	return cumulative_distance
