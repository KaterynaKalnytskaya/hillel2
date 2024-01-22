def prime_nums(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_nums(list1):
    count = 0
    for num in list1:
        if prime_nums(num):
            count += 1
    return count

my_list = [2, 3, 5, 7, 10, 11, 13, 25, 67, 101]
result = count_prime_nums(my_list)
print(f"Number of prime numbers in the list: {result}")

