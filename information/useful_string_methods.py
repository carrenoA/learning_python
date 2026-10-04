# .strip() is used to remove leading and trailing whitespace by default, if we set a parameter, it will remove that character from the beginning and end of the string
# Example:
"   hello   ".strip() # returns "hello"
"   hello   ".strip(" ") # returns "hello"
"   hello   ".strip("l") # returns "   hello   "


# Slicing: [start (it's included):end (it's not included):step (the default is 1)]
"hello"[1:3] # returns "el"
"hello"[1:] # returns "ello"
"hello"[:3] # returns "hel"
"hello"[::-1] # returns "olleh"

# .replace(old, new)
"hello".replace("l", "x") # returns "hexxo"


# .split(separator) creates a list of substrings separated by the separator
"hello".split("l") # returns ["he", "o"]
"hello".split() # returns ["hello"]
"hello".split(" ") # returns ["hello"]

# .upper() and .lower() convert the string to uppercase and lowercase respectively
"hello".upper() # returns "HELLO"
"hello".lower() # returns "hello"

# \n is a special character that represents a newline