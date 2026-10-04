vehicles = ['bmw', 'audi', 'mercedes', 'ferrari', 'tesla']

vehicles.insert(0, 'porsche')   # add an element at a specific position
vehicles.append('lamborghini') #add an element at the end of the list
vehicles.remove('audi') # remove an element by value
vehicles.pop(1) # remove an element by index
vehicles.sort() # sort the list
# vehicles.reverse() # reverse the list

print(vehicles)

#------------------------------------------------------------------

frutes1 = ['apple', 'banana', 'cherry']
frutes2 = ['kiwi', 'orange', 'mango']

frutes1.extend(frutes2) # add the elements of frutes2 to frutes1 and change the original list

print(frutes1)

frutes3 = ['apple', 'banana', 'cherry']
frutes4 = ['kiwi', 'orange', 'mango']

frutes3 = frutes3 + frutes4 # add the elements of frutes2 to frutes1 and do not change the original list

print(frutes3)
