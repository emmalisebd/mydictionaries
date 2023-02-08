person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)


# print out name of the second child
print(person['children'][1])

# print out name of cat
print(person['pets']['cat'])

# iterate through all children and print out each child
for name in person['children']:
    print(name)

# print out the pets in this format:
# type of pet: dog name of pet: Fido
for pet in person['pets']:
    print(person['pets'][pet])  # add format
