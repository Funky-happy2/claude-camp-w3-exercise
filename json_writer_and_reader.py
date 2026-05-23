# Make the function that will run the program
def read_file():
    # Try read whole file and print it, if file doesn't exist, catch the error and print a message
    try:
        with open('data.json', 'r') as file:
            data = file.read()
            print("Data read from file:")
            print(data)
    except FileNotFoundError:
        print("File not found. Please make sure 'data.json' exists.")
def edit_file():
    # Ask to add or delete data in the file
    edit_action = input("Enter 'add' to add data or 'delete' to delete data: ").strip().lower()
    if edit_action == 'delete':
        with open('data.json', 'w') as file:
            file.write('')
            print("Data has been deleted from the file.")
    elif edit_action == 'add':
        new_data = input("Enter new data to write to the file: ")
        with open('data.json', 'w') as file:
            file.write(new_data)
            print("Data has been written to the file.")

def add_data():
    new_data = input("Enter new data to write to the file: ")
    with open('data.json', 'w') as file:
        file.write(new_data)
        print("Data has been written to the file.")
def delete_data():
    with open('data.json', 'w') as file:
        file.write('')
        print("Data has been deleted from the file.")
        
def main():
    # Make a loop that runs until the user enters 'quit'.
    while True:
        # Ask the user to input an action
        action = input("Enter an action (read, edit, quit): ").strip().lower()

        # Do what the user asked for
        if action == 'quit':
            print("Exiting the program. Goodbye!")
            break
        elif action == 'read':
            # Try read whole file and print it, if file doesn't exist, catch the error and print a message
            try:
                with open('data.json', 'r') as file:
                    data = file.read()
                    print("Data read from file:")
                    print(data)
            except FileNotFoundError:
                print("File not found. Please make sure 'data.json' exists.")
        elif action == 'edit':
            # Ask to add or delete data in the file
            edit_action = input("Enter 'add' to add data or 'delete' to delete data: ").strip().lower()
            if edit_action == 'delete':
                delete_data()
            elif edit_action == 'add':
                add_data()
            
        else:
            print("Invalid action. Please enter 'read', 'edit', or 'quit'.")

if __name__ == "__main__":
    main()