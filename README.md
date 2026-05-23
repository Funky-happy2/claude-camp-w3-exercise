Claude Camp W3 Exercises
By Frank Zhang — Week 3 of the CLAUDE AI Special Study Group
Three Python projects built for Week 3, covering real file I/O, JSON config editing, and string utilities with unit testing.

Project 1: CSV Student Data Analyser
What it does
Reads and manages student records stored in a students.csv file. You can:

Read — display all students and their average grade
Stats — show just the average grade
Add — add a new student (name, grade, email, join date)
Delete — remove a student by name
Quit — exit the program

The program automatically creates the CSV header the first time a student is added, and uses proper error handling if the file doesn't exist yet.
Files used
FileDescriptionCSV_Student_Data_Analyser.pyMain programstudents.csvCreated automatically when you add your first student
How to run
bashpython CSV_Student_Data_Analyser.py
Then type one of: read, stats, add, delete, or quit
Example session
Enter an action (read, stats, add, delete, quit): add
Enter student's name: Alice
Enter student's grade: 95
Enter student's email: alice@example.com
Enter student's join year date (YYYY): 2026
Enter student's join month date (MM): 05
Enter student's join day date (DD): 18

Enter an action (read, stats, add, delete, quit): read
Student Data:
Name: Alice, Grade: 95.0, Email: alice@example.com, Join Date: 2026-05-18
Average grade of students: 95.00

Project 2: JSON Config File Reader & Writer
What it does
Reads from and writes to a data.json file using a simple command-line menu. You can:

Read — display the current contents of the file
Edit → Add — write new data to the file
Edit → Delete — clear all data from the file
Quit — exit the program

Uses try/except to handle the case where the file doesn't exist yet.
Files used
FileDescriptionjson_writer_and_reader.pyMain programdata.jsonCreated/edited when you use the edit option
How to run
bashpython json_writer_and_reader.py
Then type one of: read, edit, or quit
Example session
Enter an action (read, edit, quit): edit
Enter 'add' to add data or 'delete' to delete data: add
Enter new data to write to the file: {"theme": "dark", "language": "English"}
Data has been written to the file.

Enter an action (read, edit, quit): read
Data read from file:
{"theme": "dark", "language": "English"}

Project 3: String Utility Library
What it does
An interactive string tool with three functions:

reverse — reverses the characters in a string ("hello" → "olleh")
count_vowels — counts all vowels (a, e, i, o, u), case-insensitive
is_palindrome — checks if a string reads the same forwards and backwards, ignoring spaces, punctuation, and capitalisation (so "A man a plan a canal Panama" counts as a palindrome!)

Files used
FileDescriptionString_utility.pyMain program — no extra files needed
How to run
bashpython String_utility.py
Then type one of: reverse, count_vowels, is_palindrome, or exit
Example session
Enter a string function (reverse, count_vowels, is_palindrome), 'exit' to quit): is_palindrome
Enter a string to check if it's a palindrome: A man a plan a canal Panama
The string 'A man a plan a canal Panama' is a palindrome.

Enter a string function (reverse, count_vowels, is_palindrome), 'exit' to quit): count_vowels
Enter a string to count vowels: Hello World
Number of vowels in the string: 3

How to test all projects
Manual testing checklist
CSV Student Data Analyser:

 Run add with valid inputs → student appears when you read
 Run add with a non-number grade → error message shown, nothing saved
 Run delete with a student's name → student removed
 Run read before any students exist → "File not found" message shown

JSON Config File Reader & Writer:

 Run read before data.json exists → "File not found" message shown
 Run edit → add → data appears when you read
 Run edit → delete → file contents cleared
 Type an invalid action → "Invalid action" message shown

String Utility:

 reverse on "hello world" → "dlrow olleh"
 count_vowels on "Hello World" → 3
 is_palindrome on "racecar" → palindrome ✅
 is_palindrome on "A man a plan a canal Panama" → palindrome ✅
 is_palindrome on "hello" → not a palindrome ✅
 Type an invalid function name → "Invalid function. Please try again."


Requirements

Python 3.x
No external libraries needed (uses built-in csv, os, and string methods only)