num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
def summa(num1, num2):
    if num1 > num2:
        return 0
    else:
        return num1 + summa(num1+1, num2)


print(summa(int(num1), int(num2)))

###########################################################
## summa(num1+1,num2) => 9
## num1 -> + num1+1 => 2
## num1+1 -> + num1+1 => 3
## num2 => 4
