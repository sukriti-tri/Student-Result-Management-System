"""
main.py
-------
Student Result Management System
Entry point: shows the menu and routes the user to the right module.

Run with:  python main.py
"""

from add_record import add_student, update_student
from search_record import search_student, view_all_students
from report_module import generate_report


def show_menu():
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add New Student Record")
    print("2. Update Existing Student Record")
    print("3. Search Student by Roll Number")
    print("4. View All Student Records")
    print("5. Generate Class Report")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Exiting Student Result Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()