# to open a file, we use the open() function

# r = read
# w = write
# a = append
# x = create
# t = text mode
# b = binary mode
# += append and read


#enconding="utf-8" to read better the file, without it will be read with the system default enconding


# #first option
# try:
#     file = open("test.txt", "r") #r = read mode and "test.txt" the file name in string format
#     print(file.readline()) #readline just read the first line of the file
#     file.close() #close the file
# except FileNotFoundError:
#     print("File not found")

#second option (better option because it close the file automatically)
#read
try:
    with open("test.txt", "r", encoding="utf-8") as file: #change the order and the variable is at the end in string format
        print(file.read()) #read the entire file
except FileNotFoundError:
    print("File not found")


#append
try:
    with open("test.txt", "a") as file: 
        file.write("\nThis is a new line\n")
except TypeError:
    print("File is a file")


#create
try:
    with open("test2.txt", "r", encoding="utf-8") as file: #change the order and the variable is at the end in string format
        print(file.read()) #read the entire file
except FileNotFoundError:
    question = input("The file you are trying to open doesn't exist. Do you want to create it? (y/n): ")
    if question.lower() == "y":
        with open("test2.txt", "x") as file: 
            print("File created successfully")
    else:
        print("File not created")