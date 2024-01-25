number_symbol = int(input("Enter number of symbol: "))
def get_number_symbol(number_symbol):
    if number_symbol >= 1:
        print("*", end=" ")
        return get_number_symbol(number_symbol-1)
    else:
        print()
get_number_symbol(number_symbol)


#####################################
## get_number_symbol(4) -> + get_number_symbol(1) => 4
## get_number_symbol(3) -> + get_number_symbol(1) => 3
## get_number_symbol(2) -> + get_number_symbol(1) => 2
## get_number_symbol(1) => 1
