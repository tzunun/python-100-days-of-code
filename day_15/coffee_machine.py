from random import randint
from random import shuffle
import string


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

def turn_off() -> None:
    print("Turning off the machine.")
    quit()


def print_greeting() -> str:
    # Use a breakpoint in the code line below to debug your script.
    return user_input
    
def process_payment(drink_cost: float, amount: dict) -> bool:

    payment_recieved = (amount['quarters'] * 25 + amount['dimes'] * 10 + amount['nickles'] * 5 + amount['pennies'])/100
    if payment_recieved >= drink_cost:
        print("Here is ${} in change.".format(payment_recieved - drink_cost))
        return True
    else:
        print("Payment is insufficient.")
        return False

def collect_payment(drink: str) -> dict:
    quarters = int(get_input("How many quaters? "))
    dimes = int(get_input("How many dimes? "))
    nickles = int(get_input("How many nickles? "))
    pennies = int(get_input("How many pennies? "))

    return {'quarters':quarters, 'dimes': dimes, 'nickles':nickles, 'pennies':pennies}


def make_drink(drink: str) -> None:
    global money

    if (check_resources(drink)):
        payment_amount = collect_payment(drink)
        drink_cost = MENU[drink]['cost']
        if(process_payment(drink_cost, payment_amount)):
            update_resources(drink)
            money += drink_cost

            print("Enjoy your {}".format(drink))

    pass


def print_report() -> None:
    for (ingredient, amount) in resources.items():
        print("{}: {}".format(ingredient, amount))
    print("Money: ${}".format(money))


def update_resources(drink: str) -> None:
    '''This function will subtract the drink's ingredients quantity from the resources
    
    Parameters
    __________
    drinK
        A string which is the key that will be used to get the ingredients
        quantity and subtract those from the available resources
    
    Returns
    _______
    None
    
    '''
    drink_ingredients = MENU[drink]['ingredients']

    for ingredient in resources:
        resources[ingredient] -= drink_ingredients[ingredient]


def check_resources(drink: str) -> bool:
    '''This function checks if there are enough resources to make the drink.

    Parameters
    ----------
    drink
        A string that will be used to identify the drink's ingredients amount.
    
    Returns
    -------
    bool
        True if there are enough resources to make the drink, False otherwise
    '''

    drink_ingredients = MENU[drink]['ingredients']
    for ingredient in resources:
        if (resources[ingredient] < drink_ingredients[ingredient]):
            print("Sorry there is not enough {}.".format(ingredient))
            return False
    return True


def get_input(desired_input: str) -> str:
    '''This function obtains the desired string input and performs data
    validation.

    Parameters
    ----------
    desired_input
        A string variable that will become part of the input requested from
        the user.

    Returns
    -------
    str
        The user's answer to the desired input.

    '''

    answer = ''

    while True:
        try:
            answer = input(desired_input)
        except ValueError:
            print("Sorry, I don't understand that.")
            continue
        else:
            return answer

if __name__ == "__main__":
    print("Coffee Machine Program.")

    while (True):
        user_input = get_input("What would you like? (espresso/latte/cappuccino):")
        if user_input == 'report':
            print_report()
        elif user_input == 'off':
            turn_off()
        else:
            make_drink(user_input)