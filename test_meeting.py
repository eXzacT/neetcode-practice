from test_data import meetings
from meeting import *


def test_meetings():
    """ Function correctly calculates how many rooms are needed so all the meetings can happen simultaneously (28/10/2023) """

    for meeting in meetings:
        expected_rooms = meeting["needed_rooms"]
        meeting_times = meeting["meeting_time"]
        assert min_meeting_rooms(
            meeting_times) == expected_rooms, f"Failed for meeting times: {meeting_times}"
