# *args you can pass varargs
# **kwargs you can add key value pair

#IMORTANT
# Rule : params , *args,default parameters , **kwargs
def super_fun(*args):
    print(*args)
    return sum(args)

def another_super_fun(*args,**keyargs):

    return sum(args)+sum(keyargs.values())

def last_super_fun(*args,**keyargs):

    return sum(args)+sum(keyargs.values())

print(super_fun(1,2,3,4,5,6,7,8))
print(another_super_fun(1,2,3,4,5,6,7,8,num1 =5,num2=10,num3=100))