import re

list_home_numbers = ['9370733', '7093312', '7053344', '9400111', '789789789', '555666777', '565788']
def home_numbers_list(phone_number_list):
    for number in phone_number_list:
        if re.compile(r'^\d+$') and len(number) == 7:
            print("Valid number:", number)
        else:
            print("Invalid number", number)


home_numbers_list(list_home_numbers)



