"""
Raw student performance data.

Each student is represented as a dictionary with their name
and their scores in three subjects: Python, Mathematics, Statistics.
"""

STUDENTS: list[dict] = [
    {"name": "Rahul", "python": 91, "mathematics": 88, "statistics": 96},
    {"name": "Sneha", "python": 78, "mathematics": 82, "statistics": 74},
    {"name": "Arjun", "python": 65, "mathematics": 59, "statistics": 68},
    {"name": "Priya", "python": 88, "mathematics": 91, "statistics": 85},
    {"name": "Kiran", "python": 51, "mathematics": 60, "statistics": 55},
    {"name": "Divya", "python": 73, "mathematics": 70, "statistics": 77},
    {"name": "Aman",  "python": 84, "mathematics": 79, "statistics": 81},
    {"name": "Meera", "python": 96, "mathematics": 93, "statistics": 90},
    {"name": "Vikram","python": 60, "mathematics": 64, "statistics": 58},
    {"name": "Isha",  "python": 79, "mathematics": 76, "statistics": 82},
]

SUBJECTS: list[str] = ["python", "mathematics", "statistics"]