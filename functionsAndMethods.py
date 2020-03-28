#parameters
def say_hello(name,emoji):
    print(f"hello {name} {emoji}")



#positional arguments
say_hello("Samir","😁")
say_hello("Ahmed","😁")
say_hello("Musa","😁")

#key word argument
say_hello(emoji="😁",name="Samir")



def say_hey(name="darth Vader",emoji="💩"):
    print(f"hey {name} {emoji}")


say_hey()
say_hey("Harini")