# /tests/test_helper_functions.py
import pytest
from helper_functions import count_to_proportions

def test_count_to_proportions():
    counts_map = {"Class1": 20, "Class2": 30, "Class3": 50}
    expected_proportions = {"Class1": 0.2, "Class2": 0.3, "Class3": 0.5}
    assert count_to_proportions(counts_map) == expected_proportions
