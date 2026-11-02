# Your first program (How to start coding)

A tiny Python program for total beginners. It says hello, asks your name, greets you, and works out roughly how many days old you are.

## What you need (both free)
1. **Python**, the programming language: download it from https://www.python.org/downloads/
   - On Windows, in the first installer screen, tick **"Add python.exe to PATH"**, then click **Install Now**.
2. **VS Code**, the app where you type code: https://code.visualstudio.com/

## Run it
1. Download this folder (or copy `hello.py` into a new folder).
2. Open the folder in VS Code (**File > Open Folder...**).
3. Open the terminal (**Terminal > New Terminal**) and type:
   ```
   python hello.py
   ```
   On Mac or Linux, type `python3 hello.py` instead.
4. Answer the two questions. Example:
   ```
   Hello, world!
   What's your name? Maria
   Hi Maria!
   How old are you? 25
   You are about 9125 days old!
   ```

## The 4 ideas in this program
| Code | What it means |
|---|---|
| `print("Hello, world!")` | show this text on the screen |
| `input("What's your name? ")` | ask a question and wait for the answer (the answer is always text) |
| `name = ...` | a **variable**: a labelled box that keeps a value |
| `int(...)` | turn text like `"25"` into a whole number, so you can do math with it |

## The beginner mistake from the video
`steps/step-3-mistake.py` forgets `int()`. Text times a number repeats the text, so `"25" * 365` prints 25 written 365 times.
`hello.py` is the fixed version.

## Files
- `hello.py`: the finished program
- `steps/step-1.py` to `steps/step-3.py`: the file after each step of the video (`step-3-mistake.py` = the mistake)

If `python` is "not recognized", Python is not on PATH: run the installer again, choose **Modify**, and tick **Add Python to environment variables**. (Typing a word that is not a number at the age question shows a `ValueError`; that is normal for this tiny program.)
