
from  Student import Student

student1 = Student("Ahmad","python",3.1,False)
print(student1.name)
print(student1.major)

student2 =Student("Pam","Mozeh",666,True)
print(student2.major)
student2.age =5
print(student2.age)
print(student1.on_honer_role())
print(student2.on_honer_role())