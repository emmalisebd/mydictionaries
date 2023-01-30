person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out name of the second child
name = 'Betty'

if name in person:
    print(person[name])


# print out name of cat


# iterate through all children and print out each child


# print out the pets in this format:
# type of pet: dog name of pet: Fido
