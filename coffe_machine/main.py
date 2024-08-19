from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
# menu_items = MenuItem
coffy_makker = CoffeeMaker()
money_machine = MoneyMachine()
is_on =True

"----------------------------------------------------------------"


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffy_makker.report()
    else:
        drink = menu.find_drink(choice)
        if coffy_makker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffy_makker.make_coffee(drink)



