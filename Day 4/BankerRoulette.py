import random

test_seed=int(input("Create a seed number: "))
random.seed(test_seed)

names=input("Give me everybody's names, seperated with a comma.\n").split(", ")
nb=len(names)

randomnb= random.randint(0,nb-1)
print(names[randomnb] + " is going to pay the meal today !")
