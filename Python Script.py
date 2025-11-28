# Calculator Program
import math

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("         CALCULATOR")
    print("="*40)
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("="*40)

def get_operation():
    """Get the operation choice from the user"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def get_numbers(operation):
    """Get numbers from the user based on operation type"""
    if operation == '5':  # Square root only needs one number
        while True:
            try:
                num = float(input("Enter a number: "))
                return num, None
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:  # Other operations need two numbers
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                return num1, num2
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

def perform_calculation(operation, num1, num2):
    """Perform the selected calculation"""
    if operation == '1':
        return 'Addition', num1 + num2
    elif operation == '2':
        return 'Subtraction', num1 - num2
    elif operation == '3':
        return 'Multiplication', num1 * num2
    elif operation == '4':
        return 'Division', num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == '5':
        return 'Square Root', math.sqrt(num1) if num1 >= 0 else "Error: Cannot take square root of negative number"

def display_result(operation_name, num1, num2, result):
    """Display the calculation result"""
    print("\n" + "-"*40)
    if num2 is not None:
        print(f"{operation_name}: {num1} and {num2}")
    else:
        print(f"{operation_name}: {num1}")
    print(f"Result: {result}")
    print("-"*40)

def main():
    """Main calculator loop"""
    while True:
        operation = get_operation()
        num1, num2 = get_numbers(operation)
        operation_name, result = perform_calculation(operation, num1, num2)
        display_result(operation_name, num1, num2, result)
        
        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
