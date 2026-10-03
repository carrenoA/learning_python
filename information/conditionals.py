# if
# The syntax of if is as follows:
# if condition:
#     code to execute if the condition is true
# elif condition:
#     code to execute if the previous conditions are false and this condition is true
# else:
#     code to execute if all previous conditions are false

# pass keyword is used to create a block of code that does nothing
# syntax:
# pass

num1 = 10
num2 = 20

if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is less than num2")
elif num1 == num2:
    pass # it's here awaiting a condition to be added
else:
    print("num1 is equal to num2")


# 
# match is used to compare a value with a pattern

weak_day = 10
match weak_day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: # this is the default case, it will be executed if none of the above cases match
        print("Invalid day")