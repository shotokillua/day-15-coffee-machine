MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
profit = float(0)
keep_running = True

def enough_water(drink):
    if water > water_left:
        print("Sorry there is not enough water.")
        return False
    else:
        return True

def enough_milk(drink):
    if milk > milk_left:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True

def enough_coffee(drink):
    if coffee > coffee_left:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True

def enough_money(total, cost):
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total >= cost:
        global profit
        profit += cost
        change = total - cost
        print(f"Here is ${format(change, '.2f')} in change.")
        return True

while keep_running == True:

    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the machine by entering "off" to the prompt
    if order == "off":
        keep_running = False
    elif order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    else:

    # TODO: 3. Print report of all coffee machine resources

        water = MENU[order]["ingredients"]["water"]
        milk = MENU[order]["ingredients"]["milk"]
        coffee = MENU[order]["ingredients"]["coffee"]
        cost = MENU[order]["cost"]

        water_left = resources["water"]
        milk_left = resources["milk"]
        coffee_left = resources["coffee"]

    # TODO: 4. Check resources sufficient?
        # Functions created above while loop
    # TODO: 5. Process coins

        if enough_water(order) == True and enough_milk(order) == True and enough_coffee(order) == True:
            print("Please insert your coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    # TODO 6. Check transaction successful?
        # Function created above while loop
    # TODO: 7. Make coffee
            if enough_money(total, cost) == True:
                resources["water"] -= water
                resources["milk"] -= milk
                resources["coffee"] -= coffee
                print(f"Here is your {order} ☕. Enjoy!")

