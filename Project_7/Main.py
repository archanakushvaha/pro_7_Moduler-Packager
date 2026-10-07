import Calculator
import Converter
import random_utils
import file_menu as file
from packger import math_utils


def main():
    while True:
        
        print("1. Calculator")
        print("2. Converter")
        print("3. Random Utilities")
        print("4. File Operations")
        print("5. Mathematical Utilities")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Calculator ---")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Logarithm")

            option = input("Enter your option: ")

            a = float(input("Enter first number: "))

            if option != "5":
                b = float(input("Enter second number: "))

            if option == "1":
                print("Result:", Calculator.addition(a, b))

            elif option == "2":
                print("Result:", Calculator.subtraction(a, b))

            elif option == "3":
                print("Result:", calculator.multiplication(a, b))

            elif option == "4":
                print("Result:", Calculator.division(a, b))

            elif option == "5":
                base = float(input("Enter base: "))
                print("Result:", Calculator.logarithm(a, base))

            else:
                print("Invalid option.")

        elif choice == "2":
            print("\n--- Converter ---")
            print("1. Kilometer to Meter")
            print("2. Meter to Kilometer")
            print("3. Celsius to Fahrenheit")
            print("4. Fahrenheit to Celsius")
            print("5. Kilogram to Gram")
            print("6. Gram to Kilogram")

            option = input("Enter your option: ")

            value = float(input("Enter value: "))

            if option == "1":
                print("Result:", Converter.km_to_meter(value))

            elif option == "2":
                print("Result:", Converter.meter_to_km(value))

            elif option == "3":
                print("Result:", Converter.celsius_to_fahrenheit(value))

            elif option == "4":
                print("Result:", Converter.fahrenheit_to_celsius(value))

            elif option == "5":
                print("Result:", Converter.kg_to_gram(value))

            elif option == "6":
                print("Result:", Converter.gram_to_kg(value))

            else:
                print("Invalid option.")

        elif choice == "3":
            print("\n--- Random Utilities ---")
            print("1. Random Number")
            print("2. Dataset Sampling")
            print("3. Game Simulation")

            option = input("Enter your option: ")

            if option == "1":
                print("Random Number:", random_utils.random_number())

            elif option == "2":
                data = ["Python", "Java", "C++", "SQL", "Pandas"]
                count = int(input("How many items do you want? "))

                print("Sample:",random_utils.dataset_sampling(data, count))

            elif option == "3":
                random_utils.game_simulation()

            else:
                print("Invalid option.")

        elif choice == "4":
            file.file_menu()

        elif choice == "5":
            print("\n--- Mathematical Utilities ---")
            print("1. Square Root")
            print("2. Power")
            print("3. Factorial")
            print("4. Percentage")
            print("5. Circle Area")

            option = input("Enter your option: ")

            if option == "1":
                number = float(input("Enter number: "))
                print("Result:", math_utils.square_root(number))

            elif option == "2":
                number = float(input("Enter number: "))
                exponent = float(input("Enter exponent: "))

                print("Result:",math_utils.power(number, exponent))

            elif option == "3":
                number = int(input("Enter number: "))
                print("Result:", math_utils.factorial(number))

            elif option == "4":
                number = float(input("Enter number: "))
                percent = float(input("Enter percentage: "))

                print("Result:",math_utils.percentage(number, percent))

            elif option == "5":
                radius = float(input("Enter radius: "))
                print("Result:",math_utils.circle_area(radius))

            else:
                print("Invalid option.")

        elif choice == "6":
            print("Thank you for using Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
