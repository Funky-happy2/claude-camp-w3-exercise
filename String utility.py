# Build a loop that won't break until the user types "exit"
while True:
    # Ask user for a function to perform on a string
    user_input = input("Enter a string function (reverse, count_vowels, is_palindrome), 'exit' to quit): ")

    # Clean the input
    user_input = user_input.strip().lower()

    # Do action based on user input
    if user_input == "exit":
        print("Exiting the program. Goodbye!")
        break
    elif user_input == "reverse":
        string_to_reverse = input("Enter a string to reverse: ")
        reversed_string = string_to_reverse[::-1]
        print(f"Reversed string: {reversed_string}")
    elif user_input == "count_vowels":
        string_to_count = input("Enter a string to count vowels: ")
        vowels = 'aeiouAEIOU'
        count = sum(1 for char in string_to_count if char in vowels)
        print(f"Number of vowels in the string: {count}")
    elif user_input == "is_palindrome":
        string_to_check = input("Enter a string to check if it's a palindrome: ")
        cleaned_string = ''.join(char.lower() for char in string_to_check if char.isalnum())
        is_palindrome = cleaned_string == cleaned_string[::-1]
        if is_palindrome:
            print(f"The string '{string_to_check}' is a palindrome.")
        else:
            print(f"The string '{string_to_check}' is not a palindrome.")
    else:
        print("Invalid function. Please try again.")