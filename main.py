import auth

license = "pdm5bxim2hwh9hbt"

def display_menu():
    print("Menu:")
    print("1. Add two numbers")
    print("2. Quit")

def add_numbers():
    auth.validateUser(license)
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            add_numbers()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__=='__main__':
    auth.validateUser(license)
    main()

