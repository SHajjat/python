# soooo this is super intersing
#lets say you want to create a list of chars
#instead of doing
def chars(word):
    my_list =[]
    for char in word:
        my_list.append(char)
    return my_list


print(chars("hello world"))

#you can do my_list =[param for param in iterable]

my_list2 =[char for char in "hello world"]  # duuuuddee this is amazing
print(my_list2)
my_list3 = [num for num in range(101)]
print(my_list3)

my_list4 = [num*2 for num in range(101)]
print(my_list4)

my_list5 = [num**2 for num in range(0,101,2)]
print(my_list5)

my_list6 =[num**2 for num in range(101) if not num%2]
print(my_list6)


#Set comprehention
print("Sets")
my_set1 ={char for char in "hello world"} # duuuuddee this is amazing
print(my_set1)
my_set2 = {num for num in range(101)}
print(my_set2)

my_set3 = {num*2 for num in range(101)}
print(my_set3)


#dics its used to perfome actions on the dic
print("dics")
simple_dic ={
    "a":1,
    "b":2,
    "c":3,
    "d":4
}
my_dic1 ={key:value**2 for key,value in simple_dic.items()}
print(my_dic1)

my_dic2 ={key:value**2 for key,value in simple_dic.items() if key == "c"} # only c is added to the dic
print(my_dic2)

my_dic3 ={num:num*2 for num in [1,2,3,4,5,6,7]}
print(my_dic3)

my_list =['a','b','c','b','d','m','n','n']

my_duplicate_list =[char for char in my_list if my_list.count(char) >1]
print(list(set(my_duplicate_list)))

