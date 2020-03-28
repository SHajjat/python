
num1 = float( input('input the first number: ')) # you can use either int which will be integer or float
num2 = float(input('input the second number: '))
opration = input(' whats the operation you wanna do: ')

if opration == '*':
    print(num1*num2)
elif opration == '+':
    print(num2+num1)
elif opration == '/':
    print(num1/num2)
elif opration == '-':
    print(num1-num2)
else:
    print('Operation not found')

