# Name: ERICKA JOY C. PALMA
# Section: IV-BSIT-B
# Activity: P2 - Custom Module: student_utils
# Date: November 25, 2026

# Custom module import
import student_utils
from student_utils import get_highest # brings the get_highest function from student_utils into this program.

# Built-in module: printing the date and time
from datetime import datetime

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

def main():
    grades = get_grades()

    if len(grades) == 0:
        print("No grades were entered.")
    else: # after importing student_utils we can now use its functions ex. module.function()
        average = student_utils.get_average(grades)
        highest = get_highest(grades)
        lowest = student_utils.get_lowest(grades)
        status = student_utils.get_status(average)

        report_time = datetime.now() # gets the current date/time.

        print("\n===== STUDENT GRADE REPORT =====")
        print(f"Average: {average:.2f}")
        print(f"Highest Grade: {highest:.2f}")
        print(f"Lowest Grade: {lowest:.2f}")
        print(f"Status: {status}")
        print(f"Report generated: {report_time.strftime('%B %d, %Y %I:%M %p')}") # use strftime(...) para maging readable ung datae/time.

if __name__ == "__main__":
    main()