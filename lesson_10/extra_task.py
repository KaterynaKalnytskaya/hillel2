import re

user_passwords = ["Qwe111%User", "LLLlllllll8!!!))#", "DDD123456789!", "qqqq@#$%pppp", "QWERTYUIOPasdfgh1234567!@#$%^&"]

def list_user_password(passwords):

    for password in passwords:
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+-])[\w!@#$%^&*()_+-]{8,16}$', password):
            print("Valid password:", password)
        else:
            print("Invalid password:", password)


list_user_password(user_passwords)
