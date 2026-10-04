# dictionaries are collections that don't allow duplicate values unordered and mutable

car = {
    'color': 'red', 
    'brand': 'Volvo',
    'year': 1964
}

print(car)
print(car['color'])
print(car.get('color'))
"""
car['color'] is the same as car.get('color'), but it will raise an error if the key doesn't exist, 
and the 'get' method will return None if the key doesn't exist, also the 'get' method can take a default value as a parameter

in performance car['color'] is faster because it's not calling a function, but if they key doesn't exist will become slower and 
you gotta catch the error to not stop the program
"""
car.get('color', 'blue')
print(car.get('color', 'blue'))

print(car.keys())
print(car.values())

car.update({'year': 2000, 'plate': 'ABC-1234'}) #change a value and add another
print(car)

car.pop('year') #remove a key and value
print(car)

car.popitem() #removes the last key and value
print(car)

# car.clear() #removes all key and value
# print(car)



#-----------------------------

for k in car:
    print(k)

for v in car.values():
    print(v)

for k, v in car.items():
    print(k, v)

#-------------------------
# nested dictionaries

family = {
    'child1' : {
        'name': 'John',
        'year': 2000,
        'color': 'red'
    },
    'child2' : {
        'name': 'Jane',
        'year': 2001,
        'color': 'blue'
    },
    'child3' : {
        'name': 'Bob',
        'year': 2002,
        'color': 'green'
    }
}

print(family['child1']['name'])
