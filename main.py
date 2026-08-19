"""
Entry point for the Student Performance Analyzer.

Loads the dataset, runs the analysis, and prints a formatted report.
"""

from data.students import STUDENTS, SUBJECTS
from src.analyzer import (
    build_score_matrix,
    compute_class_average,
    compute_highest_score,
    compute_lowest_score,
    compute_subject_averages,
    find_top_student,
    get_letter_grade,
    count_students,
)


def print_report() -> None:
    """Run the full analysis and print a formatted report to the console."""
    scores = build_score_matrix(STUDENTS, SUBJECTS)

    total_students = count_students(STUDENTS)
    class_average = compute_class_average(scores)
    highest = compute_highest_score(scores)
    lowest = compute_lowest_score(scores)
    subject_averages = compute_subject_averages(scores, SUBJECTS)
    top_name, top_average = find_top_student(scores, STUDENTS)
    top_grade = get_letter_grade(top_average)

    print("╔══════════════════════════════════════╗")
    print("║      STUDENT PERFORMANCE REPORT       ║")
    print("╚══════════════════════════════════════╝")
    print()
    print(f"Students analyzed : {total_students}")
    print(f"Class average     : {class_average:.2f}%")
    print(f"Highest score     : {highest:.0f}%")
    print(f"Lowest score      : {lowest:.0f}%")
    print()
    print(f"Top Student       : {top_name}")
    print(f"Overall Score     : {top_average:.1f}%")
    print(f"Grade             : {top_grade}")
    print()
    print("Subject Averages")
    print("────────────────────────")
    for subject, average in subject_averages.items():
        print(f"{subject.capitalize():<18}{average:.1f}")


if __name__ == "__main__":
    print_report()