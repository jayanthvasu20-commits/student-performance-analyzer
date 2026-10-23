
# 🎓 Student Performance Analyzer

A Python-based web application that helps manage student records, analyze academic performance, and generate interactive reports using Streamlit, SQLite, and SQL.

## 🚀 Features

- **Student Management:** Add, edit, and delete student records.
- **SQLite Database:** Persist student data between sessions.
- **Input Validation:** Validate student names and marks before saving.
- **Error Handling:** Handle common database and input errors.
- **Performance Analytics:** View total students, average marks, highest marks, and lowest marks.
- **Pass Percentage:** Calculate the percentage of students scoring 40 or above.
- **Grade Distribution:** Visualize the distribution of student grades.
- **Search and Filtering:** Search by name and filter by grade.
- **CSV Export:** Download student reports for further analysis.
- **SQL Practice:** Explore queries, aggregations, joins, views, subqueries, and indexes.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| SQLite | Database storage |
| SQL | Queries and reporting |
| Pandas | Data processing |
| Matplotlib | Data visualization |

## 📁 Project Structure

```text
StudentsPA/
├── dashboard.py
├── database.py
├── app.py
├── analyze_data.py
├── practice_sql.py
├── test_validation.py
├── student_analyzer/
├── students.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jayanthvasu20-commits/student-performance-analyzer.git
cd student-performance-analyzer
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run dashboard.py
```

Streamlit will display a local URL in the terminal. Open it in your browser.

## 📊 Grading System

| Marks | Grade | Result |
|---:|---|---|
| 90–100 | A | PASS |
| 75–89.99 | B | PASS |
| 60–74.99 | C | PASS |
| 40–59.99 | D | PASS |
| Below 40 | F | FAIL |

## 🗄️ Database

The application uses SQLite to store student records locally. The database is created automatically when the dashboard initializes.

The local database file is excluded from Git using `.gitignore`.

## 🧪 Validation Tests

Run the input validation tests with:

```bash
python test_validation.py
```

## 🔮 Future Improvements

- User authentication and role-based access
- More detailed subject-wise analytics
- Automated testing with `pytest`
- Cloud deployment with a suitable persistent database
- Student performance trends over time

## 👨‍💻 Author

**Jayanth Vasu**

GitHub: [@jayanthvasu20-commits](https://github.com/jayanthvasu20-commits)

---

*Built as a learning project to practice Python, SQL, databases, and interactive data analytics.*
