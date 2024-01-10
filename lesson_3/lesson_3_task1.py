try:
    user_select = int(input('Enter number of the day: '))

    match user_select:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Incorrect number")
except ValueError as error:
    print("Please enter only integer number")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")





