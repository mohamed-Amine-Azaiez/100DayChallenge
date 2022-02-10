import random
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game=[Rock,Paper,Scissors]

client = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
comp=random.randint(0,2)

print(game[client])
print("Computer chose: \n"+game[comp])

if client==comp:
    print("DRAW")
elif (client==0 and comp==2) or (client==1 and comp==0) or (client==2 and comp==1):
    print("You win!")
else:
    print("You lose!")



