# calorie_calculator.py

import sys
import argparse

# Dictionary to store calories of common ingredients
ingredient_calories = {
    "rice": 130,
    "chicken": 165,
    "broccoli": 55,
    "carrot": 41,
    "potato": 77,
    "cheese": 113,
    "tomato": 22,
    "bread": 79,
    "egg": 78,
    "milk": 42,
    "vegetable stock": 10  # Added calorie information for vegetable stock
}

def calculate_calories(dish):
    ingredients = dish.lower().split(", ")
    total_calories = 0
    for ingredient in ingredients:
        if ingredient in ingredient_calories:
            total_calories += ingredient_calories[ingredient]
        else:
            print(f"Calorie information for '{ingredient}' is not available.")
    return total_calories

def main():
    parser = argparse.ArgumentParser(description='Calorie Calculator')
    parser.add_argument('dish', type=str, help='Enter the ingredients of the dish separated by commas')
    args = parser.parse_args()

    total_calories = calculate_calories(args.dish)
    print(f"Total calories for the dish: {total_calories} kcal")

if __name__ == "__main__":
    main()
