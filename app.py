
print("STUDENT PERFORMANCE ANALYZER")

name = input("Enter your name: ")
marks = float(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter a value from 0 to 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

if 0 <= marks <= 100:
    if marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")

