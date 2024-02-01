import re

users_email = ["qqq_123@gmail.com", "Qjhg%ji@mail.com", "qwerttyuiopasdfghjklzxcvbnm@gmai.com", "Lqwe123@gmail/com", "Sss.11@gmail.com", "@gmail.com", "QWE@gmail.ua"]
min_symbol = 5
max_symbol = 20
def user_email_adress(email_list):
    for email in email_list:
        if re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email) and max_symbol > len(email) > min_symbol:
            print("Valid address:", email)
        else:
            print("Invalid address:", email)


user_email_adress(users_email)
