
import pandas as pd

from student_analyzer.analysis import calculate_statistics
from student_analyzer.charts import create_student_chart


def main():
    df = pd.read_csv("students.csv")

    print("STUDENT DATA")
    print(df.to_string(index=False))

    stats = calculate_statistics(df)

    print("\nCLASS STATISTICS")
    print(f"Average marks: {stats['average']:.2f}")
    print(f"Highest marks: {stats['highest']}")
    print(f"Lowest marks: {stats['lowest']}")
    print(f"Students passed: {stats['passed']}")
    print(f"Students failed: {stats['failed']}")

    create_student_chart(df)
    print("\nChart saved as student_performance.png")


if __name__ == "__main__":
    main()
