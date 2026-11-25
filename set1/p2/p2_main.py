# Name: ERICKA JOY C. PALMA
# Section: IV-BSIT-B
# Activity: P2 - Custom Module: student_utils
# Date: November 25, 2026

import student_utils
from student_utils import get_highest

from datetime import datetime

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
    else:
        average = student_utils.get_average(grades)
        highest = get_highest(grades)
        lowest = student_utils.get_lowest(grades)
        status = student_utils.get_status(average)

        report_time = datetime.now()

        print("\n===== STUDENT GRADE REPORT =====")
        print(f"Average: {average:.2f}")
        print(f"Highest Grade: {highest:.2f}")
        print(f"Lowest Grade: {lowest:.2f}")
        print(f"Status: {status}")
        print(f"Report generated: {report_time.strftime('%B %d, %Y %I:%M %p')}")

if __name__ == "__main__":
    main()










    

# The student_utils.py is a module containing reusable codes such as functions ex. get_average(grades).
# I created this to separate the functions from the main program para maging reusable ang mga 'to sa ibang programs.

# import student_utils : gamit 'to, I can access the functions mula sa module(student_utils).
# from student_utils import get_highest : gamit 'to, I can call the get_highest() directly. 
#         average = student_utils.get_average(grades)
#         highest = get_highest(grades)
#         lowest = student_utils.get_lowest(grades)
#         status = student_utils.get_status(average)

# datetime is a built-in Python module, ginamit ko lang para idisplay ang date and time ng pag-run nong program.