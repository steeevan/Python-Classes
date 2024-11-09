# Student Data Management System

## Project Overview

This project implements a Student Data Management System using Object-Oriented Programming (OOP) in Python. The system allows managing student information, classes, grades, and GPA calculation. It also includes file handling to save and retrieve data.

---

## Features

1. **Add Students**: Add new students with their name, age, and ID.
2. **Enroll Classes**: Enroll students in classes.
3. **Add Grades**: Assign grades to students for specific classes.
4. **View Student Information**: Display all details about a student.
5. **Calculate GPA**: Automatically calculate the GPA based on grades.
6. **Data Persistence**: Save and load student data using JSON files.

---

## Class Design

### `Student` Class
- **Attributes**:
  - `name`: Student's name.
  - `age`: Student's age.
  - `student_id`: Unique ID for the student.
  - `grades`: Dictionary mapping classes to grades.
  - `classes`: List of enrolled classes.
- **Methods**:
  - `add_class(class_name)`: Enroll the student in a class.
  - `add_grade(class_name, grade)`: Assign a grade to a class.
  - `get_gpa()`: Calculate the student's GPA.
  - `display_info()`: Display student's details.

### `StudentManagementSystem` Class
- **Attributes**:
  - `students`: Dictionary mapping student IDs to `Student` objects.
- **Methods**:
  - `add_student(name, age, student_id)`: Add a new student.
  - `remove_student(student_id)`: Remove a student by ID.
  - `view_student(student_id)`: Display student details.
  - `save_to_file(filename)`: Save all student data to a JSON file.
  - `load_from_file(filename)`: Load student data from a JSON file.

---



---

## Author
Created by [Your Name]
