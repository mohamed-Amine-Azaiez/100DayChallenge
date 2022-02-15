from os import system
import art
#system('cls')

print(art.logo)
print("Welcome to The secret auction program.")

players={}


newplayer=True

while newplayer:
    name=input("what is your name?: ")
    bid=int(input("what is your bid?: $"))
    players[name]=bid

    another_bidder=input("Are there any other bidders? type 'yes' or 'no': ").lower()
    if another_bidder !="yes":
        newplayer=False
    else:
        system("cls")

system("cls")
winner=""
val=0
for player in players:
    if players[player]>val:
        winner=player
        val=players[player]
print(f"The Winner is {winner} with a bid of ${val}")
    