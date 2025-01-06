# Student-Records-Management
This Python program manages student records using a dictionary. 


Student Information Management System

Description

This Python program is a simple command-line-based Student Information Management System. It allows users to manage student records efficiently by performing the following actions:

Add New Students

Display All Students

Delete Students

Search for Students by ID

Exit the Program

The program uses a dictionary to store student details, ensuring fast and efficient data retrieval and manipulation. Basic input validation is implemented to ensure data consistency.

Features

Interactive Menu: Users can navigate options easily through a menu-driven interface.

Student Validation: Ensures the registration number is exactly 5 digits and birth year is within a reasonable range (1920-2010).

Persistent Loop: The program continuously runs until the user decides to exit.

Efficient Data Structure: Student records are stored in a Python dictionary, with the registration number as the key.

Requirements

Python 3.x

How to Run

Ensure Python 3 is installed on your system.

Download the student_management.py file.

Open a terminal or command prompt.

Navigate to the directory containing the file.

Run the program by executing:

python student_management.py

Follow the on-screen prompts to interact with the system.

Usage

Upon running the program, the following menu options will be displayed:

--- Student Dictionary Management ---
1. Add new student
2. Display all students
3. Delete student
4. Search for student by ID
5. Exit

Option 1: Add a new student by entering their registration number (5 digits), first name, last name, birth year, and residence.

Option 2: Display all stored students and their details.

Option 3: Delete a student by providing their 5-digit registration number.

Option 4: Search for a specific student by entering their registration number.

Option 5: Exit the program.

Input Validation

Registration Number: Must be exactly 5 digits.

Birth Year: Must be a number between 1920 and 2010.

If invalid input is provided, the program will prompt the user to try again until valid data is entered.

Example

Choose an option (1-5): 1
Enter the student's Registration Number (5 digits): 12345
Enter the student's first name: John
Enter the student's last name: Doe
Enter the student's birth year (between 1920 and 2010, e.g., 1995): 1998
Enter the student's residence: Athens
Student successfully added.

Notes

The student dictionary is not saved to a file and exists only during program execution.

To implement persistent storage, consider adding file I/O to save and load student data.

Author

Kosmas Nikolaos
