# tuples are ordered collections that cannot be changed
tuple = ('apple', 2, True)

print(type(tuple))
print(tuple)

x, y, z = tuple #for doing this you need to add the same values as the tuple has
print(x, y, z)

#------------------------------------------------
#wrong
tuple2 = ('test') 
print(type(tuple2))
"""
python doesn't recognize this as a tuple, it will remove the parentheses and take it as a string, if you want a tuple with just one value you need to add a comma after the first value
"""

#good
tuple3 = ('test',)
print(type(tuple3))