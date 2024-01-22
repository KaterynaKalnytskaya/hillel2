nums = [2, 34, 5, 0, -1, 6]
def my_function(min_number):
    for x in nums:
        if x is min(nums):
            return x
res = my_function(nums)
print(res)
