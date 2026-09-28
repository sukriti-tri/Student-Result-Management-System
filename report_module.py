"""
report_module.py
-----------------
Functional Module 3: Reporting & Analytics.
Generates a class-level summary: average, topper, grade distribution.
"""

from data_handler import load_all_records


def generate_report():
    records = load_all_records()

    if not records:
        print("No records available to generate a report.\n")
        return

    percentages = [float(r["Percentage"]) for r in records]
    class_average = round(sum(percentages) / len(percentages), 2)

    topper = max(records, key=lambda r: float(r["Percentage"]))

    grade_counts = {}
    for r in records:
        grade_counts[r["Grade"]] = grade_counts.get(r["Grade"], 0) + 1

    pass_count = sum(1 for r in records if r["Grade"] != "F (Fail)")
    fail_count = len(records) - pass_count

    print("\n===== CLASS RESULT REPORT =====")
    print(f"Total Students   : {len(records)}")
    print(f"Class Average    : {class_average}%")
    print(f"Topper           : {topper['Name']} (Roll No: {topper['RollNo']}, {topper['Percentage']}%)")
    print(f"Pass / Fail      : {pass_count} passed, {fail_count} failed")
    print("Grade Distribution:")
    for grade, count in sorted(grade_counts.items()):
        print(f"   {grade} : {count} student(s)")
    print("================================\n")