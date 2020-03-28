
number_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid)
print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)


def translater(word):
    word =str(word.translate(word.maketrans({"A":"itsA","B":"itsAB"})))
    return word

word ="AAABB"
print(translater(word))

def enhanc_translator(word):
    word = str(word)
    translat =""
    for letter in word :
        if letter in "AaEeOoUu":
            translat+="GoooooGle"
        else:
            translat+=letter
    return translat

print(enhanc_translator(word))




