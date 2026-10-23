
import sqlite3
import pandas as pd
import streamlit as st

from database import DB_PATH, initialize_database, validate_student_input


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# DATABASE AND VALIDATION HELPERS
# --------------------------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    return "F"


def calculate_result(marks):
    return "PASS" if marks >= 40 else "FAIL"


def load_students():
    with sqlite3.connect(DB_PATH) as connection:
        return pd.read_sql_query("""
            SELECT id, name, marks, grade, result, created_at
            FROM students
            ORDER BY id DESC;
        """, connection)


def show_database_error(error):
    st.error("A database operation failed. Please try again.")
    # Detailed diagnostic information for local development.
    st.caption(f"Details: {error}")


# --------------------------------------------------
# INITIALIZE APPLICATION
# --------------------------------------------------
st.title("🎓 Student Performance Analyzer")
st.write(
    "Manage student records, analyze marks, "
    "and generate performance reports."
)

try:
    initialize_database()
except sqlite3.Error as error:
    st.error("Could not initialize the student database.")
    st.caption(f"Details: {error}")
    st.stop()


# --------------------------------------------------
# ADD STUDENT
# --------------------------------------------------
st.header("➕ Add Student")

with st.form("add_student_form", clear_on_submit=True):
    new_name = st.text_input("Student name")

    new_marks = st.number_input(
        "Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=1.0
    )

    submitted = st.form_submit_button(
        "Add Student",
        type="primary"
    )

    if submitted:
        error = validate_student_input(new_name, new_marks)

        if error:
            st.error(error)
        else:
            name = new_name.strip()
            marks = float(new_marks)
            grade = calculate_grade(marks)
            result = calculate_result(marks)

            try:
                with sqlite3.connect(DB_PATH) as connection:
                    connection.execute("""
                        INSERT INTO students
                            (name, marks, grade, result)
                        VALUES (?, ?, ?, ?);
                    """, (name, marks, grade, result))

                st.success(f"Student '{name}' added successfully!")
                st.rerun()

            except sqlite3.Error as error:
                show_database_error(error)


# --------------------------------------------------
# LOAD CURRENT DATA
# --------------------------------------------------
try:
    students_df = load_students()
except (sqlite3.Error, pd.errors.DatabaseError) as error:
    st.error("Could not load student records.")
    st.caption(f"Details: {error}")
    st.stop()


# --------------------------------------------------
# OVERALL STATISTICS
# --------------------------------------------------
st.header("📊 Performance Overview")

with sqlite3.connect(DB_PATH) as connection:
    total, average, highest, lowest, passed = connection.execute("""
        SELECT
            COUNT(*),
            AVG(marks),
            MAX(marks),
            MIN(marks),
            COALESCE(
                SUM(CASE WHEN marks >= 40 THEN 1 ELSE 0 END),
                0
            )
        FROM students;
    """).fetchone()

pass_percentage = (
    passed / total * 100 if total > 0 else 0
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Students", total)
col2.metric(
    "Average Marks",
    f"{average:.2f}" if average is not None else "N/A"
)
col3.metric(
    "Highest Marks",
    f"{highest:g}" if highest is not None else "N/A"
)
col4.metric(
    "Lowest Marks",
    f"{lowest:g}" if lowest is not None else "N/A"
)
col5.metric("Pass Percentage", f"{pass_percentage:.1f}%")


# --------------------------------------------------
# GRADE DISTRIBUTION
# --------------------------------------------------
st.header("📈 Grade Distribution")

if not students_df.empty:
    grade_data = (
        students_df.groupby("grade")
        .size()
        .reset_index(name="Students")
        .sort_values("grade")
    )

    st.bar_chart(
        grade_data.set_index("grade"),
        y="Students"
    )
else:
    st.info("Add students to see the grade distribution.")


# --------------------------------------------------
# SEARCH AND FILTER
# --------------------------------------------------
st.header("🔎 Search and Filter Students")

col_search, col_grade = st.columns(2)

with col_search:
    search_name = st.text_input(
        "Search by student name",
        placeholder="Enter a name"
    )

with col_grade:
    grade_options = ["All Grades"] + sorted(
        students_df["grade"].dropna().unique().tolist()
    )

    selected_grade = st.selectbox(
        "Filter by grade",
        grade_options
    )

filtered_df = students_df.copy()

if search_name.strip():
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(
            search_name.strip(),
            case=False,
            na=False,
            regex=False
        )
    ]

