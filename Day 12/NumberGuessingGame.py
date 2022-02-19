import random

logo="""
  ________                                ________                       
 /  _____/ __ __   ____   ______ ______  /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/ /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \  \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >  \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/          \/     \/      \/     \/ 
"""
easy = 10
hard = 5
NUMBER = random.randint(0,100)
print(logo)
def game(rep,NUMBER):
    i =0
    while i<rep:
        print(f"You have {rep-i} attempts remaining to guess the number.")
        guess=int(input("make a guess: "))
        if guess == NUMBER:
            print(f"You got it! The answer was {NUMBER}.")
            break
        elif guess > NUMBER:
            print("Too high.")
        else:
            print("Too low.")
        i+=1
        if i<rep:
            print("Guess again.")
        else:
            print("Tou've run out of guesses, you lose.")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    game(easy,NUMBER)
elif level =="hard":
    game(hard,NUMBER)