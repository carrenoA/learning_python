# == is used to check if two values are equal
# != is used to check if two values are not equal
# > is used to check if the value on the left is greater than the value on the right
# < is used to check if the value on the left is less than the value on the right
# >= is used to check if the value on the left is greater than or equal to the value on the right
# <= is used to check if the value on the left is less than or equal to the value on the right
# and is used to check if both values are true
# or is used to check if at least one of the values is true
# not is used to check if the value is false
# is and is not are used to check if two values are the same object

x = 1
y = 2

print(x is y)
print(x is not y)


# conditional expression
# you add the first result at the beginning of the expression, then the condition, then the last result
value = 5 if x > y else 10
print(value)
