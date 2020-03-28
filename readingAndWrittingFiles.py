
import numpy as np

playa =open("playa.txt","r") # this mean read
playaAgain = open("playa.txt","a") # append to the file and add new line , if i was using int i would add \n
ListOfplayers= open("thislistOfPlayers.txt","w") # create a new file and add to it
# open("/Users/samirhajjat/Desktop/pythonProject/P4-Demographic-Data.csv","w") # this mean write
# open("/Users/samirhajjat/Desktop/pythonProject/P4-Demographic-Data.csv","a") # this mean append , you can modify you cant change but you can add more information

print(playa.readable()) # this tells me if i can read it or not if you put r it will be true if w it will be false
print(playa.readline())
# print(demographics.readline())
print(playa.readlines())
print("______")
playa.close() # with this method i think you have to close it to go back ontop
playa = open("playa.txt","r")

for line in playa.readlines():
    playaAgain.write(line)
    ListOfplayers.write(line)

playaAgain.close()
playa.close()
ListOfplayers.close()
#when you open a file you need to close it

