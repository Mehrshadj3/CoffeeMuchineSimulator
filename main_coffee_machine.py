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
coin = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01
}
drink = input("What would you like? (espresso/latte/cappuccino : ")

print("please insert coins.")
q = float(input("How many quarters: "))
d = float(input("How many dimes: "))
n = float(input("How many nickels: "))
p = float(input("How many pennies: "))

total = q * float(coin['quarter']) + d * float(coin['dime']) + n * float(coin['nickel']) + p * float(coin['penny'])


def stuff(espresso, latte, cappucciono):
    if drink == 'espresso':
        return resources['water'] - 50 and resources['coffee'] - 18
    elif drink == 'latte':
        return resources['water'] - 200 and resources['milk'] - 150 and resources['coffee'] - 24
    elif drink == 'cappuccino':
        return resources['water'] - 250 and resources['milk'] - 100 and resources['coffee'] - 24
    elif drink == 'report':
        print(resources)
        return


stuff('espresso', 'latte', 'cappuccino')

change = 0
if drink == 'espresso':
    change = total - int(MENU['espresso']["cost"])
elif drink == 'latte':
    change = total - int(MENU['latte']["cost"])
elif drink == 'cappuccino':
    change = total - int(MENU['cappuccino']["cost"])


if change >= 0:
    print(f"Here is ${change} in change.")
    print(f"Here is your {drink}. Enjoy!")
else:
    print("Sorry that's not enough money, coins refunded. ")



