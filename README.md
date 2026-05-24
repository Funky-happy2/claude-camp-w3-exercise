# File Reader / Writer

A small command-line program that reads from and writes to a `data.json` file.

> **Note:** despite the name, this stores plain text, not real JSON — it never
> uses Python's `json` module. The file is just named `data.json`.

## Files

| File | Purpose |
|------|---------|
| `json_writer_and_reader.py` | The program: read, add, and delete the contents of `data.json`. |
| `Json_file_test.py` | Tests for every function in the program. |

## Running the program

```bash
python3 json_writer_and_reader.py
```

You'll get a prompt that loops until you type `quit`:

```
Enter an action (read, edit, quit):
```

| Action | What it does |
|--------|--------------|
| `read` | Prints the contents of `data.json` (or a message if it doesn't exist). |
| `edit` | Asks `add` or `delete`. `add` writes the text you type; `delete` empties the file. |
| `quit` | Exits. |

`data.json` is created in the current folder the first time you add data.

## Running the tests

```bash
python3 Json_file_test.py
```

A clean run prints `All tests completed.` with no error lines. If a check
fails, it prints a line like `add_data failed` and keeps going.

The tests capture each function's printed output and check it with `assert`,
and they feed fake keyboard input so nothing pauses waiting for you to type.
