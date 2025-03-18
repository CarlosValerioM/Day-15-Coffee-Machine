#!/usr/bin/env python3
"""
coffeeMachine.py - A simple coffee machine simulator.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/18
License: MIT
Dependencies: None (built-in functions only)

Description:
This script simulates a coffee machine that can make different coffee drinks (espresso, latte, cappuccino)
based on the available resources. The user can:
1. Choose a coffee drink.
2. Get a report of the current resources.
3. Check if there are enough resources to make the selected coffee.
4. Deduct the required ingredients after making a coffee.

Usage:
Run the script and follow the prompts:
    python coffeeMachine.py

Example Output:
    What would you like? (espresso/latte/cappuccino): espresso
    Here is your espresso, enjoy!
"""

from menu import MENU  # Import the menu dictionary from the menu module
from resources import RESOURCES  # Import the resources dictionary from the resources module


def make_coffee(menu, resources, option):
    """
    This function checks if there are enough resources to make the selected coffee,
    and then deducts the used ingredients from the available resources.
    """
    # Check if there are enough resources for the selected coffee
    for ingredient, quantity in menu[option]["ingredients"].items():
        if resources[ingredient][0] < quantity:
            print(f"There is not enough {ingredient} to make {option}.")
            return 0  # Return 0 if there aren't enough resources

    # If there are enough resources, make the coffee and update the available resources
    print(f"Here is your {option}, enjoy!")

    # Deduct the used quantity from the available resources
    for ingredient, quantity in menu[option]["ingredients"].items():
        resources[ingredient][0] -= quantity  # Subtract the used quantity from the available resource

    return 1  # Return 1 to indicate the coffee was successfully made


def main():
    """
    Main function to start the program, prompt the user for a coffee option,
    and display resources or make coffee based on user input.
    """
    resources = RESOURCES  # Initialize resources from the imported dictionary
    menu = MENU  # Initialize menu from the imported dictionary
    active = True  # Control the loop to keep the program running

    while active:
        # Ask the user for their coffee choice
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Handle the "report" option to show the current resource status
        if option == "report":
            print("Current resource status:")
            for ingredient, (quantity, unit) in resources.items():
                print(f"{ingredient}: {quantity}{unit}")

        # Handle the case when a valid coffee option is chosen
        elif option in menu:
            make_coffee(menu, resources, option)  # Make the coffee based on user choice
        else:
            print("Invalid option, please choose from espresso, latte, or cappuccino.")


if __name__ == '__main__':
    main()  # Run the program when executed