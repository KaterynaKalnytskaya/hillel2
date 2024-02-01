def binary_search_recursive(search_number, arr, first_index, last_index, attempts):
    if first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        attempts += 1

        if arr[mid_index] == search_number:
            print(f"Congratulations!!! Your number {search_number} is at position {mid_index + 1}.")
            return attempts
        elif arr[mid_index] < search_number:
            print("Try a higher number.")
            return binary_search_recursive(search_number, arr, mid_index + 1, last_index, attempts)
        else:
            print("Try a lower number.")
            return binary_search_recursive(search_number, arr, first_index, mid_index - 1, attempts)
    else:
        print("Sorry, your number is not in the list.")
        return -1

search_number = 7
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_index = 0
last_index = len(arr) - 1
attempts = 0

result = binary_search_recursive(search_number, arr, first_index, last_index, attempts)
if result != -1:
    print(f"Number of attempts: {result}")
