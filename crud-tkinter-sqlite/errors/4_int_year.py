year_text = "third"  # typed into the Year box

if year_text.isdigit():
    print(int(year_text))
else:
    print("Year must be a number.")

print(int(year_text))  # without the check: crash
