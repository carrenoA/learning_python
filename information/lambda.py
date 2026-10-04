# lambda is an anonymous function (function without a name)
# we use lambda when we need a function for a short time

num1 = lambda a : a + 1 # a is an argument like in a regular function, and the information after the : is the return value of the function
print(num1(2))

num1 = lambda a, b : a + b # lambda can have more than one argument
print(num1(2, 3))

#-----------------------

def funcionlambda(n):
    return lambda a : a * n

myfunc = funcionlambda(3) # the argument 'n' is the 3, which means it will multiply by 3

print(myfunc(11)) # the argument 'a' is the 11, which means it will multiply by 3