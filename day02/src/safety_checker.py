def check_safety(levels: list[int]) -> bool:
	previous_level = None
	direction = None
	for level in levels:
		if previous_level is not None:
			delta = level - previous_level
			if delta == 0:
				return False
			elif delta > 0:
				if direction is None:
					direction = 1
				if direction < 0 or delta > 3 or delta < 1:
					return False
			else:
				if direction is None:
					direction = -1
				if direction > 0 or delta < -3 or delta > -1:
					return False
		previous_level = level
	return True
