import art
import data
import random
from os import system

print(art.logo)


def getguess():
    guess=random.choice(data.data)
    inde=data.data.index(guess)
    del data.data[inde]
    return guess
a=getguess()
score=0
play=True
while play:
    
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']} ")
    print(art.vs)
    b=getguess()
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']} ")
    res=input("Who has more followers, Type 'A' or 'B' : ").lower()
    if (res=="a" and a["follower_count"]>b["follower_count"]) or (res=="b" and a["follower_count"]<b["follower_count"]):
        score+=1
        system("cls")
        print(art.logo)
        print(f"You're right! Current score: {score}")
        if a["follower_count"]<b["follower_count"]:
            a=b
    else:
        system("cls")
        print(art.logo)
        print(f"Sorry , that's wrong. Final score: {score}")
        play=False
    if len(data.data)==0:
        print(f"No more Data. Final score: {score}")
    