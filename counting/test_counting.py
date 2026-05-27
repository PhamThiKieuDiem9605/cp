from counting.counting import max_freq

# Test case 1
nums = [1,1,1,2,3]
result = max_freq(nums)
assert result == 1
print("Test passed!")

# Test case 2
nums = [1,2,2,2,3]
result = max_freq(nums)
assert result == 2          
print("Test passed!")

# Test case 3
nums = [3,1,1,2,3]
result = max_freq(nums)
assert result == 3
print("Test passed!")