
# task 4

some_text = "Wellcome home!"
print(some_text[3])
print(some_text[-2])
print(some_text[:5])
print(some_text[:12])
print(some_text[::2])
print(some_text[0:15:2])
print(some_text[::-1])
print(some_text[::-2])
print(len(some_text))

#dop


some_text = ("heLLo! mY naMe is Kateryna! I am 37 years old."
                 " I lIVe in Spain during 2 years. WHat is your name?"
                 " How old aRE you? Where are yOU from?")
number_of_digits = 0
number_of_exclamation = 0
count_separator = 0
symbol_list = "!",".","?"
for i in some_text:
    if i.isdigit():
        number_of_digits += 1
    elif i in some_text:
        if i == "!":
            number_of_exclamation += 1
print(f"There are:",number_of_digits, "numbers of digit in the text.")
print(f"There are:",number_of_exclamation,"exclamation points in the text")



