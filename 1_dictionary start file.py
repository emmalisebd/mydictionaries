import random

# dictionary requires a key and returns a value
# first way to create dictionary
phonebook = {}  # creates empty dictionary

# second way to create dictionary           #lists use square brackets
phonebook = {'Chris': '555−1111',  # dictionaries use curly brackets and have key value pairs instead of index
             'Katie': '555−2222',  # key is on left "Katie", value is on right "555-2222"
             'Joanne': '555−3333'}           # 3 key value pairs here


print()
print('*****  start section 1 - print dictionary ********')
print()

# third way to create dictionary
mydictionary = dict(m=8, n=9)
print(mydictionary)

print(len(phonebook))  # shows how many key value pairs
print(type(phonebook))  # shows that it's a dictionary vs list or other


print()
print('*****  end section 1 ********')
print()


print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:  # default method is key (phone number)
    print(phonebook[name])
else:
    # Chris's number will be returned
    print(f"{name} is not in the phonebook")

# phone = phonebook["chris"]
# print(phone)


print()
print('*****  end section 2 ********')
print()


# dictionaries are mutable objects meaning you can edit them
# keys in dictionaries have to be unique, cannot have a duplicate key
print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Chris'] = '555-0123'  # updated chris's key
# appended Joe bc he did not previously exist
phonebook['Joe'] = '555-4444'
print(phonebook)

print()
print('*****  end section 3 ********')
print()


print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)

del phonebook['Chris']  # deletes Chris's key value pair

print(phonebook)

print()
print('*****  end section 4 ********')
print()


print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    # must call dictionary and provide key to get the phone number
    print(f" The key is {key} and the value is {phonebook[key]}")

for value in phonebook.values():        # .values method iterates just the values side (right side)
    print(value)

# if you don't split it using the .items method, it will return a tuple which you cannot edit
for key, value in phonebook.items():
    # don't need to call phonebook bc the .items method already does
    print(f"The key is {key} and the value is {value}")

for ph_tuple in phonebook.items():
    print(ph_tuple)

print()
print('*****  end section 5 ********')
print()


print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris', '999')  # default of 999 if "Chris" isn't found
print(phone)

phonebook.clear()
print(phonebook)  # creates an empty dictionary but does not delete data


print()
print('*****  end section 6 ********')
print()


print()
print('*****  start section 7 - using pop method ********')
print()

# pop removes the value called so it won't print
remove = phonebook.pop('Chris', 'not found')
print(remove)
print(phonebook)


print()
print('*****  end section 7 ********')
print()


print()
# pops out last item in the dictionary
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()
print(a)  # Joanne gets deleted every time
print(phonebook)


print()
print('*****  end section 8 ********')
print()


print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook_list = list(phonebook)
print(phonebook_list)
# random.choice only works for lists
random_key = random.choice(phonebook_list)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])

print()
print('*****  end section 9 ********')
print()
