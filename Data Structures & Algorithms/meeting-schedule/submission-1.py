"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            meeting1 = intervals[i]
            meeting2 = intervals[i+1]
            if meeting2.start < meeting1.end:
                return False
        return True
