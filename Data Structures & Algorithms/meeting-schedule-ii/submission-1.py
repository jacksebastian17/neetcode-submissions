"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for m in intervals:
            events.append((m.start, +1))
            events.append((m.end, -1))

        events.sort(key=lambda x: (x[0], x[1]))

        active = 0
        max_rooms = 0
        for (time, delta) in events:
            active += delta
            max_rooms = max(max_rooms, active)

        return max_rooms