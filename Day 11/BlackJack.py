from audioop import add
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user=[]
dealer=[]

def getCard():
    card = random.choice(cards)
    i= cards.index(card)
    del cards[i]
    return card
def score(list):
    score=0
    for l in list:
        score+=l
    return score
def lose():
    print("You lose !")
def addcard(list):
    list.append(getCard())
def continueplaying(user,dealer,userScore,dealerScore):
    anotherCard=input("You want another card? Type 'y' if yes or 'n' if not: ").lower()
    if anotherCard=="y":
        addcard(user)
        userScore=score(user)
        print(f"user: {userScore}")
        play(user,dealer,userScore,dealerScore)
    else:
        if dealerScore<17:
            addcard(dealer)
            dealerScore=score(dealer)
        if dealerScore >21:
            print(f"userScore: {userScore} card: {user}")
            print(f"dealerScore : {dealerScore} card: {dealer}")
            print("You win !")
        else:
            if dealerScore==userScore:
                print(f"userScore: {userScore} card: {user}")
                print(f"dealerScore : {dealerScore} card: {dealer}")
                print("Draw !")
            elif dealerScore > userScore:
                print(f"userScore: {userScore} card: {user}")
                print(f"dealerScore : {dealerScore} card: {dealer}")
                lose()
            else:
                print(f"userScore: {userScore} card: {user}")
                print(f"dealerScore : {dealerScore} card: {dealer}")
                print("You win !")

    

addcard(user)
addcard(dealer)
addcard(user)
addcard(dealer)


userScore=score(user)
dealerScore=score(dealer)

print(f"user: {user}")
print(f"dealer : {dealer[0]} ")

def play(user,dealer,userScore,dealerScore):
    if userScore==21:
        print("You win !")
    elif dealerScore==21:
        lose()
    elif userScore>21:
        haveAce= input("Do you have an Ace ? Type 'y' if yes or 'n' if not: " ).lower()
        if haveAce=="y":
            stillOver =input("If the ace counts as a 1 instead of 11, are they still over 21? Type 'y' if yes or 'n' if not: ").lower()
            if stillOver=="y":
                lose()
            else:
                continueplaying(user,dealer,userScore,dealerScore)
        else:
            lose()

    else:
        continueplaying(user,dealer,userScore,dealerScore)

play(user,dealer,userScore,dealerScore)