

def recur():
    try:

         number = int(input("enter a number "))
         print(number)
    except  ValueError as err:
         print(err)
         print("enter a number dumb ass")
         recur()
    finally:
        print("finally you are done")


recur()