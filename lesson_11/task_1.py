import re

with open("text1.txt", "w") as test_file:
    test_file.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings "
                    "and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end "
                    "them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand "
                    "natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep")

with open("text1.txt", "r") as test_file:
    text = test_file.read()
words_in_text = re.findall(r'^[A-Z][a-z]{7,}$', text)

with open("text2.txt", "a") as new_test_file:
    new_test_file.write(" ".join(words_in_text))
print("Filtered words have been written to text2.txt")

with open("text1.txt", "r") as test_file:
    text = test_file.read()
    number_of_words = re.findall(r'\b\w+\b', text)
    word_count = len(number_of_words)
print("The number of words in the text: ", word_count)

with open("text1.txt", "r") as test_file:
    text = test_file.read()
    forbidden_word = re.findall(r'\b[Dd]ie\b', text)
    for word in forbidden_word:
        text = re.sub(r'\b[Dd]ie\b', '***', text)
        forbidden_word_count = len(forbidden_word)
with open("text1.txt", "a") as test_file:
    test_file.write(text)
print("Forbidden words corrected! The number of words:", forbidden_word_count)
