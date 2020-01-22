# Raw strings
print(r"That's carols \tcat")

# multi-line string
print("""
This is
a 
multi-line
string
""")

# multi-line commments

"""
this is also considered as a multi-line comment
similar to multi-line strings
"""

# slicing and indexing
sentence = "It's a boy"
print(sentence[0:4])
print(sentence[4:])

# in substring
print('boy' in sentence)
print('boya' in sentence)

name = "Boy"
age = 32

print(name + " is " + str(32))

# similarly
print("%s's age is %d" % (name, age))
print(f"{name}s age is {age}")

# string methods
print(name.lower())
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.capitalize())

# isX methods
print("isalnum: " + str('hello'.isalnum()))
