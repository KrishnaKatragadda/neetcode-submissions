"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i: i.start)

        prevEnd = intervals[0].end

        for i in intervals[1:]:

            start = i.start
            if prevEnd > start:
                return False
            else:
                prevEnd = i.end
        
        return True


