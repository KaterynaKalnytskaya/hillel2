def get_number_pow(number, number_pow):
    if number_pow <= 1:
        return number
    return number * get_number_pow(number, number_pow - 1)

print(get_number_pow(2,3))

####################################
## number_pow 3 -> * number 2 => 8
## number_pow 2 -> * number 2 => 4
## number_pow 1 => 2
