print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the Treasure !")
option1=input("You're at a cross road. Where do you want to go? Right or left ?  ").lower()
if option1=="left":
    option2=input("You come to a lake. There is an islan in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.  ").lower()
    if option2 =="wait":
        option3=input("You arrive at the islan unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?  ").lower()
        if option3=="yellow":
            print("You found the treasure!You Win !")
        elif option3=="blue":
            print("You enter a room of beasts. Game Over")
        elif option3=="red":
            print("You enter a room full of fire. Game Over")
        else:
            print("Game Over")
    else:
        print("You got attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over")