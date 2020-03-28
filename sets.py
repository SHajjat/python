

my_set = {1,2,3,4,5,6,6,6,6,6,6,6,6,6,6}
print(my_set)
print(my_set.add(8))
print(my_set)

my_list = [1,2,3,4,5,6,6,6,6,6,6,6,6,6,6]
my_new_set = set(my_list)
print(my_new_set)
print( 1 in my_new_set)
my_list = list(my_new_set)

print(type(my_new_set))


#Set methods

my_set = {1,2,3,4,5}
your_set ={3,4,5,6,7,8,9,10}

print(my_set.difference(your_set)) # it will find the difference between my set and your set

print(my_set.discard(5)) # remove the element if it is in there
print(my_set) # 5 is removed
my_set.difference_update(your_set) # will modify my set to remove what is common between the two so it will return whats only in myset

print(my_set.intersection(your_set)) # it will return whats in both sets you can also use & will give you the same
print(my_set & your_set) # it will return whats in both sets you can also use & will give you the same
print(my_set.isdisjoint(your_set)) # as if those two sets have anything in common retrn true or false

print(my_set.union(your_set)) # this will union both just like sql , return new set with unrepeted values from both same thing with |
print(my_set | (your_set)) # this will union both just like sql , return new set with unrepeted values from both

print(my_set.issubset(your_set)) # im asking is all elements in myset contained in your set ???