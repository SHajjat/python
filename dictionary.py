dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True,
    'y': 3
}
print(dictionary)
print(dictionary['a'][1])
print(dictionary.get('a')[1])

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True,
        'y': 3
    },
    {
        'a': [5, 6, 7],
        'b': 'hello',
        'x': True,
        'y': 3
    },
    {
        'a': [8, 8, 10],
        'b': 'hello',
        'x': True,
        'y': 3
    }
]

print(my_list[0]['a'][1])  # is this awesome  or what

# keys need to be immutable so it cant be array
my_F_dict = {
    123: [1, 2, 3],
    True: 'hello',

}

print(my_F_dict[123])
print(my_F_dict.get('age', 55))  # in case age doesnt exist return defult value 55
print(my_F_dict.get('age', 100))  # in case age doesnt exist rerun defult value 100
print(my_F_dict)

user2 = dict(name='jonjon')
print(user2)

print(123 in my_F_dict)
print('hello' in my_F_dict)

print('hello' in my_F_dict.values())
print(123 in my_F_dict.keys())
print(my_F_dict.items())
print(user2)
user2.clear()
print(user2)

my_F_dict.update({123:'dsadsad'})
my_F_dict.update({"hello":"samir"})  # if the key doesnt exist it will add the key
print(my_F_dict)
