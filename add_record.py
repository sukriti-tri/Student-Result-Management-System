"""
add_record.py
-------------
Functional Module 1: Add a new student record OR update an existing one.
"""

from data_handler import load_all_records, save_all_records, record_exists
from utils import calculate_percentage, calculate_grade, get_valid_int, get_non_empty_string


def add_student():
    """Take student details from the user, calculate result, and save to file."""
    roll_no = get_non_empty_string("Enter Roll Number: ")

    if record_exists(roll_no):
        print("A student with this Roll Number already exists. Use 'Update Record' instead.\n")
        return

    name = get_non_empty_string("Enter Student Name: ")
    print("Enter marks (out of 100) for 3 subjects:")
    sub1 = get_valid_int("  Subject 1: ")
    sub2 = get_valid_int("  Subject 2: ")
    sub3 = get_valid_int("  Subject 3: ")

    marks = [sub1, sub2, sub3]
    total = sum(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    new_record = {
        "RollNo": roll_no,
        "Name": name,
        "Sub1": sub1,
        "Sub2": sub2,
        "Sub3": sub3,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade,
    }

    records = load_all_records()
    records.append(new_record)
    save_all_records(records)

    print(f"\nRecord added successfully for {name} (Roll No: {roll_no})")
    print(f"Total: {total}  Percentage: {percentage}%  Grade: {grade}\n")


def update_student():
    """Update marks for an existing student and recalculate their result."""
    roll_no = get_non_empty_string("Enter Roll Number to update: ")
    records = load_all_records()

    for record in records:
        if record["RollNo"] == roll_no:
            print(f"Updating record for {record['Name']}")
            sub1 = get_valid_int("  New Subject 1 marks: ")
            sub2 = get_valid_int("  New Subject 2 marks: ")
            sub3 = get_valid_int("  New Subject 3 marks: ")

            marks = [sub1, sub2, sub3]
            total = sum(marks)
            percentage = calculate_percentage(marks)
            grade = calculate_grade(percentage)

            record.update({
                "Sub1": sub1, "Sub2": sub2, "Sub3": sub3,
                "Total": total, "Percentage": percentage, "Grade": grade,
            })

            save_all_records(records)
            print(f"Record updated. New Percentage: {percentage}%  Grade: {grade}\n")
            return

    print("No student found with that Roll Number.\n")