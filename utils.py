"""
utils.py
--------
Reusable helper functions: percentage/grade calculation and input validation.
Keeping these separate keeps main.py and the other modules clean (Maintainability).
"""


def calculate_percentage(marks_list, max_marks_per_subject=100):
    """Given a list of marks, return the percentage (float, 2 decimal places)."""
    total_max = max_marks_per_subject * len(marks_list)
    total_scored = sum(marks_list)
    percentage = (total_scored / total_max) * 100
    return round(percentage, 2)


def calculate_grade(percentage):
    """Return a letter grade based on percentage. Simple slab-based grading."""
    if percentage >= 90:
        return "S"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F (Fail)"


def get_valid_int(prompt, min_value=0, max_value=100):
    """
    Keep asking the user until a valid integer within range is entered.
    This is our error-handling / input validation strategy (non-functional requirement).
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_empty_string(prompt):
    """Keep asking until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")