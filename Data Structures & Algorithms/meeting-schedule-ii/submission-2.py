"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # if max(start1,start2) < min(end1,end2)

        events = []

        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        
        events.sort()
        res = 0
        cur = 0
        for t, score in events:
            cur += score
            res = max(res,cur)

        return res
        