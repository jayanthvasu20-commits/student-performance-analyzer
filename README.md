# Student Performance Analyzer 📊

A beginner-friendly Python project that analyzes student marks and assigns grades and pass/fail results.

## Features

- Accepts the student's name and marks.
- Validates marks between 0 and 100.
- Assigns grades based on the marks.
- Displays the student's result.

## Technologies Used

- Python
- Git and GitHub
- pandas (installed for future data analysis features)

## Grading System

| Marks | Grade |
|---|---|
| 90–100 | A |
| 75–89.99 | B |
| 60–74.99 | C |
| 40–59.99 | D |
| Below 40 | F |

Students scoring 40 or above pass.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/jayanthvasu20-commits/student-performance-analyzer.git
cd student-performance-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the program

```bash
python app.py
```

## Example Output

```text
STUDENT PERFORMANCE ANALYZER
Enter your name: Jayanth
Enter your marks out of 100: 85
Grade: B
Result: PASS
```

## Future Improvements

- Store marks for multiple students.
- Calculate average marks and class statistics.
- Analyze student data using pandas.
- Add visualizations and machine learning features.

## Author

Jayanth
