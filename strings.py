# sooooo appearantly you can format a string , what you do is add f at the beginning and put the variables name
# inside the string in {}
#Strings are immutable so you cant change one char at one time
name = "samir"
age = 5

print("hello "+name+ "!!! you are "+str(age)+" years old")
# or we can do

print(f"hello {name}!!! you are {age} years old")

# or you can do this
print("hello {}!!! you are {} years old".format(name,age))

#or this

print("hello {1}!!! you are {0} years old".format(name,age))

# or this
print("hello {formated_name}!!! you are {formated_age} years old".format(formated_name = name,formated_age=age))


selfiesh = "1234567890"
# string[start:stop:stepover]
print(selfiesh.index("67"))
print(selfiesh[3:5])
print(selfiesh[5:2:-1])

quote ="to be or not to be "
print(quote.find("to",2))
print(quote.find("hello"))  # it will return -1 if its not there 