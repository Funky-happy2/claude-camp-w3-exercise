import builtins
import io
import os
from contextlib import redirect_stdout
from CSV_Student_Data_Analyser import read_file, add_data, delete_data, stats


def fake_input(*answers):
    # Make input() return our answers one by one instead of asking the keyboard.
    answers = iter(answers)
    builtins.input = lambda *args: next(answers)


def capture(func):
    # Run func and return everything it printed as a string.
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func()
    return buffer.getvalue()


def write_sample_csv():
    # Start each test from a known file with two students.
    with open("students.csv", "w", newline="") as f:
        f.write("name,grade,email,join_date\n")
        f.write("Alice,90,alice@x.com,2024-01-01\n")
        f.write("Bob,80,bob@x.com,2024-02-02\n")


def test_add_data():
    if os.path.exists("students.csv"):
        os.remove("students.csv")
    fake_input("Carol", "70", "carol@x.com", "2024", "03", "03")
    output = capture(add_data)
    try:
        assert "has been added to the file" in output
        with open("students.csv") as f:
            contents = f.read()
        assert "Carol" in contents
        assert "carol@x.com" in contents
    except AssertionError:
        print("add_data failed")


def test_read_file():
    write_sample_csv()
    output = capture(read_file)
    try:
        assert "Alice" in output
        assert "Bob" in output
        # Average of 90 and 80 is 85.00
        assert "85.00" in output
    except AssertionError:
        print("read_file failed")


def test_stats():
    write_sample_csv()
    output = capture(stats)
    try:
        assert "85.00" in output
    except AssertionError:
        print("stats failed")


def test_delete_data():
    write_sample_csv()
    fake_input("Alice")
    output = capture(delete_data)
    try:
        assert "has been deleted from the file" in output
        with open("students.csv") as f:
            contents = f.read()
        assert "Alice" not in contents
        assert "Bob" in contents
    except AssertionError:
        print("delete_data failed")


def main():
    # Back up the real students.csv so the tests never destroy your data.
    backup = None
    if os.path.exists("students.csv"):
        with open("students.csv") as f:
            backup = f.read()
    try:
        test_add_data()
        test_read_file()
        test_stats()
        test_delete_data()
        print("All tests completed.")
    finally:
        # Restore (or remove) students.csv to its original state.
        if backup is None:
            if os.path.exists("students.csv"):
                os.remove("students.csv")
        else:
            with open("students.csv", "w", newline="") as f:
                f.write(backup)


if __name__ == "__main__":
    main()
