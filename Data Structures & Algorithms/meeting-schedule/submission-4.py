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
        intervals.sort(key = lambda x:x.start)
        cur_end = intervals[0].end

        for inte in intervals[1:]:
            if inte.start < cur_end:
                return False
            
            else :
                cur_end = max(cur_end,inte.end)
        
        return True