if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array of meeting time intervals consisting of start and end times, 
    determine if a person could attend all meetings'''


@time_execution()
def sol(meetings: list[list[int, int]]) -> bool:
    meetings = sorted(meetings)

    for i in range(1, len(meetings)):
        if meetings[i][0] < meetings[i-1][1]:
            return False

    return True
