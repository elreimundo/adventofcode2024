from day01.src.solver import solve, solve_similiarity

def test_solve():
	test_input = """
	3   4
	4   3
	2   5
	1   3
	3   9
	3   3
""".splitlines()
	assert(solve(test_input) == 11)

def test_solve_similarity():
	test_input = """
	3   4
	4   3
	2   5
	1   3
	3   9
	3   3
""".splitlines()
	assert(solve_similiarity(test_input) == 31)