# Problem Statement

## Problem Statement

Keeping track of student marks manually and calculating totals, percentages, grades, averages, and toppers is a time-consuming, error-prone task, especially as the number of students to handle grows. Teachers and administration require a simple and reliable tool to record, store, search, update and analyse student results without having to rely on a time-consuming spreadsheet or paper register.

## Scope of the Project

The project is a console (command-line) based Student Result Management System, implemented in Python. The following features are included in the project:

- Entering each student's marks for 3 subjects
- Calculating total marks, percentage, and grade
- Storing the results in a file, to prevent data loss between sessions
- Updating marks records of a student
- Searching and viewing records of one or all students
- Generating reports on the class performance

The implementation does not include a Graphical User Interface, multi-user features, or a database backend - the scope of the project is to implement a local, single-user, file-backed student result tracking application suitable for a beginner-level programming class.

## Target Users

The target users of this application are:

- Teachers - for record keeping and calculating results
- Students - to view a summary of their results
- Coordinators - to view a summary of the class performance

## High-Level Features

### 1. Add / Update Student Record

Records of individual students can be added or updated, including entering or modifying the marks for each subject; the application will calculate the total marks, percentage, and grade.

### 2. Search / View Records

Existing records can be searched by a student's roll number; the information of all students can also be viewed at once.

### 3. Report Generation

The application can show a report of the class performance, including average marks, the topper (highest-performing) student, pass and fail counts, and the number of students against each grade.