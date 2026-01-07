from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    answer = input(f"What would you like? ({menu.get_items()}) ")
    drink = menu.find_drink(answer)

    if answer == "off":
        break

    if answer == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
