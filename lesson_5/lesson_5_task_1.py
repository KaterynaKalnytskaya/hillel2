numbers = [-1, -4, 8, 3, 2, 4, 7, 3, 7, -9]
summ = 0
summ1 = 0
summ2 = 0
mult = 1
elements = []
min_num = min(numbers)
max_num = max(numbers)
for negative_num in numbers:
    if negative_num < 0:
        summ += negative_num
print(summ)
for i in numbers:
    if i % 2 == 0:
        summ1 += i
print(summ1)
for j in numbers:
    if j % 2 != 0:
        summ2 += j
print(summ2)
for q in numbers:
    if q % 3 == 0:
        mult *= q
print(mult)
result = 1
for r in numbers:
    if min_num != r and max_num != r:
        result *= r
        print(result)
first_positive_index = None
last_positive_index = None
for i in range(len(numbers)):
    if numbers[i] > 0:
        first_positive_index = i
        break
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = i
        break
sum_between = sum(numbers[first_positive_index+1:last_positive_index])
print("Sum between first and last positive elements:", sum_between)






























