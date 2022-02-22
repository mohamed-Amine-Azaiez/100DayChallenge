from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mymenu=Menu()
mycoffeeMaker=CoffeeMaker()
mymoneyMachine=MoneyMachine()


while True:
    serve=input(f"What would you like? ({mymenu.get_items()}) :").lower()
    if serve == "report":
        mycoffeeMaker.report()
        mymoneyMachine.report()
    elif serve=="off":
        break
    else:
        drink=mymenu.find_drink(serve)
        if drink==False:
            print("Sorry that item is not available.")
        elif mycoffeeMaker.is_resource_sufficient(drink):
            if mymoneyMachine.make_payment(drink.cost):
                mycoffeeMaker.make_coffee(drink)
            
            