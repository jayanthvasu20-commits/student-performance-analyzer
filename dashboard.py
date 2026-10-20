
import streamlit as st
import pandas as pd

from database import (
    initialize_database,
    add_student,
    get_all_students,
    update_student,
    delete_student,
)

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide",
)

# Create the database table if it doesn't exist
initialize_database()

st.title("📊 Student Performance Analyzer")
st.write("Add students, analyze performance, and save records permanently.")

# Add student form
with st.form("student_form", clear_on_submit=True):
    st.subheader("Add a student")

    name = st.text_input("Student name")
    marks = st.number_input(
        "Marks out of 100",
        min_value=0.0,
        max_value=100.0,
        step=1.0,
    )

    submitted = st.form_submit_button("Save student")

if submitted:
    if not name.strip():
        st.error("Please enter a student name.")
    else:
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"

        result = "PASS" if marks >= 40 else "FAIL"

        add_student(name.strip(), marks, grade, result)
        st.success(f"Saved {name.strip()} to the database!")
        st.rerun()

# Load saved records from SQLite
records = get_all_students()

if records:
    df = pd.DataFrame(
        records,
        columns=[
            "ID", "Name", "Marks", "Grade", "Result", "Created At"
        ],
    )

    st.subheader("Saved student records")
    st.dataframe(df, use_container_width=True, hide_index=True)

    average = df["Marks"].mean()
    passed = int((df["Result"] == "PASS").sum())
    failed = int((df["Result"] == "FAIL").sum())

    col1, col2, col3 = st.columns(3)
    col1.metric("Class average", f"{average:.2f}")
    col2.metric("Passed", passed)
    col3.metric("Failed", failed)

    st.subheader("Marks chart")
    
    chart_data = df.sort_values("Name").set_index("Name")[["Marks"]]
    st.bar_chart(chart_data)

    # Download saved data
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download student records (CSV)",
        data=csv_data,
        file_name="student_results.csv",
        mime="text/csv",
    )

    
# Edit an existing student
st.subheader("Edit a student")

if not df.empty:
    selected_id = st.selectbox(
        "Choose a student ID to edit",
        df["ID"].tolist(),
        format_func=lambda sid: (
            f"{df.loc[df['ID'] == sid, 'Name'].iloc[0]} "
            f"(ID: {sid})"
        ),
        key="edit_student_id",
    )

    student = df.loc[df["ID"] == selected_id].iloc[0]

    with st.form("edit_student_form"):
        edited_name = st.text_input(
            "Student name",
            value=str(student["Name"]),
        )

        edited_marks = st.number_input(
            "Marks out of 100",
            min_value=0.0,
            max_value=100.0,
            value=float(student["Marks"]),
            step=1.0,
        )

        update_clicked = st.form_submit_button("Update student")

    if update_clicked:
        if not edited_name.strip():
            st.error("Student name cannot be empty.")
        else:
            if edited_marks >= 90:
                edited_grade = "A"
            elif edited_marks >= 75:
                edited_grade = "B"
            elif edited_marks >= 60:
                edited_grade = "C"
            elif edited_marks >= 40:
                edited_grade = "D"
            else:
                edited_grade = "F"

            edited_result = (
                "PASS" if edited_marks >= 40 else "FAIL"
            )

            update_student(
                int(selected_id),
                edited_name.strip(),
                edited_marks,
                edited_grade,
                edited_result,
            )

            st.success("Student updated successfully!")
            st.rerun()

# Delete an existing student
st.subheader("Delete a student")

if not df.empty:
    delete_id = st.selectbox(
        "Choose a student ID to delete",
        df["ID"].tolist(),
        format_func=lambda sid: (
            f"{df.loc[df['ID'] == sid, 'Name'].iloc[0]} "
            f"(ID: {sid})"
        ),
        key="delete_student_id",
    )

    if st.button("Delete selected student", type="secondary"):
        delete_student(int(delete_id))
        st.success("Student deleted successfully!")
        st.rerun()

