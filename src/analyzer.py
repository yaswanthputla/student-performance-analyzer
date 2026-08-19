"""
Core analysis logic for the Student Performance Analyzer.

Converts raw student records into NumPy arrays and provides
functions to compute statistics over them.
"""

import numpy as np


def build_score_matrix(students: list[dict], subjects: list[str]) -> np.ndarray:
    """
    Convert a list of student dicts into a 2D NumPy array of scores.

    Each row = one student, each column = one subject, in the
    order given by `subjects`.

    Args:
        students: list of dicts, each with a "name" key and one
                  numeric key per subject (e.g. "python": 91).
        subjects: ordered list of subject keys to extract.

    Returns:
        A NumPy array of shape (num_students, num_subjects).

    Raises:
        ValueError: if `students` is empty.
    """
    if not students:
        raise ValueError("students list cannot be empty")

    rows = []
    for student in students:
        row = [student[subject] for subject in subjects]
        rows.append(row)

    return np.array(rows)



def compute_class_average(scores: np.ndarray) -> float:
    """
    Compute the overall class average across all students and subjects.

    Args:
        scores: 2D array of shape (num_students, num_subjects).

    Returns:
        The mean of all scores, as a single float.
    """
    return float(np.mean(scores))


def compute_highest_score(scores: np.ndarray) -> float:
    """
    Find the single highest score in the entire dataset.

    Args:
        scores: 2D array of shape (num_students, num_subjects).

    Returns:
        The highest score, as a float.
    """
    return float(np.max(scores))


def compute_lowest_score(scores: np.ndarray) -> float:
    """
    Find the single lowest score in the entire dataset.

    Args:
        scores: 2D array of shape (num_students, num_subjects).

    Returns:
        The lowest score, as a float.
    """
    return float(np.min(scores))



def compute_subject_averages(scores: np.ndarray, subjects: list[str]) -> dict[str, float]:
    """
    Compute the average score for each subject.

    Args:
        scores: 2D array of shape (num_students, num_subjects).
        subjects: ordered list of subject names matching the
                  columns of `scores`.

    Returns:
        A dict mapping each subject name to its average score,
        e.g. {"python": 82.4, "mathematics": 75.8, ...}
    """
    column_averages = np.mean(scores, axis=0)
    return {subject: float(avg) for subject, avg in zip(subjects, column_averages)}



def compute_student_averages(scores: np.ndarray, students: list[dict]) -> dict[str, float]:
    """
    Compute each student's average score across all their subjects.

    Args:
        scores: 2D array of shape (num_students, num_subjects).
        students: original list of student dicts, in the same row
                  order as `scores` (used to get each student's name).

    Returns:
        A dict mapping each student's name to their average score,
        e.g. {"Rahul": 91.6, "Sneha": 78.0, ...}
    """
    row_averages = np.mean(scores, axis=1)
    names = [student["name"] for student in students]
    return {name: float(avg) for name, avg in zip(names, row_averages)}


def find_top_student(scores: np.ndarray, students: list[dict]) -> tuple[str, float]:
    """
    Find the student with the highest average score.

    Args:
        scores: 2D array of shape (num_students, num_subjects).
        students: original list of student dicts, in the same row
                  order as `scores`.

    Returns:
        A tuple of (student_name, their_average_score).
    """
    row_averages = np.mean(scores, axis=1)
    top_index = int(np.argmax(row_averages))
    top_name = students[top_index]["name"]
    top_average = float(row_averages[top_index])
    return top_name, top_average