def binary_search(arr, search_value) -> int:
    first_index = 0
    last_index = len(arr) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if arr[mid_index] == search_value:
            return mid_index
        else:
            if arr[mid_index] < search_value:
                first_index = mid_index + 1
            else:
                last_index = mid_index - 1

    return -1  # -1 означає, що значення не знайдено


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
value = 9
result = binary_search(numbers, value)
if result != -1:
    print(f"Item: {value} found at index {result}")
else:
    print("Not found")
