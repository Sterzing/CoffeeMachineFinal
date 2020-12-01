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
profit = 0
is_on = True


def ingredient_check(drink):
    for item in ingredients_amount:
        if resources[item] < ingredients_amount[item]:
            print(f"Sorry, we're out of {item}.")
            return False
        else:
            return True


def calculate_money():
    print("Please insert coins:")
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .1
    total += int(input("How many nickels? ")) * .05
    total += int(input("How many pennies? ")) * .01
    return total


def confirm_payment(payment, cost):
    if payment >= cost:
        print(f"Here is your ${payment - cost} in change!")
        return True
    else:
        print("Sorry, that's not enough money")
        return False

def subtract_resources(drink):
    for item in ingredients_amount:
        resources[item] -= ingredients_amount[item]


while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        ingredients_amount = MENU[order]["ingredients"]
        if ingredient_check(order):
            if confirm_payment(calculate_money(), MENU[order]["cost"]):
                profit += MENU[order]["cost"]
                subtract_resources(order)
                print(f"Enjoy your {order}!")





