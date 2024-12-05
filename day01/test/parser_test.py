from day01.src.parser import parse

def test_parse():
	test_input = """
	3   4
	4   3
	2   5
	1   3
	3   9
	3   3
""".splitlines()
	assert(parse(test_input) == [[3,4,2,1,3,3], [4,3,5,3,9,3]])