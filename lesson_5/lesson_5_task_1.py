numbers = [-1, -4, 8, 3, 2, 4, 7, 3, 7, -9]

summ_neg = sum(num for num in numbers if num < 0)
print("Sum of negative numbers:", summ_neg)


summ_even = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", summ_even)


summ_odd = sum(num for num in numbers if num % 2 != 0)
print("Sum of odd numbers:", summ_odd)


mult_by_three = 1
for num in numbers:
    if num % 3 == 0:
        mult_by_three *= num
print("Product of numbers divisible by 3:", mult_by_three)


min_num = min(numbers)
max_num = max(numbers)
result = 1
for num in numbers:
    if num != min_num and num != max_num:
        result *= num
print("Product of all numbers except min and max:", result)


first_positive_index = next(i for i, num in enumerate(numbers) if num > 0)
last_positive_index = next(i for i in range(len(numbers) - 1, -1, -1) if numbers[i] > 0)
sum_between = sum(numbers[first_positive_index + 1:last_positive_index])
print("Sum between first and last positive elements:", sum_between)
