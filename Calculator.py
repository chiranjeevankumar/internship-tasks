# PROJECT 01: INTERACTIVE CALCULATOR & UNIT CONVERTER
# Conversion factors
FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}
# Read valid numbers from the user
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
# Arithmetic functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b
# Unit conversion functions
def km_to_miles(km):
    return km * FACTORS["km_to_miles"]
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
def kg_to_pounds(kg):
    return kg * FACTORS["kg_to_pounds"]
# Main calculator program
def main():
    while True:
        print("\n===== CALCULATOR & UNIT CONVERTER =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Conversion")
        print("6. Quit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Thank you for using the calculator!")
            break
        elif choice in ("1", "2", "3", "4"):
            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")
            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
        elif choice == "5":
            print("\n===== UNIT CONVERSION =====")
            print("1. Kilometers to Miles")
            print("2. Celsius to Fahrenheit")
            print("3. Kilograms to Pounds")
            conversion = input("Choose conversion (1-3): ").strip()
            if conversion == "1":
                km = read_number("Enter kilometers: ")
                print("Miles:", km_to_miles(km))
            elif conversion == "2":
                c = read_number("Enter Celsius: ")
                print("Fahrenheit:", celsius_to_fahrenheit(c))
            elif conversion == "3":
                kg = read_number("Enter kilograms: ")
                print("Pounds:", kg_to_pounds(kg))
            else:
                print("Invalid conversion choice!")
        else:
            print("Invalid choice! Please select 1 to 6.")
# Run the program
if __name__ == "__main__":
    main()
