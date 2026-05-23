# Create the functions to use in the loop
def reverse_words(s):
    return ' '.join(s.split()[::-1])
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Build a loop that won't break until the user types "exit"
def main():
    while True:
        # Ask user for a function to perform on a string
        user_input = input("Enter a string function (reverse_words, count_vowels, is_palindrome), 'exit' to quit): ")

        # Do action based on user input
        if user_input == "exit":
            print("Exiting the program. Goodbye!")
            break
        #Reverse words, not letters in a string
        elif user_input == "reverse_words":
            string_to_reverse = input("Enter a string to reverse words: ")
            reversed_string = reverse_words(string_to_reverse)
            print(f"String with reversed words: {reversed_string}")
        elif user_input == "count_vowels":
            string_to_count = input("Enter a string to count vowels: ")
            count = count_vowels(string_to_count)
            print(f"Number of vowels in the string: {count}")
        elif user_input == "is_palindrome":
            string_to_check = input("Enter a string to check if it's a palindrome: ")
            result = is_palindrome(string_to_check)
            if result:
                print(f"The string '{string_to_check}' is a palindrome.")
            else:
                print(f"The string '{string_to_check}' is not a palindrome.")
        else:
            print("Invalid function. Please try again.")

if __name__ == "__main__":
    main()