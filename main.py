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
    "money": 0,
}


def print_report():
    for resource in resources:
        print(f"{resource.capitalize()}: {resources[resource]}")


def check_resources(order_item):
    """checks resources of ordered item in the coffee machine"""
    water = MENU[order_item]["ingredients"]["water"]
    coffee = MENU[order_item]["ingredients"]["coffee"]
    needed_items_values = [water, coffee]
    needed_items_names = ["water", "coffee"]

    if order_item != "espresso":
        milk = MENU[order_item]["ingredients"]["milk"]
        needed_items_values.insert(1, milk)
        needed_items_names.insert(1, "milk")

    for i in range(len(needed_items_values)):  # use range function
        if resources[needed_items_names[i]] < needed_items_values[i]:
            return False, f"Sorry there is not enough {needed_items_names[1]}."

    resources["water"] -= water
    resources["coffee"] -= coffee
    if order_item != "espresso":
        resources["milk"] -= milk

    return True, f"Here is your {order_item} ☕ Enjoy!"


def count_money(q, d, n, p, order_item):
    """count inserted coins"""
    price = MENU[order_item]["cost"]
    total = (q * .25) + (d * .1) + (n * .05) + (p * .01)
    refund = round(total - price, 2)
    if total < price:
        return False, "Sorry,that's not enough money. Money refunded."
    else:
        resources["money"] += price
        return True, f"Here is ${refund} in change."


def coffee_machine():
    """the main coffee machine program function"""
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        return
    elif order == "report":
        print_report()
        coffee_machine()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        resources_update = check_resources(order_item=order)
        if not resources_update[0]:
            print(resources_update[1])
            # return
            coffee_machine()
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?:"))
            dimes = int(input("How many dimes?:"))
            nickles = int(input("How many nickles?:"))
            pennies = int(input("How many pennies?:"))
            account = count_money(q=quarters, d=dimes, n=nickles, p=pennies, order_item=order)
            if not account[0]:
                print(account[1])
                #                 return
                coffee_machine()
            else:
                print(account[1])
                print(resources_update[1])
            coffee_machine()
    else:
        print("Please enter coffee name properly.")
        coffee_machine()


coffee_machine()
