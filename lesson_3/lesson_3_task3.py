#task number 3
try:
    number_1 = int(input("Enter number 1: "))
    number_2 = int(input("Enter number 2: "))
    user_select = int(input("Select a math operation: "))
    match user_select:
        case 1:
            print(number_1 + number_2)
        case 2:
            print(number_1 - number_2)
        case 3:
            print(number_2 - number_1)
        case 4:
            print(number_1 * number_2)
        case 5:
            print(number_1 / number_2)
        case 6:
            print(number_2 / number_1)
        case _:
            print("Incorrect number of case!")
except ValueError as error:
    print("Please enter only integer number")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
