
from math import *

print('hello')
myname = 'samir hajjat'
print(myname.upper())
print(myname.upper().isupper())
print(myname.lower())
print(myname.lower().islower())
print(myname.capitalize()) # make the first letter capital
print(myname[1])
for i in range(len(myname)):
    print(myname[i])

print(myname.center(5, 's'))
print(myname.endswith('f'))
print(myname.startswith('s'))
print(myname.startswith('S'))
for i in range(len(myname)):
    print(myname[-(i + 1)])

print(myname.index('s'))
#print(str.index('SAmir'))  if the index is not found it will throw an exception
print(myname.replace('a', 'hello')) # replace all instances of the char

# to convert a number to a string
num = 1
print(str(num) + 'String')
print(abs(-5)) #abs value
print(pow(5,2))
print(max(5,7))
print(min(5,4))
print(round(3.533))

# those come from Math package
print(floor(3.444))
print(ceil(3.444))
print(sqrt(4))

# input
name =input('enter your name: ')
age = input('how old are you ')
print('hello '+name)
print('you age is '+ age)
