# Day-18-Coffee-Machine
Your Coffee Machine - Difficulty: Easy
# CoffeeMachine

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/18

## License:
MIT License

## Dependencies:
None (built-in functions only)

## Description:
`coffeeMachine.py` is a simple Python script that simulates a coffee machine. The user can choose a coffee drink (espresso, latte, or cappuccino) and the program will check if there are enough resources to make the selected drink. If so, it will subtract the required ingredients from the available resources and serve the coffee. 

It also allows users to get a report of the current resources in the machine.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-2-Coffee-Machine.git
```
Navigate to the project directory:
```bash
cd Day-2-Coffee-Machine
```
Run the script:
```bash
python coffeeMachine.py
```
The script will prompt you to choose a coffee type or request a resource report. Based on your selection, it will process the request and update the resources accordingly.

## Example Output:
What would you like? (espresso/latte/cappuccino): espresso

Here is your espresso, enjoy!

or

What would you like? (espresso/latte/cappuccino): report

Current resource status:

water: 1000ml

milk: 500ml

coffee: 200g

## How it works:
The user selects a coffee drink (either espresso, latte, or cappuccino). The script checks if there are enough ingredients available (water, milk, coffee) to make the selected coffee. If the resources are sufficient, the program makes the coffee and updates the remaining resources. If not, it will notify the user of the insufficient ingredient.

The script also allows the user to check the current resource status by typing "report".

## License:
This project is licensed under the MIT License.
