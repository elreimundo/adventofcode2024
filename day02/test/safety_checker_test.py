from day02.src.safety_checker import check_safety

def test_safety_increasing():
	assert(check_safety([1,3,6,7,9]) is True)

def test_safety_decreasing():
	assert(check_safety([7,6,4,2,1]) is True)

def test_unsafe_large_delta():
	assert(check_safety([1,2,7,8,9]) is False)
	assert(check_safety([9,7,6,2,1]) is False)

def test_unsafe_direction_change():
	assert(check_safety([1,3,2,4,5]) is False)

def test_unsafe_zero_delta():
	assert(check_safety([8,6,4,4,1]) is False)
