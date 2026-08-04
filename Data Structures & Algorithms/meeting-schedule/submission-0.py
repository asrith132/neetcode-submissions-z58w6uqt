"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        i = 0
        while i < len(intervals) - 1:
            start = intervals[i].start
            end = intervals[i].end
            next_start = intervals[i + 1].start
            next_end = intervals[i + 1].end

            if end > next_start:
                return False

            i += 1
        return True

