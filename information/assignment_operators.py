# += add the value to the variable
# -= subtract the value from the variable
# *= multiply the value by the variable
# /= divide the value by the variable
# %= get the remainder of the division of the value by the variable
# **= exponentiate the value by the variable
# //= integer division of the value by the variable

# Walrus operator :=

text = "Hello world"

if(n := len(text)) > 10:
    print("nice")
else:
    print("not nice")