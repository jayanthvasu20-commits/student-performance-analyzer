
import sqlite3
from pathlib import Path

# Store the database beside this Python file
DB_PATH = Path(__file__).resolve().parent / "students.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                marks REAL NOT NULL CHECK(marks >= 0 AND marks <= 100),
                grade TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def add_student(name, marks, grade, result):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO students (name, marks, grade, result)
            VALUES (?, ?, ?, ?)
            """,
            (name, marks, grade, result)
        )


def get_all_students():
    with get_connection() as connection:
        rows = connection.execute("""
            SELECT id, name, marks, grade, result, created_at
            FROM students
            ORDER BY id DESC
        """).fetchall()

    return rows


def delete_student(student_id):
    with get_connection() as connection:
        connection.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

def update_student(student_id, name, marks, grade, result):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE students
            SET name = ?, marks = ?, grade = ?, result = ?
            WHERE id = ?
            """,
            (name, marks, grade, result, student_id)
        )

def validate_student_input(name, marks):
    """Return an error message if the input is invalid."""

    if not isinstance(name, str) or not name.strip():
        return "Student name cannot be empty."

    try:
        marks = float(marks)
    except (ValueError, TypeError):
        return "Marks must be a valid number."

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100."

    return None

def validate_student_input(name, marks):
    """Validate a student's name and marks."""

    if not isinstance(name, str) or not name.strip():
        return "Student name cannot be empty."

    try:
        marks = float(marks)
    except (ValueError, TypeError):
        return "Marks must be a valid number."

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100."

    return None
