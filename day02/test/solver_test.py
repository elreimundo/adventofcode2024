from day02.src.solver import count_safe_reports

def test_example():
	input = """
	7 6 4 2 1
	1 2 7 8 9
	9 7 6 2 1
	1 3 2 4 5
	8 6 4 4 1
	1 3 6 7 9
	""".splitlines()
	assert(count_safe_reports(input) == 2)
