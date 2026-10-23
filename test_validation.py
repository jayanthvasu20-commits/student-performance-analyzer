
from database import validate_student_input

test_cases = [
    ("Rahul", 85),
    ("", 85),
    ("   ", 85),
    ("Priya", "abc"),
    ("Arjun", 150),
    ("Sneha", -5),
    ("Kiran", 0),
    ("Adam", 100),
]

for name, marks in test_cases:
    error = validate_student_input(name, marks)

    if error is None:
        print(f"VALID: name={name!r}, marks={marks!r}")
    else:
        print(f"INVALID: name={name!r}, marks={marks!r}")
        print(f"  Reason: {error}")
