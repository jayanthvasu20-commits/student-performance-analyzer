
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
