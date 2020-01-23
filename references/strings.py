import pyperclip

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
print("isalnum: " + str('hello123'.isalnum()))
print("isalpha: " + str('hello'.isalpha()))
print("isdecimal: " + str('1233'.isdecimal()))  # DECIMAL
print("istitle: " + str('Abc'.istitle()))

print("hello world".startswith("hello"))
print("hello World".lower().endswith("world"))

csv_str = "apples,oranges,bananas"
csv_list = csv_str.split(',')
print(csv_list)
csv_str_conv = ','.join(csv_list)
print(csv_str_conv)

if csv_str_conv == csv_str:
    print("Same")

print(csv_str.partition(','))  # Same with join, but only with the first occurrence

# Justifying text
print('Hello'.rjust(20, '='))
print('Hello'.ljust(20, '='))
print('Hello'.center(20, '='))

items = {
    "apples": 6.78,
    "oranges": 1.23,
    "bananas": 2.29
}


def print_receipt_items(receipt_items):
    print("Resibo:")
    for k, v in receipt_items.items():
        print("{}{}".format(k.ljust(10, '.'), str(v).rjust(10, '.')))


print_receipt_items(items)

# trim
print(" hello".lstrip())
print(" hello ".rstrip())
print(" hello ".strip())

print(ord('A'))  # ASCII # Letters to numbers
print(chr(65))  # numbers to characters

# pyperclip.copy('Hello, world!')
pyperclip.paste()
