
import sqlite3
from database import DB_PATH

with sqlite3.connect(DB_PATH) as connection:
    # Create an index on student names
    connection.execute("""
        CREATE INDEX IF NOT EXISTS idx_students_name
        ON students(name);
    """)

    print("Index created successfully!")

    # Display indexes on the students table
    indexes = connection.execute(
        "PRAGMA index_list('students');"
    ).fetchall()

    print("\nIndexes on students table:")
    for index in indexes:
        print(index)

    # Check how SQLite searches by exact name
    plan = connection.execute("""
        EXPLAIN QUERY PLAN
        SELECT id, name, marks
        FROM students
        WHERE name = ?;
    """, ("Rahul",)).fetchall()

    print("\nQuery execution plan:")
    for row in plan:
        print(row)
