# Python CRUD with Tkinter and SQLite: Student Records

A complete desktop CRUD app: add, view, search, update and delete students, saved in a SQLite database.
Uses only the Python standard library (Tkinter + sqlite3). Tested with Python 3.12 on Windows 11 and Linux Mint 22.3.

## Run it
```bash
python app.py
```
That's all. `students.db` is created next to the script on the first run.
On Linux, if Tkinter is missing: `sudo apt install python3-tk` (then use `python3 app.py`).

## Files
| File | What it does |
|---|---|
| `db.py` | Database layer: `connect()` creates the table; `add_student`, `get_students(search)`, `update_student`, `delete_student`. Run `python db.py` for a quick test. |
| `app.py` | Tkinter window: form (Entry, Combobox, Spinbox), Treeview table, Add / Update / Delete / Clear buttons, live search. |
| `test_db.py` | Tests all four database functions without a window. |
| `steps/` | Start states used in the video's live coding (`db_start.py`, `app_start.py`) and the missing-commit mistake (`db_nocommit.py`) vs the fix (`db_fixed.py`). |
| `shorts/` | The Short's example: `no_commit.py` (data lost) vs `fixed.py` (`with connect() as conn`). |
| `errors/` | The four common errors from the video, each runnable: no commit, SQL built with f-strings (injection), row position used as the id, `int()` on unchecked text. |

## Key ideas
- `with connect() as conn:` commits automatically when the block ends without an error (and rolls back on an error).
- Always pass values with `?` placeholders, never with f-strings.
- Insert table rows with `iid=row[0]` so `table.selection()` returns the real database id.
- Call `refresh()` after every change so the table always matches the database.

## Ideas to extend it
Add a phone number column, export to CSV, sort by clicking a column heading, or turn it into an inventory system.

Demo data only (fake names, `@example.com` addresses).
