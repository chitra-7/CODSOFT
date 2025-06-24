def show_menu():
    print("=== BASIC MATH TOOL ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def calculate(num1, num2, choice):
    if choice == '1':
        return num1 + num2
    elif choice == '2':
        return num1 - num2
    elif choice == '3':
        return num1 * num2
    elif choice == '4':
        if num2 == 0:
            return "Cannot divide by zero!"
        return num1 / num2
    else:
        return "Invalid operation."

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting Basic Math Tool. Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculate(num1, num2, choice)
        print("Result:", result)
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    
    input("\nPress Enter to continue...")
