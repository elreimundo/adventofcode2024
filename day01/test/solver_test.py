from day01.src.solver import solve

def test_parse():
	test_input = """
	3   4
	4   3
	2   5
	1   3
	3   9
	3   3
""".splitlines()
	assert(solve(test_input) == 11)