import csv
import os

CSV_PATH = 'students.csv'
FIELDS = ['name', 'grade', 'email', 'join_date']

# Make a loop that runs until the user enters 'quit'.
while True:
    # Ask user to input an action
    action = input("Enter an action (read, stats, add, delete, quit): ").strip().lower()

    # Do what the user asked for
    if action == 'quit':
        print("Exiting the program. Goodbye!")
        break
    elif action == 'stats':
        # Try to read the CSV file and display the data, if file doesn't exist, catch the error and print a message
        try:
            with open('students.csv', 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)
                if not students:
                    print("No data found in the file.")
                    continue

                # Analyze data (e.g., calculate average grade)
                total_grade = 0
                count = 0
                for student in students:
                    try:
                        total_grade += float(student['grade'])
                        count += 1
                    except ValueError:
                        print(f"Skipping {student['name']}: grade {student['grade']!r} is not a number.")
                if count == 0:
                    print("No numeric grades found.")
                    continue
                average_grade = total_grade / count
                print(f"Average grade of students: {average_grade:.2f}")
        except FileNotFoundError:
            print("File not found. Please make sure 'students.csv' exists.")
    elif action == 'add':
        # Try to add data to the file. If can't be turned into floats, ask for re input.
        # Ask user for student data and add it to the CSV file
        try:

            name = input("Enter student's name: ")
            grade = float(input("Enter student's grade: "))
            email = input("Enter student's email: ")
            year_date = input("Enter student's join year date (YYYY): ")
            month_date = input("Enter student's join month date (MM): ")
            day_date = input("Enter student's join day date (DD): ")
            join_date = f"{year_date}-{month_date}-{day_date}"
            needs_header = not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0
            with open(CSV_PATH, 'a', newline='') as file:
                writer = csv.writer(file)
                if needs_header:
                    writer.writerow(FIELDS)
                writer.writerow([name, grade, email, join_date])
                print(f"Student {name} with grade {grade}, email {email}, and join date {join_date} has been added to the file.")
        except ValueError:
            print("Invalid input. Please enter the correct data types for each field.")        
    elif action == 'read':
        # Try to read the CSV file and display contents, if file doesn't exist, catch the error and print a message
        try:
            import csv
            with open('students.csv', 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)
                if not students:
                    print("No data found in the file.")
                    continue

                # Display all student data
                print("Student Data:")
                for student in students:
                    print(f"Name: {student['name']}, Grade: {student['grade']}, Email: {student['email']}, Join Date: {student['join_date']}")

                # Analyze data (e.g., calculate average grade)
                total_grade = 0
                count = 0
                for student in students:
                    try:
                        total_grade += float(student['grade'])
                        count += 1
                    except ValueError:
                        print(f"Skipping {student['name']}: grade {student['grade']!r} is not a number.")
                if count == 0:
                    print("No numeric grades found.")
                    continue
                average_grade = total_grade / count
                print(f"Average grade of students: {average_grade:.2f}")
        except FileNotFoundError:
            print("File not found. Please make sure 'students.csv' exists.")
    elif action == 'delete':
        # Try to delete a student from the file
        try:
            name = input("Enter the name of the student to delete: ")
            with open('students.csv', 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)
            students = [student for student in students if student['name'] != name]
            with open('students.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(students)
            print(f"Student {name} has been deleted from the file.")
        except FileNotFoundError:
            print("File not found. Please make sure 'students.csv' exists.")
    else:
        print("Invalid action. Please enter 'read', 'stats', 'add', or 'quit'.")