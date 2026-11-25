# Name: ERICKA JOY C. PALMA
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 2026

# get grades
def get_grades():
    grades = []

    while True:
        grade_input = input("Enter a grade or 'done' to finish: ")

        if grade_input.lower() == "done":
            break
        try:
            grade = float(grade_input)

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("\nInvalid grade. Please enter a number from 0 to 100.\n")

        except ValueError:
            print("\nInvalid input. Please enter a number from 0 to 100.\n")
    return grades

# calculate average
def get_average(grades):
    return sum(grades) / len(grades)

# finds highest
def get_highest(grades):
    return max(grades)

# find lowest
def get_lowest(grades):
    return min(grades)

# determines pass or fail
def get_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

grades = []

while True:
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("1. Enter Grades")
    print("2. View Results")
    print("3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        grades = get_grades()
        print("\nGrades successfully entered.")
    elif choice == "2":
        if len(grades) == 0:
            print("No grades entered yet. Please enter grades first.")
        else:
            average = get_average(grades)
            highest = get_highest(grades)
            lowest = get_lowest(grades)
            status = get_status(average)

            print("\n===== GRADE RESULTS =====")
            print(f"Average: {average:.2f}")
            print(f"Highest Grade: {highest:.2f}")
            print(f"Lowest Grade: {lowest:.2f}")
            print(f"Status: {status}")
    elif choice == "3":
        print("Thanks!")
        break
    else:
        print("Invalid choice. Select 1, 2, or 3.")

# The difference between LOCAL VARIABLE and GLOBAL VARIABLE is that a Global Variable ay isang variable that is created sa labas ng isang function.
# While a Local Variable ay isang variable that is created sa loob naman ng isang functin.
# Hindi rin pwedeng gamitin o cannot be use itong Local Variable sa labas, dapat sa loob lang ng function.