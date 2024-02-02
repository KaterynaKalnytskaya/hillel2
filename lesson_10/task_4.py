import re

clients_names = ["Ivan Ivanovich Ivanov", "Petr Petrovich Petrov", "Sam", "Daniel Marks", "Катерина Викторовна Тур",
                 "Hieruhriehgierurhirughirugh HIuhiuhiu Uiuhiuhiu", "Sergey 123 Qwe"]


def full_name(name):
    for name in clients_names:
        if re.match(r'^\w\D{2,20}( \w\D{2,20}){2}$', name):
            print("Valid name:", name)
        else:
            print("Invalid name:", name)


full_name(clients_names)
