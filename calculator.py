def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def option_menu():
    print("\nSelect an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input()

    # Validate choice input
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid selection, please try again.")
        choice = input()

    return choice

def validate_number():
    valid_number = False
    while not valid_number:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            valid_number = True
        except ValueError:
            print("Invalid input! Please enter numeric values.")

    return num1, num2

def main():
    while True:
        print("\n---Calculator---")

        choice = option_menu()

        if choice == "5":
            print("Bye Bye calculator")
            return

        num1, num2 = validate_number()

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {div(num1, num2)}")

if __name__ == '__main__':
    main()
