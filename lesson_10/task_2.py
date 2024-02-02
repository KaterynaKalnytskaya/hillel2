import re
list_phone_numbers = ["+30000000000", "0661111111", "+311111111111", "+111111111111", "+1090909090901", "+09090q0077777", "+21111111111", "0509898989"]


def phone_numbers(phone_number_list):
    for phone_number in phone_number_list:
        if re.findall(r'^\+\d+$', phone_number) and len(phone_number) == 13:
            print("Valid number:", phone_number, "len of number = +12")
        elif re.findall(r'^\d+$', phone_number) and len(phone_number) == 10:
            print("Valid number:", phone_number, "len of number = 10")
        else:
            print("Invalid number", phone_number)


phone_numbers(list_phone_numbers)
