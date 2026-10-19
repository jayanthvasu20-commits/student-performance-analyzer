
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("students.csv")

# Display all student records
print("STUDENT DATA")
print(df.to_string(index=False))

# Calculate statistics
print("\nCLASS STATISTICS")
print("Average marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())
print("Students passed:", (df["Marks"] >= 40).sum())
print("Students failed:", (df["Marks"] < 40).sum())

# Create a bar chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Performance")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("student_performance.png")
plt.show()

print("\nChart saved as student_performance.png")
