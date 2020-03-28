for letter in "hello world":
    print(letter + "\n")

friends = ["John", "Josh", "Ahmad", "Samir"]
for word in friends:
    print(word)

for index in range(len(friends)):
    print(str(index) + " is the index of " + friends[index])

    users = {
        "name": "ahmad",
        "age": 30,
        "can_swim": True
    }

for key, value in users.items():
    print(key, value)

for item in users.items():
    print(item)
    key, value = item
    print(key, value)

for key in users.keys():
    print(key)
    print(users.get(key))

for value in users.values():
    print(value)
