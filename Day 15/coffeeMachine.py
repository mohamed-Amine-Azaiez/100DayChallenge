import menu


water=menu.resources['water']
milk=menu.resources['milk']
coffee=menu.resources['coffee']
money=0
def report():
    print(f"water: {water}ml")
    print(f"milk: {milk}ml")
    print(f"coffee: {coffee}g")
    print(f"money: ${money}")
def espresso():
    eswater=menu.MENU['espresso']['ingredients']['water']
    escoffee=menu.MENU['espresso']['ingredients']['coffee']
    esprice=menu.MENU['espresso']['cost']
    if eswater>water:
        print("Sorry there is not enough water.")
    elif escoffee>coffee:
        print("Sorry there is not enough coffee")
    else:
        coins(esprice, "espresso",eswater,0,escoffee)





def latte():
    latwater=menu.MENU['latte']['ingredients']['water']
    latcoffee=menu.MENU['latte']['ingredients']['coffee']
    latmilk=menu.MENU['latte']['ingredients']['milk']
    latprice=menu.MENU['latte']['cost']
    if latwater>water:
        print("Sorry there is not enough water.")
    elif latcoffee>coffee:
        print("Sorry there is not enough coffee")
    elif latmilk>milk:
        print("Sorry there is not enough milk")
    else:
        coins(latprice,"latte",latwater,latmilk,latcoffee)



def cappuccino():
    capwater=menu.MENU['cappuccino']['ingredients']['water']
    capcoffee=menu.MENU['cappuccino']['ingredients']['coffee']
    capmilk=menu.MENU['cappuccino']['ingredients']['milk']
    capprice=menu.MENU['cappuccino']['cost']
    if capwater>water:
        print("Sorry there is not enough water.")
    elif capcoffee>coffee:
        print("Sorry there is not enough coffee")
    elif capmilk>milk:
        print("Sorry there is not enough milk")
    else:
        coins(capprice, "cappuccino",capwater,capmilk,capcoffee)


def coins(price,type,upwater,upmilk,upcoffee):
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    totalInsert=(quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    if totalInsert<price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change=totalInsert-price
        change=round(change, 2)
        if change >0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {type} ☕ Enjoy! ")
        update(upwater,upmilk,upcoffee,price)

def update(upwater,upmilk,upcoffee,upmoney):
    global water
    global milk
    global coffee
    global money
    water-=upwater
    milk-=upmilk
    coffee-=upcoffee
    money+=upmoney


while True:
    serve=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if serve == "report":
        report()
    elif serve=="espresso":
        espresso()
    elif serve=="latte":
        latte()
    elif serve=="cappuccino":
        cappuccino()
    elif serve=="off":
        break
