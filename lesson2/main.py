num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3: "))
middle_value = (num1 + num2 + num3) / 3
print(max(num1, num2, num3))
print(min(num1, num2, num3))
print(middle_value)


distance = int(input("Enter length in meters: "))
if distance <= 0:
    print("Wrong distance")
elif distance > 0:
    measure = str(input("Enter one of measure: yard, inch, mile   "))
    if measure == "yard":
        yards = distance * 1.0936
        print(f"Distance in yard:{yards} ")
    elif measure == "mile":
        miles = distance * 0.00062137
        print(f"Distance in miles:{miles} ")
    elif measure == "inch":
        inch = distance * 39.26
        print(f"Distance in inch:{inch} ")
    else:
        print("Choose correct measure: yard, inch, mile")




