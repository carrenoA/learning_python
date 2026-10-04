#while 

num = 0

while num < 10:
    num += 1
    if num == 8:
        break # stops the entire while loop
    if num == 3:
        continue # stops the current iteration and starts a new one
    print(num)


#for
#list
list1 = [1, 2, 3, 4, 5]
for x in list1:
    if x == 3:
        continue
    if x == 5:
        break
    print(x)

#range
for i in range (0,11,2):
    print(i)

#two lists
list2 = ['a','b','c']
list3 = ['d','e','f']

for i in list2:
    for j in list3:
        print(i, j)
