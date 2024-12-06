from .parser import parse
from .safety_checker import check_safety

def count_safe_reports(inputs: list[str]) -> int:
	safe_reports = 0
	reports = parse(inputs)
	for report in reports:
		if check_safety(report):
			safe_reports += 1
	return safe_reports
