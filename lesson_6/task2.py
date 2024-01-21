# task 2
list_1 = [1, 4, 7, 9, 4, 6, 8]
list_2 = [4, 2, 5, 3, 8, 7, 10]
nums = set(list_1)
nums2 = set(list_2)
print(nums.difference(nums2))
print(len(nums.difference(nums2)))
print(nums2.difference(nums))
print(len(nums2.difference(nums)))