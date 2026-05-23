from String_utility import is_palindrome
from String_utility import count_vowels
from String_utility import reverse_words


def test_reverse_words():
    assert reverse_words("Hello World") == "World Hello"
    assert reverse_words("Python is great") == "great is Python"
    assert reverse_words("   Leading and trailing spaces   ") == "spaces trailing and Leading"
    assert reverse_words("") == ""
    assert reverse_words("SingleWord") == "SingleWord"
    assert reverse_words("Multiple   spaces between words") == "words between spaces Multiple"
    assert reverse_words("Punctuation! Should, be: handled?") == "handled? be: Should, Punctuation!"


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama") is True
    assert is_palindrome("No 'x' in Nixon") is True
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("Madam In Eden, I'm Adam") is True
    assert is_palindrome("Hello, World!") is False
    assert is_palindrome("12321") is True
    assert is_palindrome("Hi ih") is True


def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python is great") == 4
    assert count_vowels("   Leading and trailing spaces   ") == 9
    assert count_vowels("") == 0
    assert count_vowels("SingleWord") == 3
    assert count_vowels("Multiple   spaces between words") == 9
    assert count_vowels("Punctuation! Should, be: handled?") == 10

def main():
    test_reverse_words()
    test_is_palindrome()
    test_count_vowels()
    print("All tests passed!")

if __name__ == "__main__":
    main()
