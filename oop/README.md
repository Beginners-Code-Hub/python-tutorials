# Python OOP: Build a Mini Store Inventory (source code)

Code from the video, one file per step. Standard library only, nothing to install.
Works on Python 3.8 or newer (tested on Python 3.12).

## Run
Open a terminal in this folder:

```
python steps/step-01-dicts.py              # ends with KeyError: 'stock' on purpose
python steps/step-02-first-class.py
python steps/step-03-methods.py
python steps/step-04-print-problem.py      # prints <__main__.Product object at 0x...>
python steps/step-04-str.py
python steps/step-05-class-attributes.py
python steps/step-06-price-problem.py      # a negative price is accepted (the problem)
python steps/step-06-property.py
python steps/step-07-inheritance.py
python steps/step-08-polymorphism.py
python steps/step-09-inventory.py
python demo.py                             # the inventory report from the start of the video
```

On macOS/Linux use `python3` if `python` is not found.

## Files
- `steps/`: the exact code shown in each step of the video
- `store.py`: the final `Product`, `PerishableProduct` and `Inventory` classes
- `demo.py`: builds a small store with `store.py` and prints the report
- `shorts/`: the compact `__str__` example from the Short (`print_problem.py`, then `str_fix.py`)
- `errors/`: the four common mistakes from the video. Each file fails on purpose; read the comment to see the bug.

## Try it yourself
1. Add a `DigitalProduct` class (an e-book) that never runs out of stock: override `sell` and `needs_attention`.
2. Give `Inventory` a `find(name)` method that returns the product with that name.
