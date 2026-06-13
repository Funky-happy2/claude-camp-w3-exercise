# String Utility

A small command-line program with three string helper functions.

## Files

| File | Purpose |
|------|---------|
| `String_utility.py` | The program and its three functions. |
| `String_utility_test.py` | Tests for each function. |

## The functions

| Function | What it does | Example |
|----------|--------------|---------|
| `reverse_words(s)` | Reverses the order of words (not the letters). | `"Hello World"` → `"World Hello"` |
| `count_vowels(s)` | Counts the vowels (a, e, i, o, u, any case). | `"Hello World"` → `3` |
| `is_palindrome(s)` | Checks if the text reads the same backwards, ignoring case, spaces, and punctuation. | `"A man, a plan, a canal, Panama"` → `True` |

## Running the program

```bash
python3 String_utility.py
```

You'll get a prompt that loops until you type `exit`:

```
Enter a string function (reverse_words, count_vowels, is_palindrome), 'exit' to quit:
```

Type one of the function names, then enter the string to run it on.

## Running the tests

```bash
python3 String_utility_test.py
```

A clean run prints `All tests passed!`. The tests use `assert`, so a failing
check raises an error pointing at the exact line that failed.

You can also run them with pytest if it's installed:

```bash
pytest String_utility_test.py
```
