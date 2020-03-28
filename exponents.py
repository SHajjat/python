
# you can use 2**3 which is 2^3

def raise_to_power(base_num ,power_num):
    result =1
    for i in range(power_num):
        result=result*base_num
    return result


print(raise_to_power(10,10))
print(pow(10,10))