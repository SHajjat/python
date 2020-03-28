

def find_duplicates(my_list):
    returned_list=[]
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i]==my_list[j] and my_list[i] not in returned_list:
                returned_list.append(my_list[i])

    return  returned_list


my_test_list =['f','a','b','c','b','d','m','n','n','a']
print(find_duplicates(my_test_list))



#another solution
def yet_again_another_method(my_list):
    list(my_list)
    returned_list =[]
    for value in my_list:
        if my_list.count(value) > 1 and value not in returned_list:
            returned_list.append(value)
    return returned_list

print(yet_again_another_method(my_test_list))