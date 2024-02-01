def my_game():
    start = 1
    end = 10
    print(f"Guess a number between {start} and {end}")
    while True:
        middle_number = (start + end) // 2
        print(f"Your number: {middle_number}?")
        user_input = input('"+"-> yes, "-" -> no')
        if user_input == '+':
            print(f"We guessed your number:{middle_number}")
            return
        elif user_input == '-':
            print(f"Your number bigger then {middle_number}")
            user_input = input('"+"-> yes, "-"-> no')
            if user_input == "+":
                start = middle_number + 1
            elif user_input == "-":
                end = middle_number - 1
            elif start < 1:
                print("Number is out of range")
            elif end > 10:
                print("Number is out of range")
            else:
                print("Invalid input. Try again.")


my_game()