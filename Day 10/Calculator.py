from os import system
logo="""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}
print(logo)
num1=float(input("What's the first number? "))
for key in operations:
    print(key)


rep=True
while rep:
    operation_symbol=input("Pick an operation: ")
    num2=float(input("What's the second number? "))
    calculation_function = operations[operation_symbol]
    result=calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    again=input(f"Type 'y' to continue calculation with {result} or Type 'n' to start a new calculation: ")
    if again =="y":
        num1=result
    elif again=="n":
        system("cls")
        print(logo)
        num1=float(input("What's the first number? "))
    else:
        rep=False



