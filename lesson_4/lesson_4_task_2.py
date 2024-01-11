# task 2
some_text = input("Enter text: ")
result_symbol = 0
for i in some_text:
    if i == '@':
        result_symbol += 1
print(f"The number of symbol '@' in the text:", result_symbol)

