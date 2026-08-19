# Student Performance Analyzer

A Python + NumPy command-line tool that analyzes student academic performance across multiple subjects — computing class-wide statistics, subject averages, individual student rankings, and grading, all from a clean, modular codebase.

## Features

- Overall class average, highest, and lowest scores
- Subject-wise average scores (Python, Mathematics, Statistics)
- Identifies the top-performing student
- Individual student averages
- Letter grade calculation (A–F)
- Pass/fail status per student
- Clean, formatted console report

## Technologies Used

- Python 3.14
- NumPy

## Project Structure

```
student-performance-analyzer/
│
├── data/
│   └── students.py      # Raw student dataset
│
├── src/
│   └── analyzer.py      # Core analysis logic (NumPy-based)
│
├── main.py               # Entry point — generates the report
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
```
   git clone https://github.com/yaswanthputla/student-performance-analyzer.git
   cd student-performance-analyzer
```

2. Install dependencies:
```
   pip install -r requirements.txt
```

## Usage

Run the analyzer from the project root:

```
python main.py
```

## Example Output

```
╔══════════════════════════════════════╗
║      STUDENT PERFORMANCE REPORT       ║
╚══════════════════════════════════════╝

Students analyzed : 10
Class average     : 76.43%
Highest score     : 96%
Lowest score      : 51%

Top Student       : Meera
Overall Score     : 93.0%
Grade             : A

Subject Averages
────────────────────────
Python            76.5
Mathematics       76.2
Statistics        76.6
```

## Future Improvements

- Accept custom datasets via CSV input
- Add per-student pass/fail breakdown to the report
- Visualize subject performance with charts
- Add unit tests for each analysis function

## Author

Yaswanth Putla