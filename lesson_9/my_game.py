def my_game():
    start = 1
    end = 10
    print(f"Guess a number between {start} and {end}")

    while True:
        middle_number = (start + end) // 2
        print(f"Is your number {middle_number}?")
        user_input = input('"+" -> yes, "-" -> no: ')

        if user_input == '+':
            print(f"We guessed your number: {middle_number}")
            return
        elif user_input == '-':
            print(f"Your number is bigger than {middle_number}")
            user_input = input('"+" -> yes, "-" -> no: ')

            if user_input == "+":
                start = middle_number + 1
                if end >= 11:
                    print("Number is out of range")
                    return
            elif user_input == "-":
                end = middle_number - 1
                if start <= 0:
                    print("Number is out of range")
                    return
            else:
                print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")


my_game()
