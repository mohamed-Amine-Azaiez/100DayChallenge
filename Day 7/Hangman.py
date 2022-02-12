from os import system
import random
import hangman_arts
import hangman_words

print(hangman_arts.logo)

lives=6
chosen_word=random.choice(hangman_words.word_list)
display=[]


for i in range(0,len(chosen_word)):
    display.append("_")

gameOver=False
while not gameOver:
    guess=input("Guess a letter: ").lower()
    system('cls')
    if guess in display:
        print(f"You've already gessed {guess}")
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess==chosen_word[i]:
                display[i]=guess
        print(display)
        print(hangman_arts.stages[lives])
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(display)
        lives-=1
        print(hangman_arts.stages[lives])
    if lives ==0:
        gameOver=True
        print("You lose !")
    if not ("_" in display):
        gameOver=True
        print("You win!")
    
