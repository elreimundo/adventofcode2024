def parse(lines: list[str]) -> list[list[int]]:
	records = []
	for line in lines:
		record = []
		current_number = None
		for char in line.strip():
			if char.isnumeric():
				if current_number is None:
					current_number = int(char)
				else:
					current_number = current_number * 10 + int(char)
			else:
				if current_number is not None:
					record.append(current_number)
					current_number = None
		if current_number is not None:
			record.append(current_number)
		if len(record) > 0:
			records.append(record)
	return records
