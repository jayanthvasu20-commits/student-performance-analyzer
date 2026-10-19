
import pandas as pd

print("STUDENT PERFORMANCE ANALYZER")
print("-" * 35)

students = []

while True:
    name = input("\nEnter student name (or 'done' to finish): ")

    if name.strip().lower() == "done":
        break

    if not name.strip():
        print("Name cannot be empty.")
        continue

    try:
        marks = float(input("Enter marks out of 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        continue

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

    students.append({
        "Name": name.strip(),
        "Marks": marks,
        "Grade": grade,
        "Result": result
    })

    print(f"Added {name.strip()} successfully!")

if students:
    df = pd.DataFrame(students)

    print("\nSTUDENT RESULTS")
    print(df.to_string(index=False))

    print(f"\nClass average: {df['Marks'].mean():.2f}")
    print(f"Students passed: {(df['Result'] == 'PASS').sum()}")
    print(f"Students failed: {(df['Result'] == 'FAIL').sum()}")

    df.to_csv("student_results.csv", index=False)
    print("\nResults saved to student_results.csv")
else:
    print("\nNo student records were entered.")
