
is_male =False
tale =True

if is_male or tale:
    print("you are Male")
else:
    print("you are Female")

if is_male and tale:
    print("you are Male")
else:
    print("you are Female")

if not is_male :
    print("you are Female")
else:
    print("you are Male")


if is_male and tale:
    print("you are short male")
elif is_male and not tale:
    print("you are short male")
elif not is_male and tale:
    print("you are Tale female")
elif not is_male and not tale:
    print("you are short female")