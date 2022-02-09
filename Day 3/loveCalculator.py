print("Welcome to the Love Calculator!")
name1=input("What is Your Name? \n")
name2=input("What is their Name? \n")

name1=name1.lower()
name2=name2.lower()

nbtrue = 0
nbtrue+=name1.count("t") + name2.count("t")
nbtrue+=name1.count("r") + name2.count("r")
nbtrue+=name1.count("u") + name2.count("u")
nbtrue+=name1.count("e") + name2.count("e")

nblove=0
nblove+=name1.count("l") + name2.count("l")
nblove+=name1.count("o") + name2.count("o")
nblove+=name1.count("v") + name2.count("v")
nblove+=name1.count("e") + name2.count("e")
score=str(nbtrue)+str(nblove)

lovescore = int(score)

if lovescore<10 or lovescore>90:
    print(f"Your Score is {lovescore}%, you go together like coke and mentos.")
elif lovescore>=40 and lovescore<=50:
    print(f"Your Score is {lovescore}%, you are alright together.")
else:
    print(f"Your Score is {lovescore}%")