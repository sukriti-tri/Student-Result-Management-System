"""
search_record.py
-----------------
Functional Module 2: Search for a specific student, or view all records.
"""

from data_handler import load_all_records
from utils import get_non_empty_string


def print_record(record):
    print("-" * 40)
    print(f"Roll No     : {record['RollNo']}")
    print(f"Name        : {record['Name']}")
    print(f"Subject 1   : {record['Sub1']}")
    print(f"Subject 2   : {record['Sub2']}")
    print(f"Subject 3   : {record['Sub3']}")
    print(f"Total       : {record['Total']}")
    print(f"Percentage  : {record['Percentage']}%")
    print(f"Grade       : {record['Grade']}")
    print("-" * 40)


def search_student():
    """Search a student by roll number and display their record."""
    roll_no = get_non_empty_string("Enter Roll Number to search: ")
    records = load_all_records()

    for record in records:
        if record["RollNo"] == roll_no:
            print_record(record)
            return

    print("No student found with that Roll Number.\n")


def view_all_students():
    """Display every record currently stored."""
    records = load_all_records()
    if not records:
        print("No records found yet. Add a student first.\n")
        return

    print(f"\nTotal Students: {len(records)}")
    for record in records:
        print_record(record)