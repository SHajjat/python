# 1. start with local scope
# 2. then parent scope
# 3. then global scope (what ever the file have)
# 4. built in python functions
a = 1


def test():
    # a = a+1
    print(a)
test()



def parent():
    a = 10

    def confustion():
        return a

    return confustion()


print(parent())


total =0

def count():
    global total
    total+=1
    return total

print(count())
print(count())
print(count())



#nonLocal
# its a way to get the parent variable

def outer():
    x= "local"
    def inner():
        # nonlocal x
        x = "nonlocle"
        print("inner",x)

    inner()
    print("outter", x)


outer()