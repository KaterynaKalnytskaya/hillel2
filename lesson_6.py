# task 1
list_1 = [1, 2, 5, 5, 2, 8, 9]
print(set(list_1))


# task 2
list_1 = [1, 4, 7, 9, 4, 6, 8]
list_2 = [4, 2, 5, 3, 8, 7, 10]
nums = set(list_1)
nums2 = set(list_2)
print(nums.difference(nums2))
print(len(nums.difference(nums2)))
print(nums2.difference(nums))
print(len(nums2.difference(nums)))


# task 3
some_text = "3 Hello! How are you? I am ok! Where are you? I am at home."
num = ""
counter = 0
for number in some_text:
    if number.isnumeric():
        num += number
        counter += 1
    else:
        break
num = int(num)
print(num)
some_text = some_text[counter + 1:]
print(some_text)
unique_words = list(set(some_text.split()))
print(unique_words)


# task 4
strana_1 = dict.fromkeys(["Ukraine"], ["Kharkov", "Odessa", "Kiev"])
strana_2 = dict.fromkeys(["USA"], ["Los Angeles", "Las Vegas"])
print(strana_1)
print(strana_2)


# task 5
list_1 = [1, 2, 3, 4]
list_2 = ["one", "two", "three", "four"]
slovar = dict(zip(list_1, list_2))
print(slovar)



