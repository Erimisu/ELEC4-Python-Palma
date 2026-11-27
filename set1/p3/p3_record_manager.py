# Name: ERICKA JOY C. PALMA
# Section: IV-BSIT-B
# Activity: P3: Student Record Manager 
# Date: November 2026

# === CREATE EMPTY LIST & SET ===

# List : for actual student names.
students = []
# Set : for lowercase/normalized version of student names
student_name = set()

# === HERE COMES OUR 5 PROGRAM FUNCTIONS ===

def add_student():

    # Keeps the input in loop.
    while True:
        name = input("Enter your name: ").strip()

        if name.lower() == "done":
            print("Finished adding students!")
            break
        
        if name == "": # Check for empty inputs
            print("Student name cannot be empty!")
            continue
 
        normalized_name = name.lower() # Check Duplications

        if normalized_name in student_name:
            print("Student already exists!\n")
            continue

        students.append(name) # Ddds the actual name to the List.
        student_name.add(normalized_name) # Adds the normalized name to the Set.

        print("Student added successfully!\n")

def remove_student():
    name = input("Enter student name to remove: ").strip()

    # Check for empty inputs
    if name == "":
        print("Student name cannot be empty.")
        return

    normalized_name = name.lower()

    for student in students: # Loop through students list
        if student.lower() == normalized_name: # actual name == normalized name
            
            # Removes actual and normalized name sa List and Set
            students.remove(student)
            student_name.remove(normalized_name)

            print("Student removed successfully.")
            return

    print("Student not found.")

def search_student():
    name = input("\nFind student: ").strip().lower()

    # if the user enters nothing.
    if name == "":
        print("\nSearch term cannot be empty.")
        return

    found = False

    print("\n--- Search Results ---\n")
   
    for student in students: # Loop through students list
        if name in student.lower():
            print(student)
            found = True

    if not found:
        print("\nNo student found.")

def display_students():

    # check if empty ang list
    if not students:
        print("No students in the record!")
        return
    
    # arrange the List in alphabetical order. Save it sa variable sorted_students.
    sorted_students = sorted(students, key=str.lower)

    print("\n=== STUDENT LIST ===")

    # add numerical numbers ex. 1. Ericka
    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    # len() counts the total items
    print(f"\nTotal students: {len(students)}")

def display_menu():
    print("\n===== STUDENT RECORD MANAGER =====\n")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit\n")


if __name__=="__main__":

    # this what makes the menu keep coming back.
    while True:

        # === actual program flow ===

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


# COMMENTS/EXPLANATIONS
#  The difference between List and Set is that List can store identical items in ordered, while Set stores only unique items in unordered collection.
#  So I used Lists to make sure that student names are display in alphabetical order.
#  I used Set naman to make sure names are unique.