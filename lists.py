
friends =["Rose","Rachel","Monica","Chandler","Joe"]
print(type(friends))

for i in range(len(friends)):
    print(friends[i])

print(friends[::-1])
print(friends[2::-1])
friends.append("Samir")
print(friends)
myfriends = friends.copy()
myfriends1 = friends
myfriends1[0]="Samir"
print(myfriends1)
print(friends)
friends.extend(friends) # you add another list to the list (add two lists together
print(friends)
friends.insert(1,"Kelly")
print(friends)
friends.remove("Samir")
print(friends)
print(friends.pop()) # remove the last element and return it
print(friends)
print(friends.index("Samir"))
print(friends.count("Samir"))
friends.sort()
print(friends)
friends.reverse()
print(friends)

# list methods
basket =[1,2,3,4,5]

#adding
basket.append(6)
basket.insert(200000,20) # modifies the list
basket.extend([100,101])
name =basket.pop()
print(basket)
print(name)
name =basket.pop(0)
print(name)
print(basket)
basket.remove(4)
print(basket)
basket.clear()
print(basket)

#######
basket = ["a","b","c","d"]
print(basket.index("b"))
print(basket.reverse())
print(basket)

print('x' in basket) # you can also do it in string
print("samir" in "hey samir" )
print(basket.count("a"))
print("hey i love a good  samir".count("o"))
print(basket.sort() ) # sort the list
print(basket)
basket.reverse()
print(basket)

print(sorted(basket))
print(basket)

# join
sentence=''
new_sentense =sentence.join(['hi ','my ',' name ',' is ',' jojo']) # join list to a string
print(sentence)
print(new_sentense)

# unpacking

a,b,c=[1,2,3]

print(a)
print(b)
print(c)

a , b , c  , *otheritems , d =[1,2,3,4,5,6,7,8]

print(a)
print(b)
print(c)
print(otheritems) # this will be a list
print(d)


