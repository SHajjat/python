# make a method that return the highest even number
def first_highest_ever(args):
    highest_even = 0
    for i in args:
        if i % 2 == 0 and i > highest_even:
            highest_even = i

    return highest_even


def second_highest_even(args):
    args.sort()
    for i in range(len(args)-1, 0, -1):
        if args[i] % 2 == 0:
            return args[i]

def third_highest_even(arg):
    evens=[]
    for i in arg:
        if i % 2 ==0:
            evens.append(i)
    return max(evens)


print(first_highest_ever([10,100,23,3241,432423,1,0,200]))
print(second_highest_even([10,100,23,3241,432423,1,0,200]))
print(third_highest_even([10,100,23,3241,432423,1,0,200]))