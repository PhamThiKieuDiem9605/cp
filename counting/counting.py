import logging 
logging.basicConfig(level=logging.INFO)
def max_freq(nums):
    count = {}
    max_freq = 0
    a = 0
    for num in nums:
        logging.info(f"Current number: {num}")
        if num in count:
            count[num] += 1
        else:        
            count[num] = 1
        logging.info(f"Current count: {count}")

    for num in count:
        if count[num] > max_freq:
            max_freq = count[num]
            a = num
    return a

nums = [1,1,1,2,3]
result = max_freq(nums)
print(f"Result: {result}")