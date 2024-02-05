numbers = [1, 5, 2, 4, 7, -4, -9]

is_even = [num for num in numbers if num % 2 == 0]
is_odd = [num for num in numbers if num % 2 != 0]
negative = [num for num in numbers if num < 0]
positive = [num for num in numbers if num > 0]
print("Even numbers:", is_even)
print("Odd numbers:", is_odd)
print("Negative numbers:", negative)
print("Positive numbers:", positive)
