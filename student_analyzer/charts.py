
import matplotlib.pyplot as plt


def create_student_chart(df, output_path="student_performance.png"):
    """Create and save a bar chart of student marks."""

    plt.figure(figsize=(8, 5))
    plt.bar(df["Name"], df["Marks"])
    plt.title("Student Performance")
    plt.xlabel("Student")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()
