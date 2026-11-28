# Name: ERICKA JOY C. PALMA
# Section: IV-BSIT-B
# Activity: P4: Safe Menu Program
# Date: November 2026

# SIMPLE MENU SOURCE CODE

# Display the menu
def display_menu():
    print("\n===== SAFE MENU PROGRAM =====\n")
    print("1. Divide two numbers")
    print("2. Open a file")
    print("3. Exit")

# divide numbers and handle error
def divide_numbers():
    
    try: # will calculate
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2

    except ValueError: # ValueError catch non-numeric input, no crash happens.
        print("Invalid input. Please enter numbers only")

    except ZeroDivisionError: # ZeroDivisionError catch 0 input, no crash happens.
        print("Cannot divide by zero.")

    else: # print the result if try statement is true?
         print(f"Result: {result}")
         print("Division operation finished.")

# Read files and handle errors.
def open_file():

    filename = input("\nEnter file name: ").strip()

    try: # open the file that you input
        with open(filename, "r") as file:
            print("\n--- File Contents ---\n")
            print(file.read()) # read and display everything inside that file.

    # FileNotFoundError catch non-exist files, no crash happens.
    except FileNotFoundError:
        print("File not found.")

    finally: # runs may error man o wala
        print("\nFile operation finished.")

# keeps the menu running
while True:
    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        divide_numbers()
    elif choice == "2":
        open_file()
    elif choice == "3":
        print("Bye bye!")
        break
    else:
        print("Invalid choice. Please select 1-3.")


# def display_menu() displays the menu
# def divide_numbers() divides two numbers and handle errors
# def open_file() read files and handle error
# while True keeps the menu running