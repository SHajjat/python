#Exercise
import  numpy as np
picture =[
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

new_picture=[]


for i,row in enumerate(picture):
    for j,col in enumerate(row):
        if col==0:
            picture[i][j]=" "
            print(end=" ")
        elif col == 1:
            picture[i][j]="*"
            print("*",end="")
    print()

print()
matrx =np.array(picture)
print(matrx)