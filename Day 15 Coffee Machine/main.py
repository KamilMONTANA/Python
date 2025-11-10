"""
TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.

TODO 3: Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

TODO 4: Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.

TODO 5: Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

TODO 6: Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.

TODO 7: Make coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""

import data

CoffeeMachine = True


def check_resources(drink):
    """Check if there are enough resources to make the drink."""
    for ingredient in data.MENU[drink]["ingredients"]:
        if data.MENU[drink]["ingredients"][ingredient] > data.resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def report():
    """Prints a report of the current resources."""
    print("\nCurrent resources:")
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Espresso: ${data.profit['espresso']:.2f}")
    print(f"Latte: ${data.profit['latte']:.2f}")
    print(f"Cappuccino: ${data.profit['cappuccino']:.2f}")


def process_coins():
    """Processes the coins inserted by the user."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def payment(drink):
    """Processes the payment for the drink."""
    cost = data.MENU[drink]["cost"]
    print(f"The cost of {drink} is ${cost:.2f}.")
    payment = process_coins()
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if "milk" in data.MENU[drink]["ingredients"]:
            data.resources["milk"] -= data.MENU[drink]["ingredients"]["milk"]
        if "water" in data.MENU[drink]["ingredients"]:
            data.resources["water"] -= data.MENU[drink]["ingredients"]["water"]
        if "coffee" in data.MENU[drink]["ingredients"]:
            data.resources["coffee"] -= data.MENU[drink]["ingredients"]["coffee"]

        change = round(payment - cost, 2)
        data.profit[drink] += cost
        print(f"\nHere is ${change:.2f} in change.")
        return True


while CoffeeMachine:
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if user_input == "espresso":
        if check_resources("espresso"):
            payment(user_input)
            print("\nHere is your espresso. Enjoy!")

    elif user_input == "latte":
        if check_resources("latte"):
            payment(user_input)
            print("\nHere is your latte. Enjoy!")

    elif user_input == "cappuccino":
        if check_resources("cappuccino"):
            payment(user_input)
            print("\nHere is your cappuccino. Enjoy!")

    elif user_input == "off":
        CoffeeMachine = False

    elif user_input == "report":
        report()

    else:
        print("Invalid input. Please try again.")
