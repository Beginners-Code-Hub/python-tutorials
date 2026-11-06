# check_setup.py: is Python installed?

A 3-line file that proves Python works on your computer. Part of the "Python From Zero" series (episode 2).

## Run it
1. Install Python from python.org. In the installer, tick **Add python.exe to PATH** before you click Install Now.
2. Install VS Code (free) from code.visualstudio.com.
3. In VS Code open this folder, open `check_setup.py`, then open the terminal (Terminal > New Terminal) and type:

```
python check_setup.py
```

You should see `Python is working!` and your version number.

## If you see "python is not recognized" (or "Python was not found")
1. Close VS Code completely and open it again, then retry.
2. Try `py check_setup.py` instead.
3. Run the Python installer again, click **Modify**, tick **Add Python to environment variables**, finish, restart VS Code.
