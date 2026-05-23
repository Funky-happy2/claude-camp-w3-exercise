import builtins
import io
from contextlib import redirect_stdout
from json_writer_and_reader import read_file, edit_file, add_data, delete_data


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


def test_add_data():
    fake_input("some new data")
    output = capture(add_data)
    try:
        assert "Data has been written to the file." in output
        with open("data.json") as f:
            assert f.read() == "some new data"
    except AssertionError:
        print("add_data failed")


def test_delete_data():
    with open("data.json", "w") as f:
        f.write("existing content")
    output = capture(delete_data)
    try:
        assert "Data has been deleted from the file." in output
        with open("data.json") as f:
            assert f.read() == ""
    except AssertionError:
        print("delete_data failed")


def test_edit_file_add():
    fake_input("add", "edited content")
    output = capture(edit_file)
    try:
        assert "Data has been written to the file." in output
        with open("data.json") as f:
            assert f.read() == "edited content"
    except AssertionError:
        print("edit_file add failed")


def test_edit_file_delete():
    with open("data.json", "w") as f:
        f.write("to be removed")
    fake_input("delete")
    output = capture(edit_file)
    try:
        assert "Data has been deleted from the file." in output
        with open("data.json") as f:
            assert f.read() == ""
    except AssertionError:
        print("edit_file delete failed")


def test_read_file():
    with open("data.json", "w") as f:
        f.write("hello world")
    output = capture(read_file)
    try:
        assert "hello world" in output
    except AssertionError:
        print("read_file failed")


def main():
    test_add_data()
    test_delete_data()
    test_edit_file_add()
    test_edit_file_delete()
    test_read_file()
    print("All tests completed.")


if __name__ == "__main__":
    main()
