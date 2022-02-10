import random

test_seed=int(input("Create a seed number: "))
random.seed(test_seed)

names=input("Give me everybody's names, seperated with a comma.\n").split(", ")
print(random.choice(names) + " is going to pay the meal today !")
