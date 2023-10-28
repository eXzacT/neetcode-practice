import pytest
from copy import deepcopy
from test_data import non_overlapping_intervals, overlapping_intervals
from intervals import *


@pytest.fixture(autouse=True)
def setup_data():
    global non_overlapping_intervals, overlapping_intervals
    from test_data import non_overlapping_intervals, overlapping_intervals
    non_overlapping_intervals = deepcopy(non_overlapping_intervals)
    overlapping_intervals = deepcopy(overlapping_intervals)


def test_inserting_into_intervals():
    """ Test if the interval is properly inserted (28/10/2023) """

    for interval in non_overlapping_intervals:
        expected_intervals = interval["merged_intervals"]
        new_interval = interval["new_interval"]
        intervals = interval["original_intervals"]
        assert insert_new_into_intervals(
            new_interval, intervals) == expected_intervals, f"Failed for intervals: {intervals}"


def test_merging_intervals():
    """ Test if the overlapping intervals are properly merged (28/10/2023) """

    for interval in overlapping_intervals:
        expected_intervals = interval["merged_intervals"]
        intervals = interval["original_intervals"]
        assert merge_intervals(
            intervals) == expected_intervals, f"Failed for intervals: {intervals}"


def test_min_intervals_to_remove():
    """ 
    Test if the function 'min_intervals_to_remove_for_no_overlap' returns the expected 
    minimum number of intervals to remove to stop overlaps. (28/10/2023)
    """

    for interval in overlapping_intervals:
        expected_removals = interval["min_removals_for_no_overlap"]
        intervals = interval["original_intervals"]
        assert min_intervals_to_remove_for_no_overlap(
            intervals) == expected_removals, f"Failed for intervals: {intervals}"
