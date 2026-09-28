"""
data_handler.py
----------------
Handles all reading and writing of student records to the CSV file.
This file acts as our simple "database layer" for the project.
"""

import csv
import os

DATA_FILE = "students.csv"
FIELDNAMES = ["RollNo", "Name", "Sub1", "Sub2", "Sub3", "Total", "Percentage", "Grade"]


def initialize_file():
    """Create the CSV file with headers if it does not already exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_all_records():
    """Read all student records from the CSV file and return as a list of dicts."""
    initialize_file()
    with open(DATA_FILE, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_all_records(records):
    """Overwrite the CSV file with the given list of student record dicts."""
    with open(DATA_FILE, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)


def record_exists(roll_no):
    """Check whether a student with the given roll number already exists."""
    records = load_all_records()
    return any(r["RollNo"] == str(roll_no) for r in records)