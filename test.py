fruits = [
    "apple",
    "banana",
    "orange",
    "mango",
    "grape",
    "pineapple",
    "strawberry",
    "blueberry",
    "watermelon",
    "kiwi",
    "peach"
]

print("List of fruits:", fruits)
print('---------------------')

for i in fruits:
    print(i)

print('---------------------')

cab = [n.upper() for n in fruits]
for i in cab:
    print(i)