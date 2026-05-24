# CSV Student Data Analyser

A small command-line program for storing and analysing student records in a
`students.csv` file.

## Files

| File | Purpose |
|------|---------|
| `CSV_Student_Data_Analyser.py` | The program: read, add, delete, and get stats on student records. |
| `CSV_Student_Data_Analyser_Test.py` | Tests for every function in the program. |

## Running the program

```bash
python3 CSV_Student_Data_Analyser.py
```

You'll get a prompt that loops until you type `quit`:

```
Enter an action (read, stats, add, delete, quit):
```

| Action | What it does |
|--------|--------------|
| `read` | Prints every student and the average grade. |
| `stats` | Prints just the average grade. |
| `add` | Asks for name, grade, email, and join date (year, month, day), then appends a row. |
| `delete` | Asks for a name and removes that student. |
| `quit` | Exits. |

The data is stored in `students.csv`, which is created automatically the first
time you add a student.

## Running the tests

```bash
python3 CSV_Student_Data_Analyser_Test.py
```

A clean run prints `All tests completed.` with no error lines. If a check
fails, it prints a line like `add_data failed` and keeps going.

The tests **back up** your real `students.csv` before running and **restore**
it afterwards, so running them never changes your data.
