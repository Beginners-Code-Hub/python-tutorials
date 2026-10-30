# Python Decorators Explained: source code

Code from the video, one file per step. Standard library only, nothing to install.
Works on Python 3.8 or newer (tested on Python 3.12).

## Run
From this folder:

```
python steps/step-01-functions-are-objects.py
python steps/step-02-wrap-by-hand.py
python steps/step-03-at-syntax.py
python steps/step-04-arguments-broken.py   # shows the TypeError on purpose
python steps/step-04-arguments.py
python steps/step-05-timer.py
python steps/step-06-wraps-problem.py      # prints "wrapper" and "None"
python steps/step-06-wraps.py
python steps/step-07-retry.py
python demo.py                             # @timer on three functions
```

On macOS/Linux use `python3` if `python` is not found.

## Files
- `steps/`: the exact code shown in each step of the video
- `decorators.py`: the final reusable `timer` and `retry(times)` decorators
- `demo.py`: uses `@timer` from `decorators.py`

## Try it yourself
Write a `@log_calls` decorator that writes every call (function name and arguments) to a file.

## Shorts
`shorts/timer.py` + `shorts/demo.py`: the compact timer used in the Short. Run `cd shorts && python demo.py`.
