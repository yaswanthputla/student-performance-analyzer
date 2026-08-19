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