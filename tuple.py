coordinents = (4, 5)  # immutable tuple cant be changed or modified
print(coordinents.__doc__)
# what are tuples
# they are immutable list
my_tuple =(1,2,3,4,5)
print(my_tuple[1])
print(my_tuple.count(5)) # this will count the characters or elements given
print(len(my_tuple))
print(5 in my_tuple)

listOfCords =[(1,2),(2,5),(332,32)]
print(listOfCords)

my_dic = {
    (1,2):["hello ","world"],
    "ahmad":"hello"
}

print(my_dic[(1,2)])


my_tuple = (1,2,3,4,5,5,6)
print(my_tuple.index(5,my_tuple.index(5)+1))
