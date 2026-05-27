from counting.counting import max_freq

def test_case_1():
    nums = [1,1,1,2,3]
    result = max_freq(nums)
    assert result == 1
    print("Test case 1 passed!")

def test_case_2():
    nums = [1,2,2,2,3]
    result = max_freq(nums)
    assert result == 1
    print("Test case 2 passed!")

def test_case_3():
    nums = [3,1,1,2,3]
    result = max_freq(nums)
    assert result == 2
    print("Test case 3 passed!")