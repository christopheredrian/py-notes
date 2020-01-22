import pprint

person = {
    "name": "chris",
    "age": 24
}

# Check if key exists
if "age" in person:
    print("The key 'age' is in person")

# Get keys
print(person.keys())

# Get Values
print(person.values())

# Printing all values
print("All keys in person: ")

for key in person.keys():
    print(person[key])

# Printing keys and values
print("\nAll keys and values:")

for k, v in person.items():
    print("Key: {}. Value: {}".format(k, v))

if 24 in person.values():
    print("The integer 4 is in the values");

dp_value = person.get("dp", "N/A")
print(dp_value)

# if 'dp' not in person:
#     person['dp'] = 'Yahoo'

print(person)

# Alternative to above
person.setdefault('dp', 'Yahoo')

print(person)

pprint.pprint(person)
