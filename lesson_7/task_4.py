numbers = [2, 34, 5, 2, 2, 2, 6, 2, 2]
def my_function(nums,digit_foremove):
    while digit_foremove in numbers:
        if digit_foremove:
            numbers.remove(digit_foremove)
    return nums
res = my_function(numbers,2)
print(res)
