# Assignment Sub-task 3 (Student Records Management) - Kosmas Nikolaos - AM: 169560

# This function displays a menu with the options available in the program. ----->
# -----> It prints options 1-5 (Add new student, Display all students, Delete student, Search for student by ID, Exit).
def display_menu():
    print("\n--- Student Dictionary Management ---")
    print("1. Add new student")
    print("2. Display all students")
    print("3. Delete student")
    print("4. Search for student by ID")
    print("5. Exit")

# Step 1: Add a student with detailed information and validate ID and birth year
# This function (def add_student(students)) adds a new student to the dictionary. The user is prompted to provide the student ID, name, surname, birth year, and residence. -----> 
# -----> The ID must be exactly 5 digits long and the birth year must be a number between 1920 and 2010. -----> 
# -----> If the information is correct, the student is added to the dictionary. If not, the user is asked to re-enter the information. -----> 
def add_student(students):
    while True:
        am = input("Enter the student's Registration Number (5 digits): ")
        # Check if the ID is numeric (isdigit()) and exactly 5 digits long (len(am) == 5). If valid, break the loop.
        # If invalid, display an error message and repeat the loop.
        if am.isdigit() and len(am) == 5:
            break
        else:
            print("The Registration Number must have 5 digits and contain only numbers. Try again.")
    
    # Enter student's first name
    name = input("Enter the student's first name: ")
    # Enter student's last name
    surname = input("Enter the student's last name: ")

    # Check if a valid birth year is entered
    while True:
        birth_year = input("Enter the student's birth year (between 1920 and 2010, e.g., 1995): ")
        # Check if the birth year is numeric (isdigit()) and between 1920 and 2010.
        if birth_year.isdigit() and 1920 <= int(birth_year) <= 2010:
            break
        else:
            print("The birth year must be a number between 1920 and 2010. Try again.")
    
    # Enter student's residence
    residence = input("Enter the student's residence: ")
    
    # Add the student to the dictionary with ID as key and other details as values
    students[am] = {
        "First Name": name,
        "Last Name": surname,
        "Birth Year": birth_year,
        "Residence": residence
    }
    print("Student successfully added.")

# Step 2: Display all students in the dictionary
def display_students(students):
    # Check if the dictionary is empty
    # If not, iterate over the dictionary and display each student's information (ID, first name, last name, birth year, residence)
    if not students:
        print("No students found.")
    else:
        for am, info in students.items():
            print(f"ID: {am}, First Name: {info['First Name']}, Last Name: {info['Last Name']}, Birth Year: {info['Birth Year']}, Residence: {info['Residence']}")

# Step 3: Delete a student by their ID
def delete_student(students):
    while True:
        am = input("Enter the Registration Number of the student you want to delete (5 digits): ")
        # If the ID is valid, check if it exists in the dictionary
        if am.isdigit() and len(am) == 5:
            if am in students:
                # Delete the student if found
                del students[am]
                print("Student successfully deleted.")
                break
            else:
                # Error message if the ID is not found
                print("Student ID not found.")
        else:
            # Error message if the ID is invalid
            print("The Registration Number must have 5 digits and contain only numbers. Try again.")

# Step 4: Search for a student by their ID
def search_student(students):
    while True:
        am = input("Enter the student's Registration Number (5 digits), or press Enter to return to the main menu: ")
        if am == "":
            break
        elif am.isdigit() and len(am) == 5:
            if am in students:
                info = students[am]
                print(f"Student information for ID: {am}\n - First Name: {info['First Name']}\n - Last Name: {info['Last Name']}\n - Birth Year: {info['Birth Year']}\n - Residence: {info['Residence']}")
            else:
                print("No student found with this ID.")
        else:
            print("The Registration Number must be numeric and exactly 5 digits.")

# Main Program
students = {}
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        delete_student(students)
    elif choice == "4":
        search_student(students)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
