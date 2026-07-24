"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            prev = intervals[i - 1] # (0,30)
            curr = intervals[i]     # (5,10)
            if curr.start < prev.end:
                return False
        return True
