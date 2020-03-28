#map , filter zip and reduce

# map takes a function and takes itrable like list and perform that function
#map is pure function
# pure function is function that doesnt change outside world which mean it will not change the original list

def multiply_by2(list):
    new_list = []
    for i in list:
        new_list.append(i*2)
    return new_list

my_list = [1,2,3,4,5]
print(multiply_by2(my_list))

def mapped_multiply_by2(item_in_list):
    return item_in_list*2

print(map(mapped_multiply_by2,my_list)) # this take every element in my_list and run it through the function and return list of them all
print(list(map(mapped_multiply_by2,my_list))) # you need to change it to list to see items


#filter it takes true or false , if its true it keeps the item

def odd(item):
    return item % 2 # if its odd it get nonzero number which is true

print(list(filter(odd,my_list)))

my_list = [1,2,3,4,5]
your_list = [10,20,30,40]

#zip it takes two or more lists and take the first item and add it to tuple and second and add them to tuple
#if one list is shorter than the other extra items are ignored


print(list(zip(my_list,your_list)))  # [(1, 10), (2, 20), (3, 30), (4, 40)]


#reduceeeee
from functools import  reduce

def accumulator(accumalate,item):
    print(accumalate,item)
    return accumalate+item

print(reduce(accumulator,my_list,0))

