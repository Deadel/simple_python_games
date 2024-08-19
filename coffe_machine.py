MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def report():
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}')


def check_suply(user_choose):
    for ingredient in MENU[user_choose]["ingredients"]:
        if MENU[user_choose]["ingredients"][ingredient] > resources[ingredient]:
            print(f"“Sorry there is not enough {ingredient}.")
        #     return 1
        # print(MENU[user_choose]["ingredients"][ingredient])


def coins(user_choose):
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickles = int(input("Insert nickles: "))
    pennies = int(input("Insert pennies: "))
    try:
        suma = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
        print(suma)
    except:
        print("This is no money")
    if suma > MENU[user_choose]["cost"]:
        change = float(suma - MENU[user_choose]["cost"])
        print(f"Here is ${change:.2f} dollars in change.")
        print(f"Here is your {user_choose}. Enjoy!")
        return MENU[user_choose]["cost"]
    elif suma == MENU[user_choose]["cost"]:
        print(f"Here is your {user_choose}. Enjoy!")
        return MENU[user_choose]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


working = True


while working:
    user_choose = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choose in ["espresso", "latte", "cappuccino"]:
        check_suply(user_choose)
        money = coins(user_choose)
        for ingredient in MENU[user_choose]["ingredients"]:
            resources[ingredient] -= MENU[user_choose]["ingredients"][ingredient]
    elif user_choose == "report":
        report()
    elif user_choose == "off":
        working = False
    else:
        pass




