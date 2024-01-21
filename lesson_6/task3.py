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