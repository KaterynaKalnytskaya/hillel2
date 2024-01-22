def exponentiation(my_list, degree):
    if degree == 0:
        return [1] * len(my_list)
    elif degree < 0:
        return [0] * len(my_list)
    else:
        result = []
        for num in my_list:
            result.append(num ** degree)
        return result
list_nums = [2, 3, 4, 5]
degree = 5
result = exponentiation(list_nums, degree)
print(result)
