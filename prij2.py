import os
import random 
from builtins import input

def wordgenerator():
    with open("wordd.txt","r") as wo:
        words=wo.readlines()    
        w=words[random.randint(0,len(words))]    
        v=w.split()
        return (v[0])
def printer(l):
    for i in range(len(l)):
        print(l[i],end=" ")
    print()
def handman(tries):
    arr = [[" "," ","O"],["\n","--"],["|"],["--","\n"],["  ","|"],["\n"," ","/"],[" ","\\"],[""]]
    for i in range(tries):
        for j in range(len(arr[i])):
            print(arr[i][j],end="")
word=wordgenerator()
tries=0
chances=8
l=["_" for i in range (len(word))]
printer(l)
g=set()

while tries<chances:
    guess=input("guess the word")
    g.add(guess)
    os.system("cls")
    if len(g)>0:
        for i in g:
            print(f"({i})",end="")
    print("\n")

    if guess in word:
        index=[i for i,v in enumerate(word) if v==guess]
        for i in index:
            l[i]=guess.upper()
        handman(tries)
        print()
        print()
        printer(l)
    if guess not in word:
        tries+=1
        handman(tries)
        print()
        print()
        printer(l)
    if tries ==chances-1:
        print(f"you cant save me,actual worf was {word}")
        break
    if word.upper()=="".join(l):
        print("yes you saved me ")
        break
    

           
