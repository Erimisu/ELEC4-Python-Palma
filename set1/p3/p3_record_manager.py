# Name: ERICKA JOY C. PALMA
# Section: IV-BSIT-B
# Activity: P3: Student Record Manager 
# Date: November 2026

# === CREATE EMPTY LIST & SET ===
# why use two? List cant prevent duplicates, so we use Set to help check uniqueness.

# List : store the actual student names I want to disply hal. Ericka Palma
students = []
# Set : store the lowercase/normalized version of student names hal. ericka palma
student_name = set()

# === HERE COMES OUR 5 PROGRAM FUNCTIONS ===

#00 I have a first function called add_student()
def add_student():
    #01 input() ask the user for a name.
    #02 .strip() removes extra spaces sa beginning and start.
    #03 name dito sini-save ung entered name.
    #04 while True helps keep this input repeatable kasi gusto kong makapaginput ng multiple students si user.
    while True:
        name = input("Enter your name: ").strip()

        # .lower() helps converts text to lowercase ex. "DONE" to "done"
        if name.lower() == "done":
            print("Finished adding students!")
            break
        
        #  check for empty inputs. We shouldn't allow empty names being entered...
        if name == "":
            print("Student name cannot be empty!")
            continue #Skip this attempt, then ask for another name.
        #use this for duplication checking.
        normalized_name = name.lower() # checks whether something exists in the set

        # Check if the student already exists. This checks if this normalized name already inside our set
        if normalized_name in student_name:
            print("Student already exists!\n")
            continue

        students.append(name) # adds a name to the List.
        student_name.add(normalized_name) # adds the normalized name to the Set.

        print("Student added successfully!\n")

# The second function find a student and remove them.
def remove_student():
    name = input("Enter student name to remove: ").strip() # get the student name

    # check for empty input, if true, return helps leave the function.
    if name == "":
        print("Student name cannot be empty.")
        return

    normalized_name = name.lower() #again, converts original user input into lowercase version and save it as "normalized_name"

    for student in students: # This loop will go through every student in the list one by one.
        if student.lower() == normalized_name: # and then compares the actual name and normalized name. If True, it found the student.
            
            # The program removes both actual and normalized name from the collections (List and Set)
            students.remove(student)
            student_name.remove(normalized_name)

            print("Student removed successfully.")
            return

    #If the for loop finishes without finding anyone
    print("Student not found.")

# This function looks for matching name.
def search_student():
    # when the user input text, the .strip removes extra spaces and convert it into lowercase and save it sa variable name.
    name = input("\nFind student: ").strip().lower()

    # if the user enters nothing.
    if name == "":
        print("\nSearch term cannot be empty.")
        return

    #if nothing is found
    found = False

    print("\n--- Search Results ---\n")
    # for loop: examine every student name sa students (List) one by one.
    for student in students:
        #suppose the actual name is "Ericka Palma" and user searched "ericka", then "ericka" is in "Ericka Palma".
        if name in student.lower():
            #therefore we print the actual name.
            print(student)
            # Because after the loop, we need to know whether anything matched.
            found = True

    #if nothing is found, it will print blahhh.
    if not found:
        print("\nNo student found.")

# This function show all students alphabetically, numbered, and give the total.
def display_students():

    # check if empty ang list
    if not students:
        print("No students in the record!")
        return
    
    # arrange the actual list(students) in alphabetically sorted version, and save it sa variable sorted_students as sorted version
    sorted_students = sorted(students, key=str.lower) # key=str.lower prevents uppercase/lowercase differences from making the ordering weird.

    print("\n=== STUDENT LIST ===")

    # add numerical numbers ex. 1. Ericka
    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}") # using f string, I able to insert variables into text.

    # len() counts the total items
    print(f"\nTotal students: {len(students)}")

def display_menu():
    print("\n===== STUDENT RECORD MANAGER =====\n")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit\n")

# Run the following code when this Python file is executed directly.
if __name__=="__main__":

    # this what makes the menu keep coming back.
    while True:

        # === actual program flow ===

        display_menu()

        # suppose the user enter 1-5, i-compares it sa if conditions sa baba.
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