if selected_grade != "All Grades":
    filtered_df = filtered_df[
        filtered_df["grade"] == selected_grade
    ]

display_columns = ["id", "name", "marks", "grade", "result"]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)

st.caption(f"Showing {len(filtered_df)} student(s)")


# --------------------------------------------------
# CSV DOWNLOAD
# --------------------------------------------------
st.download_button(
    label="📥 Download Filtered Report (CSV)",
    data=filtered_df[display_columns].to_csv(
        index=False
    ).encode("utf-8"),
    file_name="student_performance_report.csv",
    mime="text/csv"
)


# --------------------------------------------------
# EDIT STUDENT
# --------------------------------------------------
st.header("✏️ Edit Student")

if students_df.empty:
    st.info("Add a student before using the edit section.")
else:
    student_options = students_df[
        ["id", "name", "marks"]
    ].to_dict("records")

    selected_student = st.selectbox(
        "Choose a student to edit",
        student_options,
        format_func=lambda student: (
            f"ID {student['id']} — {student['name']} "
            f"({student['marks']} marks)"
        ),
        key="edit_student"
    )

    with st.form("edit_student_form"):
        edit_name = st.text_input(
            "Updated name",
            value=selected_student["name"]
        )

        edit_marks = st.number_input(
            "Updated marks",
            min_value=0.0,
            max_value=100.0,
            value=float(selected_student["marks"]),
            step=1.0
        )

        edit_submitted = st.form_submit_button("Save Changes")

        if edit_submitted:
            error = validate_student_input(edit_name, edit_marks)

            if error:
                st.error(error)
            else:
                name = edit_name.strip()
                marks = float(edit_marks)
                grade = calculate_grade(marks)
                result = calculate_result(marks)

                try:
                    with sqlite3.connect(DB_PATH) as connection:
                        cursor = connection.execute("""
                            UPDATE students
                            SET name = ?, marks = ?, grade = ?, result = ?
                            WHERE id = ?;
                        """, (
                            name,
                            marks,
                            grade,
                            result,
                            selected_student["id"]
                        ))

                    if cursor.rowcount == 0:
                        st.warning("The student record was not found.")
                    else:
                        st.success("Student updated successfully!")
                        st.rerun()

                except sqlite3.Error as error:
                    show_database_error(error)


# --------------------------------------------------
# DELETE STUDENT
# --------------------------------------------------
st.header("🗑️ Delete Student")

if students_df.empty:
    st.info("There are no student records to delete.")
else:
    delete_options = students_df[
        ["id", "name", "marks"]
    ].to_dict("records")

    selected_delete = st.selectbox(
        "Choose a student to delete",
        delete_options,
        format_func=lambda student: (
            f"ID {student['id']} — {student['name']} "
            f"({student['marks']} marks)"
        ),
        key="delete_student"
    )

    confirm_delete = st.checkbox(
        f"I confirm that I want to delete "
        f"{selected_delete['name']}.",
        key="confirm_delete"
    )

    if st.button(
        "Delete Selected Student",
        type="secondary"
    ):
        if not confirm_delete:
            st.warning("Please confirm before deleting.")
        else:
            try:
                with sqlite3.connect(DB_PATH) as connection:
                    cursor = connection.execute(
                        "DELETE FROM students WHERE id = ?;",
                        (selected_delete["id"],)
                    )

                if cursor.rowcount == 0:
                    st.warning("The student record was not found.")
                else:
                    st.success("Student deleted successfully!")
                    st.rerun()

            except sqlite3.Error as error:
                show_database_error(error)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption(
    "Student Performance Analyzer | "
    "Python • Streamlit • SQLite • SQL"
)
