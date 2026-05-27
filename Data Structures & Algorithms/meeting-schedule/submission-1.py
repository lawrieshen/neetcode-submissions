"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort intervals by end time
        intervals.sort(key=lambda x: x.end) # (5, 10) (15, 20) (0, 30)
        # loop thru intervals in range(1, n), check if prev.end < current.start
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
            # if not return False

        # return True
        return True